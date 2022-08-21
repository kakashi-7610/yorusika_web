"use strict";
// alert("test");の場合画面がロードされる前に実行される
// window.addEventListener('load', function () {
//   alert("test");
// });の場合ロード後に実行される

// 削除ボタンが押された時のイベント
const deleteRecommend = () => {
  return confirm("本当に削除しますか？");
}
