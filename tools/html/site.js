/* Behaviour of the HTML documentation: search, light/dark, drawer, image zoom, copy buttons, scroll spy.
   Plain JavaScript, no dependencies. Every page is complete without it. */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  var $ = function (s, r) { return (r || doc).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || doc).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode, file:// */ }
    }
  };
  var ROOT = root.getAttribute("data-root") || "";

  /* smooth scrolling for in-page clicks, but not for deep links or the 190 000 px single file */
  window.addEventListener("load", function () {
    if (!doc.body.hasAttribute("data-single")) root.classList.add("smooth");
  });

  /* ---- light / dark ---- */
  var themeBtn = $("#theme");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme") || "light";     /* light unless the reader chose dark */
      var next = cur === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store.set("ulg-theme", next);
    });
  }

  /* ---- reading progress ---- */
  var bar = $(".progress span");
  if (bar) {
    var pending = false;
    var progress = function () {
      pending = false;
      var h = doc.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? Math.min(100, Math.max(0, window.scrollY / h * 100)) : 0) + "%";
    };
    window.addEventListener("scroll", function () { if (!pending) { pending = true; requestAnimationFrame(progress); } }, { passive: true });
    window.addEventListener("resize", progress);
    progress();
  }

  /* ---- drawer on small screens ---- */
  var menuBtn = $("#menu"), backdrop = $(".backdrop");
  function drawer(open) {
    doc.body.classList.toggle("nav-open", open);
    if (menuBtn) menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (menuBtn) menuBtn.addEventListener("click", function () { drawer(!doc.body.classList.contains("nav-open")); });
  if (backdrop) backdrop.addEventListener("click", function () { drawer(false); });
  $$(".sidebar a").forEach(function (a) { a.addEventListener("click", function () { drawer(false); }); });

  /* ---- copy buttons ---- */
  function copyText(text, done) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(); });
    } else { fallback(); }
    function fallback() {
      var t = doc.createElement("textarea");
      t.value = text; t.style.position = "fixed"; t.style.opacity = "0";
      doc.body.appendChild(t); t.select();
      try { doc.execCommand("copy"); done(); } catch (e) { /* ignore */ }
      doc.body.removeChild(t);
    }
  }
  $$(".codeblock").forEach(function (block) {
    var b = doc.createElement("button");
    b.type = "button"; b.className = "copy"; b.textContent = "Copy"; b.setAttribute("aria-label", "Copy code");
    b.addEventListener("click", function () {
      var code = $("pre", block);
      copyText(code ? code.innerText.replace(/\n$/, "") : "", function () {
        b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1400);
      });
    });
    block.appendChild(b);
  });

  /* ---- image zoom ---- */
  var box = null;
  function closeBox() { if (box) { box.remove(); box = null; } }
  function openBox(src, alt) {
    closeBox();
    box = doc.createElement("div"); box.className = "lightbox"; box.setAttribute("role", "dialog");
    var img = doc.createElement("img"); img.src = src; img.alt = alt || "";
    var x = doc.createElement("button"); x.className = "x"; x.type = "button"; x.setAttribute("aria-label", "Close"); x.textContent = "×";
    box.appendChild(img); box.appendChild(x);
    box.addEventListener("click", function (e) {
      if (e.target === img) { box.classList.toggle("full"); } else { closeBox(); }
    });
    doc.body.appendChild(box);
  }
  $$("article img").forEach(function (img) {
    if (img.closest("a")) return;
    img.addEventListener("click", function () { openBox(img.currentSrc || img.src, img.alt); });
  });

  /* ---- scroll spy in the sidebar ---- */
  if ("IntersectionObserver" in window) {
    var links = {};
    $$(".sidebar .toc a").forEach(function (a) { links[a.getAttribute("href")] = a; });
    var heads = $$("article h2[id], article h3[id]").filter(function (h) { return links["#" + h.id]; });
    var activeLink = null;
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = en.isIntersecting && links["#" + en.target.id];
        if (!a) return;
        if (activeLink) activeLink.classList.remove("active");
        a.classList.add("active"); activeLink = a;
      });
    }, { rootMargin: "-12% 0px -75% 0px" });
    heads.forEach(function (h) { spy.observe(h); });

    /* single-file version: the chapter in view is opened in the sidebar */
    var pages = $$("section.page[id]");
    if (pages.length) {
      var chapters = {}, openChapter = null;
      $$(".sidebar li[data-page]").forEach(function (li) { chapters[li.getAttribute("data-page")] = li; });
      var pspy = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var li = en.isIntersecting && chapters[en.target.id];
          if (!li) return;
          if (openChapter) openChapter.classList.remove("open", "current");
          li.classList.add("open", "current"); openChapter = li;
          if (li.scrollIntoView) { var nav = $(".sidebar"); var r = li.getBoundingClientRect(), n = nav.getBoundingClientRect();
            if (r.top < n.top || r.bottom > n.bottom) nav.scrollTop += r.top - n.top - 80; }
        });
      }, { rootMargin: "-10% 0px -80% 0px" });
      pages.forEach(function (p) { pspy.observe(p); });
    }
  }

  /* ---- search ---- */
  var input = $("#q"), out = $("#results");
  var index = window.ULG_INDEX || [];
  var shown = [], sel = -1;
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function words(q) { return q.toLowerCase().split(/[^\p{L}\p{N}_.\-]+/u).filter(function (w) { return w.length > 0; }); }
  function hit(text, ws) {
    var lower = text.toLowerCase(), at = -1;
    for (var i = 0; i < ws.length; i++) { var p = lower.indexOf(ws[i]); if (p >= 0 && (at < 0 || p < at)) at = p; }
    var from = Math.max(0, at - 60), snip = text.substr(from, 170);
    var html = esc(snip);
    ws.forEach(function (w) {
      if (!w) return;
      var re = new RegExp("(" + w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
      html = html.replace(re, "<mark>$1</mark>");
    });
    return (from > 0 ? "…" : "") + html + (from + 170 < text.length ? "…" : "");
  }
  function search(q) {
    var ws = words(q);
    if (!ws.length) return [];
    var res = [];
    for (var i = 0; i < index.length; i++) {
      var r = index[i], title = r[2].toLowerCase(), page = r[1].toLowerCase(), text = r[3].toLowerCase(), score = 0, ok = true;
      for (var j = 0; j < ws.length; j++) {
        var w = ws[j], inT = title.indexOf(w) >= 0, inP = page.indexOf(w) >= 0, n = 0, p = -1;
        while ((p = text.indexOf(w, p + 1)) >= 0 && n < 5) n++;
        if (!inT && !inP && !n) { ok = false; break; }
        score += (inT ? 14 : 0) + (inP ? 3 : 0) + n;
      }
      /* prose before reference before source code */
      if (ok) res.push({ r: r, score: score + (/^(Home|Guide)/.test(r[1]) ? 6 : /^Reference/.test(r[1]) ? 2 : /^Project/.test(r[1]) ? -5 : 0) });
    }
    res.sort(function (a, b) { return b.score - a.score; });
    return res.slice(0, 30).map(function (x) { return x.r; });
  }
  function render(list, q) {
    shown = list; sel = -1;
    if (!q.trim()) { out.hidden = true; out.innerHTML = ""; return; }
    var ws = words(q);
    out.innerHTML = list.length ? list.map(function (r, i) {
      var url = (r[0].charAt(0) === "#" ? "" : ROOT) + r[0];
      return '<a href="' + esc(url) + '" data-i="' + i + '"><span class="r-page">' + esc(r[1]) + '</span><span class="r-title">' +
        esc(r[2]) + '</span>' + (r[3] ? '<span class="r-text">' + hit(r[3], ws) + "</span>" : "") + "</a>";
    }).join("") : '<div class="none">Nothing found for “' + esc(q) + "”.</div>";
    out.hidden = false;
  }
  function mark(i) {
    var items = $$("a", out);
    if (!items.length) return;
    sel = (i + items.length) % items.length;
    items.forEach(function (a, k) { a.classList.toggle("sel", k === sel); });
    items[sel].scrollIntoView({ block: "nearest" });
  }
  if (input && out) {
    var timer = null;
    input.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(function () { render(search(input.value), input.value); }, 60);
    });
    input.addEventListener("focus", function () { if (input.value.trim()) render(search(input.value), input.value); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); mark(sel + 1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); mark(sel - 1); }
      else if (e.key === "Enter") {
        var a = $$("a", out)[Math.max(sel, 0)];
        if (a) { a.click(); }
      }
      else if (e.key === "Escape") { out.hidden = true; input.blur(); }
    });
    out.addEventListener("click", function () { out.hidden = true; });
    doc.addEventListener("click", function (e) { if (!e.target.closest(".search")) out.hidden = true; });
    doc.addEventListener("keydown", function (e) {
      var typing = /^(INPUT|TEXTAREA|SELECT)$/.test((e.target.tagName || "")) || e.target.isContentEditable;
      if ((e.key === "/" && !typing) || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k")) {
        e.preventDefault(); input.focus(); input.select();
      } else if (e.key === "Escape") { closeBox(); }
    });
  }
})();
