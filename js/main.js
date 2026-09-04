/* ==========================================================================
   main.js — shared behaviour
   Loaded by every page with `defer`, so the DOM is ready when this runs.
   Page-specific behaviour belongs in the script named after that page.
   ========================================================================== */

(function () {
  'use strict';

  /* ------------------------------------------------------------------------
     Mobile navigation
     The nav collapses under 620px. Without this the menu is unreachable on a
     phone — which is where a lot of readers will open this.
     ------------------------------------------------------------------------ */
  function initNavToggle() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('site-nav');

    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.textContent = isOpen ? 'Close' : 'Menu';
    });

    /* close the menu if the viewport grows back to desktop while it's open */
    var wide = window.matchMedia('(min-width: 621px)');
    var onChange = function (event) {
      if (event.matches) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.textContent = 'Menu';
      }
    };

    if (typeof wide.addEventListener === 'function') {
      wide.addEventListener('change', onChange);
    } else if (typeof wide.addListener === 'function') {
      wide.addListener(onChange);   /* older Safari */
    }
  }

  /* ------------------------------------------------------------------------
     Colophon year
     Any element with data-current-year gets this year's number.
     ------------------------------------------------------------------------ */
  function initYear() {
    var year = String(new Date().getFullYear());
    var targets = document.querySelectorAll('[data-current-year]');

    for (var i = 0; i < targets.length; i++) {
      targets[i].textContent = year;
    }
  }

  initNavToggle();
  initYear();
})();
