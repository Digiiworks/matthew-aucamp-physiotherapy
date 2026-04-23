# Matthew Aucamp Physiotherapy

Official website for **Matthew Aucamp Physiotherapy** — DBC Certified physiotherapist in Walmer, Gqeberha, Eastern Cape, South Africa.

Specialising in musculoskeletal conditions, manual therapy, injury rehabilitation, and DBC Certified neck & back rehabilitation.

- **Practice**: 64 Main Road, Walmer, Gqeberha, Eastern Cape, 6065
- **Email**: contact@matthewaucampphysio.co.za
- **Director**: Matthew Aucamp — BSc Physiotherapy (UFS), DBC Certified Neck & Back Expert

---

## Tech Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (no frameworks)
- **Database**: Supabase (contact form submissions)
- **Hosting**: Vercel
- **Fonts**: Google Fonts (Montserrat + Inter)
- **Images**: Unsplash (royalty-free)

No build step. Pure static files.

---

## Local Development

1. Install [VS Code](https://code.visualstudio.com/)
2. Install the **Live Server** extension by Ritwick Dey (`ritwickdey.LiveServer`)
3. Clone this repo and open the folder in VS Code
4. Right-click `index.html` → **Open with Live Server**
5. Preview runs at <http://localhost:5500>
6. No build step required — vanilla HTML/CSS/JS edits hot-reload automatically

### Supabase form testing locally

For the contact form to submit while developing locally:

1. Open your Supabase project dashboard
2. Go to **Authentication → URL Configuration → Allowed URLs**
3. Add `http://localhost:5500`
4. Copy `.env.example` to `.env` and fill in your `SUPABASE_URL` and `SUPABASE_ANON_KEY`
5. For local testing only, add a small inline script in `index.html` setting `window.SUPABASE_URL` and `window.SUPABASE_ANON_KEY` (do **not** commit real keys)

---

## Deployment (Vercel)

```bash
vercel          # preview
vercel --prod   # production
```

Set the following environment variables in the Vercel project dashboard (Settings → Environment Variables):

- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`

These are injected as `window.SUPABASE_URL` / `window.SUPABASE_ANON_KEY` via the small inline config in each HTML file.

---

## Supabase Setup

1. Create a new Supabase project named `matthew-aucamp-physiotherapy`
2. Open the **SQL Editor**
3. Paste and run the contents of [`supabase/schema.sql`](supabase/schema.sql)
4. Copy the project URL and anon key into your Vercel env vars

---

## File Structure

```
.
├── index.html              # Homepage
├── about.html              # About Matthew
├── services.html           # Services overview
├── contact.html            # Booking / contact form
├── blog/
│   ├── index.html
│   ├── back-pain-treatment-gqeberha.html
│   ├── neck-pain-physiotherapy-port-elizabeth.html
│   ├── sports-injury-rehabilitation-eastern-cape.html
│   └── manual-therapy-what-to-expect.html
├── css/
│   ├── global.css          # Reset, variables, utilities
│   ├── components.css      # Nav, footer, cards, forms, buttons
│   └── pages.css           # Page-specific layouts
├── js/
│   ├── config.js           # Env config (window globals)
│   ├── supabase-client.js  # Supabase wrapper + form submit
│   ├── nav.js              # Sticky nav + mobile menu
│   ├── animations.js       # Intersection observer fade-ins
│   └── form.js             # Contact form validation + submit
├── assets/
│   └── images/             # OG image and favicons (Unsplash CDN used inline)
├── supabase/
│   └── schema.sql          # Run in Supabase SQL editor
├── robots.txt
├── sitemap.xml
├── vercel.json
├── .env.example
└── README.md
```

---

## License

MIT — see [LICENSE](LICENSE).

---

Built by [DigiWorks](https://digiiworks.co) — April 2026.
