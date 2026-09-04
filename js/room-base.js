/* ==========================================================================
   room-base.js — shared room page behaviour
   Loaded by all six room pages. Room-specific behaviour goes in the script
   named after that room, e.g. js/rooms/physics-research.js.
   ========================================================================== */

(function () {
  'use strict';

  /* ------------------------------------------------------------------------
     "In this room" index → entry anchors
     Native anchor jumps work without this. What this adds is a brief
     highlight on the destination, so a reader who jumps from the index to
     entry 1.4 can see where they landed instead of hunting for it.
     ------------------------------------------------------------------------ */
  function initEntryHighlight() {
    var links = document.querySelectorAll('[data-entry-link]');
    if (!links.length) return;

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced) return;

    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function (event) {
        var id = this.getAttribute('href');
        if (!id || id.charAt(0) !== '#') return;

        var target = document.querySelector(id);
        if (!target) return;

        /* let the browser handle the actual scroll */
        window.setTimeout(function () {
          target.classList.add('is-targeted');
          window.setTimeout(function () {
            target.classList.remove('is-targeted');
          }, 1200);
        }, 300);
      });
    }
  }

  initEntryHighlight();
})();
