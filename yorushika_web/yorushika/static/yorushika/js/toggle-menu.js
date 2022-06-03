window.addEventListener('load', function () {
  var $button = document.querySelector('.toggle-menu');
  var $menu = document.querySelector('.header-menu');
  $button.addEventListener('click', function () {
    if ($menu.classList.contains('-show')) {
      $menu.classList.remove('-show');
    }
    else {
      $menu.classList.add('-show');
    }
  });
});
