"use strict";
// alert("test");の場合画面がロードされる前に実行される
// window.addEventListener('load', function () {
//   alert("test");
// });の場合ロード後に実行される


function stopWatch() {
  // getElementsByClassNameは一致するもの全件取得
  var startButton = document.getElementsByClassName('startButton')[0];
  var stopButton = document.getElementsByClassName('stopButton')[0];
  var displayElm = document.getElementsByClassName('display')[0];
  var logElm = document.querySelector('.log');
  var timer = null;

  function addMessage(message) {
    var messageElm = document.createElement('div');
    var now = new Date();

    messageElm.innerText = now.getHours() + '時' + now.getMinutes() + '分' + now.getSeconds() + '秒' + message;
    // クラス名を追加
    messageElm.classList = ['message'];
    logElm.appendChild(messageElm);
  }

  startButton.addEventListener('click', function () {
    if (timer === null) {
      var seconds = 0;

      // 返り値として繰り返し処理を識別する数値が返される
      timer = setInterval(function () {
        seconds++;
        // innerTextは中身を上書き
        displayElm.innerText = seconds;
      }, 1000);
      addMessage('開始')
    }
  });

  stopButton.addEventListener('click', function () {
    if (timer !== null) {
      clearInterval(timer);
      timer = null;
      addMessage('終了')
    }
  });
}

window.addEventListener('load', stopWatch)

// 削除ボタンが押された時のイベント
const deleteRecommend = () => {
  return confirm("本当に削除しますか？");
}
