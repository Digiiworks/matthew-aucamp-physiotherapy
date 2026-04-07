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
