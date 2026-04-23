-- ============================================================================
-- Matthew Aucamp Physiotherapy — Supabase Schema
-- Run in the Supabase SQL editor for project: matthew-aucamp-physiotherapy
-- ============================================================================

-- Contact / booking form submissions
CREATE TABLE IF NOT EXISTS contact_submissions (
  id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name            TEXT NOT NULL,
  email           TEXT NOT NULL,
  phone           TEXT,
  condition       TEXT NOT NULL,
  preferred_date  DATE,
  referral_source TEXT,
  message         TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- DigiWorks shared client list
CREATE TABLE IF NOT EXISTS clients (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name          TEXT NOT NULL,
  business_name TEXT,
  email         TEXT,
  phone         TEXT,
  website_url   TEXT,
  industry      TEXT,
  location      TEXT,
  status        TEXT DEFAULT 'active',
  notes         TEXT,
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

-- Insert Matthew Aucamp into the DigiWorks client list
INSERT INTO clients (name, business_name, email, industry, location, website_url, notes)
VALUES (
  'Matthew Aucamp',
  'Matthew Aucamp Physiotherapy',
  'contact@matthewaucampphysio.co.za',
  'Healthcare - Physiotherapy',
  '64 Main Road, Walmer, Gqeberha, Eastern Cape, South Africa',
  'https://matthewaucampphysio.co.za',
  'Solo practitioner. Director since Jan 2026. BSc Physio UFS 2019. Golden Key. DBC Certified Neck & Back. Specialises in MSK and manual therapy. Built by DigiWorks April 2026.'
);

-- Row Level Security
ALTER TABLE contact_submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE clients              ENABLE ROW LEVEL SECURITY;

-- Allow anonymous (public) inserts to contact form
DROP POLICY IF EXISTS "Public can insert contact forms" ON contact_submissions;
CREATE POLICY "Public can insert contact forms"
  ON contact_submissions
  FOR INSERT
  WITH CHECK (true);

-- Index for sorting recent submissions
CREATE INDEX IF NOT EXISTS contact_submissions_created_at_idx
  ON contact_submissions (created_at DESC);
