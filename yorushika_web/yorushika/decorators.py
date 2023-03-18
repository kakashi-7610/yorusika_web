# 関数をデコレーティングすることで関数のスタート、エンド、実行結果をログに吐き出す
import os
import logging
import inspect
from functools import wraps


def function_log(logger):
    CALLED_FILENAME = 'called_filename'
    CALLED_FUNCNAME = 'called_funcname'
    CALLED_LINENO = 'called_lineno'

    class custom_filter(logging.Filter):

        # 呼び出し元メソッド情報にレコードを書き換え
        def filter(self, record):
            record.filename = getattr(record, CALLED_FILENAME, record.filename)
            record.funcName = getattr(record, CALLED_FUNCNAME, record.funcName)
            record.lineno = getattr(record, CALLED_LINENO, record.lineno)

    def decorator(function):

        # このデコレーターとした関数を再度デコレートすることを防ぐ
        # https://blog.pyq.jp/entry/Python_kaiketsu_201201
        @wraps(function)
        def wrapper(*args, **kwargs):
            function_name = function.__name__
            extra = {
                CALLED_FILENAME: os.path.basename(inspect.getfile(function)),
                CALLED_FUNCNAME: function_name,
                CALLED_LINENO: 0
            }

            logger.debug(f'[START]{function_name}{args}', extra=extra)
            result = function(*args, **kwargs)
            logger.debug(f'[END]{function_name}', extra=extra)
            return result

        return wrapper

    logger.addFilter(custom_filter())
    return decorator
