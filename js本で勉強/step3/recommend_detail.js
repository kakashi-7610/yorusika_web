"use strict";
// alert("test");の場合画面がロードされる前に実行される
// window.addEventListener('load', function () {
//   alert("test");
// });の場合ロード後に実行される

// 削除ボタンが押された時のイベント
const deleteRecommend = () => {
  return confirm("本当に削除しますか？");
}

class PhotoViewer {
  // 設計の柔軟性を考え、画像最大数やどの要素にビューアーを作るかは
  // 可変にしたいため、画像と要素は引数で渡すようにする
  constructor(rootElm, images) {
    this.rootElm = rootElm;
    this.images = images;
    this.currentIndex = 0;
  }

  init() {
    const nextButtonElm = this.rootElm.querySelector('.nextButton');
    nextButtonElm.addEventListener('click', () => {
      this.next()
    })

    const prevButtonElm = this.rootElm.querySelector('.prevButton');
    prevButtonElm.addEventListener('click', () => {
      this.prev()
    })

    this.updatePhoto();
  }

  updatePhoto() {
    const frameElm = document.querySelector(".frame");
    const image = this.images[this.currentIndex];
    frameElm.innerHTML = `<div class="currentImage"><img src="${image}" /></div>`;

    this.startTimer();
  }

  startTimer() {
    // すでにタイマーが動作している場合は停止しないと、インターバル処理が
    // 複数個実行されてしまう。
    if (this.timerKey) {
      clearTimeout(this.timerKey)
    }

    // timeoutIDをローカル変数で持ってしまうと関数が呼び出される度にリセットされてしまう。
    // インスタンス変数で持つことでインスタンスが解放されるまで利用できる。

    // setTimeoutは時間切れになったら１度だけ関数を実行する
    // setIntervalは設定した時間間隔で永遠に関数が実行される

    // setIntervalでの繰り返し処理
    // 処理にかかる時間に関係なく指定した秒数ごとに関数が実行される。

    // setTimeoutでの繰り返し処理
    // 関数が終了してから指定した秒数後に関数が実行される。
    this.timerKey = setTimeout(() => {
      this.next();
    }, 3000);
  }

  next() {
    this.currentIndex++;
    if (this.currentIndex === this.images.length) {
      this.currentIndex = 0;
    }

    this.updatePhoto();
  }

  prev() {
    this.currentIndex--;
    if (this.currentIndex < 0) {
      this.currentIndex = this.images.length - 1;
    }

    this.updatePhoto();
  }
}


const execution = () => {
  const rootElm = document.getElementById("photoViewer");
  const images = [
    "https://pbs.twimg.com/media/FawBrCgVQAAEtT0?format=jpg&name=4096x4096",
    "https://pbs.twimg.com/profile_banners/738199700914872320/1659525506/1500x500",
    "https://s3-ap-northeast-1.amazonaws.com/s.okmusic.jp/news_items/images/331503/extra_large.jpg?1554519066"
  ]

  const photoViewer = new PhotoViewer(rootElm, images);
  photoViewer.init();
}

window.addEventListener('load', execution)