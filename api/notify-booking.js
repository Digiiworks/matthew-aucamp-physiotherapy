// Vercel Function: notify-booking
// Triggered by a Supabase Database Webhook on INSERT into contact_submissions.
// Sends a styled HTML notification email to hello@digiiworks.co (test recipient).
// When SiteGround mailbox is provisioned later, swap NOTIFY_TO + SMTP env vars.

import nodemailer from 'nodemailer';

const escapeHtml = (s = '') =>
  String(s).replace(/[&<>"']/g, (c) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  }[c]));

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Shared-secret check (sent by Supabase webhook in custom header)
  const incomingSecret = req.headers['x-webhook-secret'];
  if (!process.env.WEBHOOK_SECRET || incomingSecret !== process.env.WEBHOOK_SECRET) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  // Supabase webhook payload format: { type, table, record, schema, old_record }
  const payload = req.body || {};
  const row = payload.record || payload;

  if (!row || !row.email || !row.name) {
    return res.status(400).json({ error: 'Invalid payload — missing required fields' });
  }

  const {
    name,
    email,
    phone,
    condition,
    preferred_date,
    referral_source,
    message,
    created_at,
  } = row;

  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: Number(process.env.SMTP_PORT) || 465,
    secure: Number(process.env.SMTP_PORT) === 465,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });

  const html = `<!doctype html>
<html>
<body style="margin:0;padding:0;background:#f4f7fb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#1e293b;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f7fb;padding:32px 16px;">
    <tr><td align="center">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(11,79,138,0.08);">
        <tr><td style="background:linear-gradient(135deg,#083966 0%,#0B4F8A 50%,#1E8A52 100%);padding:32px 32px 28px;color:#ffffff;">
          <div style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;opacity:0.85;margin-bottom:8px;">New Booking Request</div>
          <div style="font-size:22px;font-weight:800;line-height:1.25;">Matthew Aucamp Physiotherapy</div>
          <div style="font-size:13px;opacity:0.85;margin-top:6px;">A new appointment request has just been submitted via the website.</div>
        </td></tr>
        <tr><td style="padding:32px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-size:14px;line-height:1.6;">
            <tr><td style="padding:8px 0;color:#64748B;width:140px;font-weight:600;">Name</td><td style="padding:8px 0;color:#1e293b;">${escapeHtml(name)}</td></tr>
            <tr><td style="padding:8px 0;color:#64748B;font-weight:600;">Email</td><td style="padding:8px 0;"><a href="mailto:${escapeHtml(email)}" style="color:#0B4F8A;text-decoration:none;">${escapeHtml(email)}</a></td></tr>
            ${phone ? `<tr><td style="padding:8px 0;color:#64748B;font-weight:600;">Phone</td><td style="padding:8px 0;"><a href="tel:${escapeHtml(phone)}" style="color:#0B4F8A;text-decoration:none;">${escapeHtml(phone)}</a></td></tr>` : ''}
            ${preferred_date ? `<tr><td style="padding:8px 0;color:#64748B;font-weight:600;">Preferred Date</td><td style="padding:8px 0;color:#1e293b;">${escapeHtml(preferred_date)}</td></tr>` : ''}
            ${referral_source ? `<tr><td style="padding:8px 0;color:#64748B;font-weight:600;">Heard via</td><td style="padding:8px 0;color:#1e293b;">${escapeHtml(referral_source)}</td></tr>` : ''}
          </table>
          <div style="margin-top:24px;padding:20px;background:#F0F7FF;border-left:4px solid #2EAD6C;border-radius:6px;">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#1E8A52;margin-bottom:8px;">Condition / Reason for visit</div>
            <div style="font-size:14px;color:#1e293b;line-height:1.6;">${escapeHtml(condition || '')}</div>
          </div>
          ${message ? `<div style="margin-top:16px;padding:20px;background:#F4F7FB;border-radius:6px;"><div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#64748B;margin-bottom:8px;">Additional Message</div><div style="font-size:14px;color:#1e293b;line-height:1.6;">${escapeHtml(message)}</div></div>` : ''}
          <div style="margin-top:32px;padding-top:20px;border-top:1px solid #E2EAF4;font-size:12px;color:#64748B;">Submitted ${escapeHtml(created_at || new Date().toISOString())}</div>
        </td></tr>
        <tr><td style="background:#0D1B2A;padding:20px 32px;color:#ffffff;font-size:11px;text-align:center;letter-spacing:0.04em;">
          Matthew Aucamp Physiotherapy &nbsp;|&nbsp; 64 Main Road, Walmer, Gqeberha &nbsp;|&nbsp; +27 83 293 3445
        </td></tr>
      </table>
      <div style="font-size:11px;color:#94a3b8;margin-top:16px;">This is a TEST notification. Production email will be routed via SiteGround.</div>
    </td></tr>
  </table>
</body>
</html>`;

  try {
    await transporter.sendMail({
      from: `"Matthew Aucamp Physiotherapy" <${process.env.SMTP_USER}>`,
      to: process.env.NOTIFY_TO || 'hello@digiiworks.co',
      replyTo: email,
      subject: `New booking request — ${name}`,
      html,
      text:
        `New booking request — Matthew Aucamp Physiotherapy\n\n` +
        `Name: ${name}\nEmail: ${email}\n` +
        (phone ? `Phone: ${phone}\n` : '') +
        (preferred_date ? `Preferred date: ${preferred_date}\n` : '') +
        (referral_source ? `Heard via: ${referral_source}\n` : '') +
        `\nCondition: ${condition || ''}\n` +
        (message ? `\nMessage: ${message}\n` : '') +
        `\nSubmitted: ${created_at || new Date().toISOString()}`,
    });
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('[notify-booking] sendMail failed:', err);
    return res.status(500).json({ error: 'Failed to send notification', detail: String(err.message || err) });
  }
}
