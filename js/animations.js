// Intersection Observer fade-in animations
(function () {
  const elements = document.querySelectorAll('.fade-in');
  if (!elements.length || !('IntersectionObserver' in window)) {
    elements.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px',
  });
  elements.forEach(function (el) { observer.observe(el); });
})();

// Hero background parallax
(function () {
  var bg = document.querySelector('.hero__bg');
  var hero = document.querySelector('.hero');
  if (!bg || !hero) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var ticking = false;
  function update() {
    var rect = hero.getBoundingClientRect();
    if (rect.bottom < 0 || rect.top > window.innerHeight) {
      ticking = false;
      return;
    }
    var offset = rect.top * -0.35;
    bg.style.transform = 'translate3d(0,' + offset + 'px,0)';
    ticking = false;
  }
  function onScroll() {
    if (!ticking) {
      window.requestAnimationFrame(update);
      ticking = true;
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();
