// Sticky nav + mobile menu + active link highlighting
(function () {
  const nav = document.querySelector('.nav');
  if (!nav) return;

  const hamburger = nav.querySelector('.nav__hamburger');
  const links = nav.querySelectorAll('.nav__link, .nav__cta');

  // Scroll state
  function onScroll() {
    if (window.scrollY > 80) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Hamburger toggle
  if (hamburger) {
    hamburger.addEventListener('click', function () {
      nav.classList.toggle('open');
      const expanded = nav.classList.contains('open');
      hamburger.setAttribute('aria-expanded', expanded);
      document.body.style.overflow = expanded ? 'hidden' : '';
    });
  }

  // Close menu on link click
  links.forEach(function (link) {
    link.addEventListener('click', function () {
      nav.classList.remove('open');
      if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  // Active link highlight based on current path
  const path = window.location.pathname.replace(/\/$/, '') || '/';
  nav.querySelectorAll('.nav__link').forEach(function (link) {
    const href = link.getAttribute('href') || '';
    const cleanHref = href.replace(/\.html$/, '').replace(/\/$/, '') || '/';
    if (cleanHref === path || (cleanHref !== '/' && path.startsWith(cleanHref))) {
      link.classList.add('active');
    }
  });
})();
