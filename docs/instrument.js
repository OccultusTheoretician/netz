/* instrument.js - SHELL-2026-09-04. The workpaper shell needs one behaviour: copy a
   receipt value. Everything else in the shell is markup and CSS. A copy button
   names what it does ("copy") and what it did ("copied"), and returns to its
   name; if the clipboard is unavailable the button says so instead of failing
   silently. ASCII only. */
(function () {
  "use strict";
  function setDone(btn, text) {
    var was = btn.textContent;
    btn.textContent = text; btn.setAttribute("data-done", "1");
    setTimeout(function () { btn.textContent = was; btn.removeAttribute("data-done"); }, 1600);
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest(".wp-copy") : null;
    if (!btn) return;
    var sel = btn.getAttribute("data-copy");
    var src = sel ? document.querySelector(sel) : btn.previousElementSibling;
    var text = src ? (src.getAttribute("data-value") || src.textContent).trim() : "";
    if (!text) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { setDone(btn, "copied"); },
                                              function () { setDone(btn, "select and copy by hand"); });
    } else {
      setDone(btn, "select and copy by hand");
    }
  });
})();
