// Contact form validation + Supabase submission
(function () {
  const form = document.querySelector('#booking-form');
  if (!form) return;

  const submitBtn = form.querySelector('button[type="submit"]');
  const errorBanner = form.querySelector('.form__error-banner');

  function setError(name, message) {
    const group = form.querySelector('[data-field="' + name + '"]');
    if (!group) return;
    group.classList.add('error');
    const errEl = group.querySelector('.form__error');
    if (errEl) errEl.textContent = message;
  }
  function clearErrors() {
    form.querySelectorAll('.form__group.error').forEach(function (g) { g.classList.remove('error'); });
    if (errorBanner) errorBanner.classList.remove('visible');
  }
  function validate(data) {
    clearErrors();
    let ok = true;
    if (!data.name || data.name.trim().length < 2) {
      setError('name', 'Please enter your full name'); ok = false;
    }
    if (!data.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
      setError('email', 'Please enter a valid email address'); ok = false;
    }
    if (!data.condition || data.condition.trim().length < 5) {
      setError('condition', 'Please describe your condition or reason for visit'); ok = false;
    }
    if (data.preferred_date) {
      const today = new Date(); today.setHours(0,0,0,0);
      const chosen = new Date(data.preferred_date);
      if (chosen < today) {
        setError('preferred_date', 'Please choose a date in the future'); ok = false;
      }
    }
    return ok;
  }

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const formData = {
      name: form.name.value,
      email: form.email.value,
      phone: form.phone.value,
      condition: form.condition.value,
      preferred_date: form.preferred_date.value,
      referral_source: form.referral_source.value,
      message: form.message.value,
    };
    if (!validate(formData)) return;

    submitBtn.classList.add('loading');
    submitBtn.disabled = true;

    try {
      await window.SupabaseAPI.submitContactForm(formData);
      // Replace form with success state
      form.innerHTML =
        '<div class="form__success">' +
        '<h3>Thank you, ' + escapeHtml(formData.name) + '!</h3>' +
        '<p>Your appointment request has been received. Matthew will be in touch within 24 hours at <strong>' + escapeHtml(formData.email) + '</strong>.</p>' +
        '</div>';
    } catch (err) {
      console.error('[form] submit failed:', err);
      submitBtn.classList.remove('loading');
      submitBtn.disabled = false;
      if (errorBanner) {
        errorBanner.textContent = 'Sorry, something went wrong sending your request. Please try again or email contact@matthewaucampphysio.co.za directly.';
        errorBanner.classList.add('visible');
      }
    }
  });

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }
})();
