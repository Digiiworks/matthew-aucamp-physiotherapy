// Supabase client wrapper
// Requires the Supabase UMD bundle loaded via CDN in HTML before this script:
//   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>

(function () {
  let client = null;

  function getClient() {
    if (client) return client;
    if (!window.supabase || typeof window.supabase.createClient !== 'function') {
      console.warn('[supabase] CDN bundle not loaded.');
      return null;
    }
    const url = window.MAP_CONFIG && window.MAP_CONFIG.supabaseUrl;
    const key = window.MAP_CONFIG && window.MAP_CONFIG.supabaseAnonKey;
    if (!url || !key) {
      console.warn('[supabase] Missing SUPABASE_URL or SUPABASE_ANON_KEY.');
      return null;
    }
    client = window.supabase.createClient(url, key);
    return client;
  }

  async function submitContactForm(formData) {
    const sb = getClient();
    if (!sb) {
      throw new Error('Supabase is not configured. Please contact us at campphysiotherapy@gmail.com.');
    }
    const payload = {
      name: formData.name,
      email: formData.email,
      phone: formData.phone || null,
      condition: formData.condition,
      preferred_date: formData.preferred_date || null,
      referral_source: formData.referral_source || null,
      message: formData.message || null,
    };
    const { data, error } = await sb
      .from('contact_submissions')
      .insert([payload])
      .select();
    if (error) throw error;
    return data;
  }

  // Placeholder for future blog CMS use
  async function getBlogPosts() {
    const sb = getClient();
    if (!sb) return [];
    const { data, error } = await sb
      .from('blog_posts')
      .select('*')
      .order('created_at', { ascending: false });
    if (error) {
      console.warn('[supabase] getBlogPosts:', error.message);
      return [];
    }
    return data || [];
  }

  window.SupabaseAPI = { submitContactForm, getBlogPosts };
})();
