// Environment configuration
// Set these as window globals via your deployment environment.
// In Vercel, expose them by adding a small inline <script> in each HTML file
// that reads from build-time env vars, or set them manually in dev.
const CONFIG = {
  supabaseUrl: window.SUPABASE_URL || '',
  supabaseAnonKey: window.SUPABASE_ANON_KEY || '',
};

window.MAP_CONFIG = CONFIG;
