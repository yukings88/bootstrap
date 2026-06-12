/* ==========================================================================
   Yukings Noise Barrier - Shared JavaScript
   Auto-rotation carousel for product details images.
   Shared by product-01.html through product-08.html.
   ========================================================================== */
(function () {
  'use strict';

  function initCarousel(rootId) {
    var carousel = document.getElementById(rootId);
    if (!carousel) return;
    var images = carousel.querySelectorAll('.rsb-details__image');
    var dots = document.querySelectorAll('.rsb-details__dot');
    if (images.length === 0) return;

    var idx = 0;
    var timer;

    function show(n) {
      idx = (n + images.length) % images.length;
      images.forEach(function (img, i) {
        img.classList.toggle('rsb-details__image--active', i === idx);
      });
      dots.forEach(function (d, i) {
        d.classList.toggle('rsb-details__dot--active', i === idx);
      });
    }
    function next() { show(idx + 1); }
    function start() { timer = setInterval(next, 4000); }
    function stop() { clearInterval(timer); }

    dots.forEach(function (d, i) {
      d.addEventListener('click', function () { stop(); show(i); start(); });
    });
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
    start();
  }

  function initCookieBanner() {
    var banner = document.getElementById('rsb-cookie-banner');
    if (!banner) return;
    var buttons = banner.querySelectorAll('button');
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () { banner.style.display = 'none'; });
    });
  }

  function init() {
    initCarousel('rsb-details-carousel');
    initCookieBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
