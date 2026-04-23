"""One-shot generator for the 6 individual service pages.
Run from the site/ directory: python3 build_service_pages.py
This file is gitignored after use; it exists only to template the pages.
"""
import json, os

DOMAIN = "https://matthewaucampphysio.co.za"

PAGES = [
    {
        "slug": "back-pain-treatment-gqeberha",
        "title": "Back Pain Treatment in Gqeberha | Matthew Aucamp Physio",
        "desc": "DBC Certified back pain treatment in Walmer, Gqeberha. Evidence-based rehabilitation for chronic and acute lower back pain in Port Elizabeth.",
        "kw": "back pain treatment Gqeberha, back pain physio Port Elizabeth, lower back pain Walmer, DBC back rehabilitation Eastern Cape",
        "h1": "Back Pain Treatment in Gqeberha — DBC Certified Spinal Rehabilitation",
        "subtitle": "Evidence-based back pain treatment from a DBC Certified physiotherapist in Walmer.",
        "image": "https://images.unsplash.com/photo-1620050382792-434b5828873d?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "Back pain treatment Gqeberha — physiotherapy session at Matthew Aucamp Physiotherapy",
        "breadcrumb": "Back Pain Treatment",
        "service_type": "MedicalTherapy",
        "intro": "Lower back pain is the leading cause of disability worldwide and one of the most common reasons patients walk through my Walmer clinic doors. The good news is that the vast majority of back pain is mechanical — meaning it comes from how the spine is loaded and used, not from a structural problem. With the right rehabilitation, lasting relief is achievable for most patients.",
        "h2_about": "Why Most Back Pain Is Treated Poorly",
        "about_paras": [
            "Most back pain in Gqeberha and Port Elizabeth is treated with painkillers, generic stretches and short-lived manual therapy — none of which address the underlying mechanical drivers. Patients spend months cycling through this approach before realising it's not working. By the time they arrive at my practice, they've often had pain for years and have started believing their spine is fragile.",
            "The honest truth is that mechanical back pain responds extremely well to the right physiotherapy. The key is identifying the actual mechanical drivers — joint stiffness, muscular over-activity, postural overload, weakened deep stabilisers — rather than chasing symptoms with anti-inflammatories and rest.",
        ],
        "h2_approach": "How I Treat Back Pain — The DBC Certified Approach",
        "approach_paras": [
            "I am one of a small number of physiotherapists in the Eastern Cape with the dual DBC (Dynamic Back Care) certifications for both neck and back rehabilitation. DBC is a Finnish-developed, internationally recognised spinal rehabilitation system used in over 30 countries with strong research evidence behind it.",
            "The DBC lumbar protocol combines a thorough clinical assessment, individualised progressive loading, manual therapy, and structured patient education into a programme that runs over 6–12 weeks. Most patients see meaningful improvement within the first 2–3 sessions, with full functional recovery by the end of the programme.",
            "Throughout treatment you'll understand exactly what is happening in your back, what we're doing about it, and how to manage it long term so you don't end up back in the cycle.",
        ],
        "helps": [
            "Chronic or recurring lower back pain",
            "Mechanical back pain from desk-based work",
            "Disc-related back pain (with appropriate clinical screening)",
            "Post-surgical lumbar rehabilitation",
            "Patients who have tried other approaches without success",
        ],
        "expect": [
            "Detailed 60-minute initial assessment",
            "Working diagnosis explained in plain language",
            "Same-session manual therapy where appropriate",
            "Structured 6–12 week DBC programme",
            "Long-term self-management strategy",
        ],
        "closing": "If you're tired of being told your back is degenerating or that you just have to live with it, book an assessment with Matthew at his Walmer practice. Most patients are seen within the same week.",
        "related": [
            ("dbc-spinal-rehabilitation-eastern-cape", "DBC Spinal Rehabilitation"),
            ("manual-therapy-gqeberha", "Manual Therapy"),
        ],
    },
    {
        "slug": "neck-pain-treatment-port-elizabeth",
        "title": "Neck Pain Treatment in Port Elizabeth | DBC Certified Physio",
        "desc": "Chronic neck pain treatment in Port Elizabeth. DBC Certified physiotherapist Matthew Aucamp specialises in cervical spine rehabilitation in Walmer, Gqeberha.",
        "kw": "neck pain treatment Port Elizabeth, cervical physio Gqeberha, DBC neck rehabilitation Eastern Cape, cervicogenic headache physio",
        "h1": "Neck Pain Treatment in Port Elizabeth — Cervical Spine Specialist",
        "subtitle": "DBC Certified neck rehabilitation for chronic and recurrent cervical pain.",
        "image": "https://images.unsplash.com/photo-1740035680800-d5270855c68d?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "Neck pain treatment Port Elizabeth — DBC certified cervical spine physiotherapy",
        "breadcrumb": "Neck Pain Treatment",
        "service_type": "MedicalTherapy",
        "intro": "Chronic neck pain has quietly become one of the most common conditions I see at my Walmer practice. The typical neck pain patient today is in their thirties or forties — often with a desk job, a smartphone, and a steadily worsening problem. The mechanics are reversible, but the standard treatment approach often makes things worse rather than better.",
        "h2_about": "Why Neck Pain Is So Often Misdiagnosed",
        "about_paras": [
            "Patients arrive at my practice every week having been told their neck pain is from a 'pinched nerve', 'muscle spasm', or 'degenerative spine'. Sometimes they've been sent for imaging that showed disc bulges or wear and tear, and have walked out feeling that their spine is broken.",
            "The research is clear: most asymptomatic adults over 30 have disc bulges and degenerative changes on MRI — these findings correlate poorly with pain. Telling a patient their neck is 'degenerating' usually does more harm than good, because the single biggest predictor of chronic pain becoming entrenched is the belief that the body is fragile.",
        ],
        "h2_approach": "DBC Certified Neck Rehabilitation",
        "approach_paras": [
            "I hold a DBC Certified Neck Expert credential — a specialist qualification held by very few physiotherapists in the Eastern Cape. DBC (Dynamic Back Care) is an internationally recognised cervical rehabilitation protocol with strong research evidence.",
            "The DBC cervical programme combines detailed assessment with outcome measures, manual therapy (joint mobilisation and soft-tissue work), progressive resistance training of the deep neck stabilisers, and patient education on long-term self-management. Most patients see clear improvement within 2–4 sessions.",
            "Postural correction is part of the picture, but not in the rigid 'sit up straight' sense. The healthiest position is the next one — variability, frequent movement and specific exercises matter more than holding any single posture all day.",
        ],
        "helps": [
            "Chronic or recurring neck pain (over 3 months)",
            "Cervicogenic headaches",
            "Postural neck pain from desk-based work",
            "Whiplash and post-traumatic cervical pain",
            "Patients unresponsive to other treatments",
        ],
        "expect": [
            "Detailed cervical assessment with outcome measures",
            "Manual therapy and joint mobilisation",
            "Structured 6–12 week DBC protocol",
            "Progressive resistance training",
            "Education on long-term self-management",
        ],
        "closing": "If chronic neck pain is affecting your work, sleep or daily life, book a DBC certified assessment with Matthew at his Walmer practice. Most patients see meaningful improvement within the first few sessions.",
        "related": [
            ("dbc-spinal-rehabilitation-eastern-cape", "DBC Spinal Rehabilitation"),
            ("manual-therapy-gqeberha", "Manual Therapy"),
        ],
    },
    {
        "slug": "sports-injury-rehabilitation-gqeberha",
        "title": "Sports Injury Rehabilitation Gqeberha | Return-to-Play Physio",
        "desc": "Sports injury rehabilitation in Gqeberha. Structured return-to-play programmes from a physiotherapist with 5+ years across leading Port Elizabeth practices.",
        "kw": "sports injury physio Gqeberha, sports rehabilitation Port Elizabeth, return to play programme Eastern Cape, hamstring physio Gqeberha",
        "h1": "Sports Injury Rehabilitation in Gqeberha — Return-to-Play Specialist",
        "subtitle": "Structured rehabilitation that gets you back to performance — not just to pain-free.",
        "image": "https://images.unsplash.com/photo-1649751361457-01d3a696c7e6?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "Sports injury rehabilitation Gqeberha — physiotherapist guiding athlete recovery",
        "breadcrumb": "Sports Injury Rehabilitation",
        "service_type": "PhysicalTherapy",
        "intro": "Sports injuries are one of the most common reasons active people in Gqeberha and Port Elizabeth come through my clinic. Whether you play club rugby, social cricket, surf the Wild Side, run the Hobie Beach front, or hit the gym a few times a week — eventually something will tweak. The question isn't whether you'll get injured; it's how well you handle it when it happens.",
        "h2_about": "Why Early Physiotherapy Matters",
        "about_paras": [
            "The first 72 hours after an injury are when the most important early decisions get made — and unfortunately they're often the worst-managed. Patients ice excessively, immobilise things that should be gently moved, or push through pain that's telling them to stop. Each of these decisions extends recovery dramatically.",
            "Getting assessed within the first week of an injury achieves three things: an accurate diagnosis, optimal early loading, and a clear timeline for recovery. The longer an injury goes without proper assessment, the more likely you are to develop compensatory movement patterns and a sensitised nervous system.",
        ],
        "h2_approach": "Structured Return-to-Play Programmes",
        "approach_paras": [
            "Every well-built sports rehabilitation programme moves through five distinct phases: acute management, mobility restoration, strength and tissue capacity, sport-specific conditioning, and return-to-play assessment. Skipping any phase is the single most common reason athletes re-injure themselves.",
            "I work with patients across the full spectrum of musculoskeletal sports injury — ankle sprains, knee injuries, hamstring strains, shoulder impingement, and lower back pain. Each programme is built around your specific sport and goals, with clear criteria you have to pass before progressing to the next phase.",
            "Returning to play happens only after a formal assessment of strength, range of motion, sport-specific function and confidence — measured against the uninjured side. The pressure to return early is the biggest threat to long-term recovery.",
        ],
        "helps": [
            "Ankle sprains and ligament injuries",
            "Knee injuries — meniscus, ligament, patellofemoral",
            "Hamstring and groin strains",
            "Shoulder injuries — rotator cuff, impingement",
            "Lower back injuries from rugby, cricket and gym",
        ],
        "expect": [
            "Phase-based 5-stage rehabilitation programme",
            "Clear return-to-activity criteria",
            "Progressive strength and conditioning",
            "Sport-specific functional testing",
            "Return-to-play clearance assessment",
        ],
        "closing": "Recovering from a sports injury in Gqeberha or Port Elizabeth? Book a structured rehabilitation assessment with Matthew today and get back to performance properly.",
        "related": [
            ("manual-therapy-gqeberha", "Manual Therapy"),
            ("post-operative-physiotherapy-walmer", "Post-Operative Physiotherapy"),
        ],
    },
    {
        "slug": "manual-therapy-gqeberha",
        "title": "Manual Therapy in Gqeberha | Hands-On Physiotherapy Walmer",
        "desc": "Hands-on manual therapy in Walmer, Gqeberha. Joint mobilisation, soft tissue release and myofascial work from DBC Certified physiotherapist Matthew Aucamp.",
        "kw": "manual therapy Gqeberha, hands-on physio Walmer, joint mobilisation Port Elizabeth, myofascial release Eastern Cape",
        "h1": "Manual Therapy in Gqeberha — Hands-On Physiotherapy",
        "subtitle": "Evidence-based manual therapy from a DBC Certified physiotherapist in Walmer.",
        "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "Manual therapy session in Walmer, Gqeberha — joint mobilisation and soft tissue work",
        "breadcrumb": "Manual Therapy",
        "service_type": "PhysicalTherapy",
        "intro": "Manual therapy is the hands-on side of physiotherapy — and it remains one of the most effective tools we have for restoring movement and reducing pain. Joint mobilisations, soft-tissue release, myofascial work and trigger-point techniques can produce immediate, measurable improvements in pain and range of motion.",
        "h2_about": "Manual Therapy Is Not Just Massage",
        "about_paras": [
            "Massage is one component of soft-tissue work, and soft-tissue work is one component of manual therapy. But manual therapy is much broader — it is a clinical, hands-on approach to assessing and treating the muscles, joints, ligaments and connective tissues of the body, informed by detailed anatomical knowledge and current research.",
            "A massage therapist works with relaxation and general muscle tension. A physiotherapist using manual therapy works with specific clinical findings — a stiff joint, an irritable muscle, a movement restriction, a sensitised nerve — and applies techniques targeted at those specific issues.",
        ],
        "h2_approach": "Evidence-Based Techniques Only",
        "approach_paras": [
            "Every manual therapy technique I use has clinical research behind it. If a technique is no longer supported by current evidence, I don't use it — regardless of how popular it might be elsewhere.",
            "Joint mobilisation and manipulation, soft tissue release, myofascial release and trigger-point work all play a role depending on what the assessment reveals. Manual therapy is paired with progressive exercise and patient education for lasting results — used on its own, the relief lasts a few days at best.",
            "The techniques themselves should never be painful. You may feel firm pressure, a stretch, or a release sensation, but the treatment is always within your comfort tolerance.",
        ],
        "helps": [
            "Acute joint stiffness and limited range of motion",
            "Chronic muscle tension and trigger points",
            "Spinal pain and postural dysfunction",
            "Soft-tissue tightness following injury",
            "Headaches with cervical (neck) origin",
        ],
        "expect": [
            "Hands-on assessment to identify dysfunction",
            "Joint mobilisation and soft-tissue work",
            "Immediate post-treatment re-assessment",
            "Home exercises to maintain the gains",
            "Clear explanation of every technique used",
        ],
        "closing": "Curious about manual therapy? Book a session with Matthew at his Walmer practice and find out exactly what your body needs.",
        "related": [
            ("back-pain-treatment-gqeberha", "Back Pain Treatment"),
            ("neck-pain-treatment-port-elizabeth", "Neck Pain Treatment"),
        ],
    },
    {
        "slug": "post-operative-physiotherapy-walmer",
        "title": "Post-Operative Physiotherapy Walmer Gqeberha | Recovery Specialist",
        "desc": "Post-operative physiotherapy and orthopaedic rehabilitation in Walmer, Gqeberha. Knee, shoulder, hip and spinal surgery recovery programmes.",
        "kw": "post-operative physio Walmer, orthopaedic rehab Gqeberha, knee replacement physio Port Elizabeth, post-surgery physiotherapy Eastern Cape",
        "h1": "Post-Operative Physiotherapy in Walmer, Gqeberha",
        "subtitle": "Structured orthopaedic rehabilitation that protects your surgical outcome.",
        "image": "https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "Post-operative physiotherapy in Walmer, Gqeberha — orthopaedic rehabilitation",
        "breadcrumb": "Post-Operative Physiotherapy",
        "service_type": "MedicalTherapy",
        "intro": "What you do in the weeks and months after orthopaedic surgery often matters more than the surgery itself. A poorly rehabilitated knee replacement, shoulder repair or spinal fusion can leave you with worse function than before the operation. Done properly, post-surgical rehabilitation gets you back to full strength, mobility and confidence.",
        "h2_about": "Why Structured Rehabilitation Matters",
        "about_paras": [
            "Surgeons fix the structural problem. Physiotherapists rebuild the function around it. Both are essential — and skipping the rehabilitation phase is one of the most common reasons people end up disappointed with surgical outcomes that should have been excellent.",
            "I work closely with your surgeon's protocols, respecting their timelines while delivering the hands-on treatment, exercise progression and education needed for a smooth recovery. Every programme is individualised to the procedure, your starting point, and your functional goals.",
        ],
        "h2_approach": "Phase-Based Recovery Programmes",
        "approach_paras": [
            "Post-operative recovery moves through clearly defined phases — acute protection, early mobility, progressive loading, functional restoration, and return to full activity. Each phase has criteria you need to pass before moving on.",
            "The early phase focuses on swelling control, gentle range of motion, and protecting the surgical site. As tissues heal, we progress through manual therapy, scar management, strength building, and finally sport- or work-specific re-training.",
            "Whether you're recovering from a routine arthroscopy or a major joint replacement, structured physiotherapy is the single biggest predictor of long-term outcome.",
        ],
        "helps": [
            "Knee surgery — ACL, meniscus, joint replacement",
            "Shoulder surgery — rotator cuff, labral repair",
            "Hip replacements and resurfacing",
            "Spinal surgery — discectomy, fusion, decompression",
            "Ankle, foot and hand orthopaedic procedures",
        ],
        "expect": [
            "Coordination with your surgeon's protocol",
            "Phase-based recovery plan",
            "Manual therapy and scar management",
            "Progressive strengthening programme",
            "Return-to-activity guidance",
        ],
        "closing": "Recovering from orthopaedic surgery in Gqeberha? Book a post-operative assessment with Matthew at his Walmer practice and protect your surgical outcome.",
        "related": [
            ("sports-injury-rehabilitation-gqeberha", "Sports Injury Rehabilitation"),
            ("manual-therapy-gqeberha", "Manual Therapy"),
        ],
    },
    {
        "slug": "dbc-spinal-rehabilitation-eastern-cape",
        "title": "DBC Spinal Rehabilitation Eastern Cape | Neck & Back Specialist",
        "desc": "DBC Certified spinal rehabilitation for chronic neck and back pain in the Eastern Cape. Internationally recognised protocol delivered in Walmer, Gqeberha.",
        "kw": "DBC spinal rehabilitation Eastern Cape, DBC certified physio Gqeberha, dynamic back care Port Elizabeth, certified spinal physio Walmer",
        "h1": "DBC Spinal Rehabilitation in the Eastern Cape — Dual Certified",
        "subtitle": "Internationally recognised neck and back rehabilitation from a dual-certified specialist.",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1400&q=80&auto=format&fit=crop",
        "image_alt": "DBC spinal rehabilitation Eastern Cape — Dynamic Back Care certified physiotherapy",
        "breadcrumb": "DBC Spinal Rehabilitation",
        "service_type": "MedicalTherapy",
        "intro": "DBC stands for Dynamic Back Care — a Finnish-developed, internationally recognised spinal rehabilitation system used by leading physiotherapy practices in over 30 countries. It is one of the most rigorously researched approaches to chronic neck and back pain available today, and I am one of a small number of physiotherapists in the Eastern Cape with the dual certification for both protocols.",
        "h2_about": "What DBC Certification Actually Means",
        "about_paras": [
            "DBC certification is not a weekend course. It involves an intensive postgraduate training programme, supervised clinical hours, and a formal competency assessment. The dual certification — for both cervical (neck) and lumbar (back) protocols — is held by very few practitioners across South Africa, and even fewer in the Eastern Cape.",
            "For patients, this means you are receiving care grounded in current scientific evidence, delivered by a practitioner who has demonstrated advanced clinical competency in exactly the conditions you're dealing with. It is not a quick fix — it is the gold standard of spinal physiotherapy.",
        ],
        "h2_approach": "How a DBC Programme Works",
        "approach_paras": [
            "A DBC programme runs over 6 to 12 weeks and combines four key elements: a detailed clinical assessment with objective outcome measures, hands-on manual therapy, individualised progressive resistance training to rebuild spinal load tolerance, and structured patient education on long-term self-management.",
            "The protocol is the same one used in the leading spinal rehabilitation centres in Europe. It is hard work and it requires consistent attendance — but the outcomes for patients who commit to it are consistently excellent, including for those who have struggled with chronic pain for years.",
            "Both the cervical (neck) and lumbar (back) protocols are available at the Walmer practice. Patients can be assessed for either or both, depending on their condition.",
        ],
        "helps": [
            "Chronic or recurrent low back pain",
            "Chronic neck pain and cervicogenic headaches",
            "Disc-related spinal conditions",
            "Post-surgical spinal rehabilitation",
            "Patients seeking an alternative to surgery",
        ],
        "expect": [
            "Comprehensive spinal assessment",
            "Objective outcome measures and re-testing",
            "6–12 week structured DBC programme",
            "Progressive loading and strengthening",
            "Long-term self-management strategy",
        ],
        "closing": "If you've been told you'll just have to live with chronic neck or back pain, the DBC protocol is worth a serious look. Book a DBC assessment with Matthew today.",
        "related": [
            ("back-pain-treatment-gqeberha", "Back Pain Treatment"),
            ("neck-pain-treatment-port-elizabeth", "Neck Pain Treatment"),
        ],
    },
]

NAV = '''<nav class="nav nav--solid" aria-label="Primary">
  <div class="nav__inner">
    <a href="/" class="nav__logo"><img src="/images/logos/matthew-aucamp-logo_Matt Logo White.svg" alt="Matthew Aucamp Physiotherapy" class="nav__logo-img nav__logo-img--white"><img src="/images/logos/matthew-aucamp-logo_Matt Logo Black.svg" alt="Matthew Aucamp Physiotherapy" class="nav__logo-img nav__logo-img--black">Matthew Aucamp<span>Physiotherapy</span></a>
    <button class="nav__hamburger" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <div class="nav__links">
      <a href="/" class="nav__link">Home</a>
      <a href="/about" class="nav__link">About</a>
      <a href="/services" class="nav__link">Services</a>
      <a href="/blog" class="nav__link">Blog</a>
      <a href="/faq" class="nav__link">FAQ</a>
      <a href="/contact" class="nav__link">Contact</a>
      <a href="/contact" class="nav__cta">Book Appointment</a>
    </div>
  </div>
</nav>'''

FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__col">
        <a href="/" class="footer__logo">Matthew Aucamp Physiotherapy</a>
        <p class="footer__tagline">Expert Physiotherapy in Gqeberha — DBC Certified neck &amp; back specialist serving Walmer, Port Elizabeth and the Eastern Cape.</p>
        <a href="https://www.linkedin.com/in/matthew-aucamp-916639207/" class="footer__social" aria-label="LinkedIn" target="_blank" rel="noopener"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 1 1 8.3 6.5a1.78 1.78 0 0 1-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0 0 13 14.19V19h-3v-9h2.9v1.3a3.11 3.11 0 0 1 2.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg></a><a href="https://www.instagram.com/matthew_aucamp_physiotherapy" class="footer__social" aria-label="Instagram" target="_blank" rel="noopener" style="margin-left:8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li><li><a href="/services">Services</a></li><li><a href="/blog">Blog</a></li><li><a href="/faq">FAQ</a></li><li><a href="/contact">Contact</a></li></ul>
      </div>
      <div class="footer__col">
        <h4>Services</h4>
        <ul><li><a href="/services/back-pain-treatment-gqeberha">Back Pain</a></li><li><a href="/services/neck-pain-treatment-port-elizabeth">Neck Pain</a></li><li><a href="/services/sports-injury-rehabilitation-gqeberha">Sports Injury</a></li><li><a href="/services/manual-therapy-gqeberha">Manual Therapy</a></li><li><a href="/services/dbc-spinal-rehabilitation-eastern-cape">DBC Spinal</a></li><li><a href="/services/post-operative-physiotherapy-walmer">Post-Op Recovery</a></li></ul>
      </div>
      <div class="footer__col">
        <h4>Contact</h4>
        <address class="footer__contact">64 Main Road<br>Walmer, Gqeberha<br>Eastern Cape, 6065<br><br><a href="mailto:contact@matthewaucampphysio.co.za">contact@matthewaucampphysio.co.za</a><br>+27 83 293 3445<br><br>Mon–Fri 08:00–17:00<br>Sat 08:00–12:00</address>
      </div>
    </div>
  </div>
  <div class="footer__bottom"><div class="container">© 2026 Matthew Aucamp Physiotherapy &nbsp;|&nbsp; HPCSA Registered &nbsp;|&nbsp; Built by <a href="https://digiiworks.co" target="_blank" rel="noopener" class="footer__digiiworks"><img src="/images/logos/digiiworks-logo-allwhite.svg" alt="Digiiworks" class="footer__digiiworks-logo footer__digiiworks-logo--white"><img src="/images/logos/digiiworks-logo-white.svg" alt="Digiiworks" class="footer__digiiworks-logo footer__digiiworks-logo--gradient"></a></div></div>
</footer>'''

def render(p):
    canonical = f"{DOMAIN}/services/{p['slug']}"
    breadcrumb_schema = {
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":f"{DOMAIN}/"},
            {"@type":"ListItem","position":2,"name":"Services","item":f"{DOMAIN}/services"},
            {"@type":"ListItem","position":3,"name":p["breadcrumb"],"item":canonical},
        ]
    }
    service_schema = {
        "@context":"https://schema.org",
        "@type":"MedicalProcedure",
        "name":p["breadcrumb"],
        "url":canonical,
        "description":p["desc"],
        "procedureType":p["service_type"],
        "performer":{"@type":"MedicalBusiness","@id":f"{DOMAIN}/#business","name":"Matthew Aucamp Physiotherapy","url":DOMAIN,"address":{"@type":"PostalAddress","streetAddress":"64 Main Road","addressLocality":"Walmer","addressRegion":"Eastern Cape","postalCode":"6065","addressCountry":"ZA"}},
        "bodyLocation":"Musculoskeletal system"
    }

    helps_html = "\n".join(f"      <li>{h}</li>" for h in p["helps"])
    expect_html = "\n".join(f"      <li>{e}</li>" for e in p["expect"])
    about_paras = "\n".join(f"    <p>{para}</p>" for para in p["about_paras"])
    approach_paras = "\n".join(f"    <p>{para}</p>" for para in p["approach_paras"])
    related_html = "\n".join(
        f'      <li><a href="/services/{slug}">{name} →</a></li>'
        for slug, name in p["related"]
    )

    return f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<meta name="keywords" content="{p["kw"]}">
<meta name="author" content="Matthew Aucamp Physiotherapy">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://matthew-aucamp-physiotherapy.vercel.app/assets/images/og-image.jpg">
<meta property="og:image:secure_url" content="https://matthew-aucamp-physiotherapy.vercel.app/assets/images/og-image.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Matthew Aucamp Physiotherapy — DBC Certified Physiotherapist in Gqeberha">
<meta property="og:locale" content="en_ZA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p["title"]}">
<meta name="twitter:description" content="{p["desc"]}">
<meta name="twitter:image" content="https://matthew-aucamp-physiotherapy.vercel.app/assets/images/og-image.jpg">
<link rel="alternate" hreflang="en-ZA" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<link rel="canonical" href="{canonical}">

<link rel="preconnect" href="https://images.unsplash.com">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/inter-400-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/montserrat-800-latin.woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/css/styles.css?v=20260423b">

<script type="application/ld+json">
{json.dumps(service_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(breadcrumb_schema, indent=2)}
</script>
</head>
<body>

{NAV}

<header class="page-hero page-hero--sm">
  <div>
    <div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services">Services</a><span>/</span>{p["breadcrumb"]}</div>
    <h1>{p["h1"]}</h1>
    <p class="page-hero__subtitle">{p["subtitle"]}</p>
  </div>
</header>

<section class="section">
  <div class="container container--narrow">
    <p class="lead" style="font-size:1.125rem; margin-bottom:2.5rem;">{p["intro"]}</p>

    <img src="{p["image"]}" alt="{p["image_alt"]}" loading="eager" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:var(--radius-lg); box-shadow:var(--shadow-md); margin-bottom:3rem;">

    <h2 style="margin-bottom:1.5rem;">{p["h2_about"]}</h2>
{about_paras}

    <h2 style="margin-top:3rem; margin-bottom:1.5rem;">{p["h2_approach"]}</h2>
{approach_paras}

    <h2 style="margin-top:3rem; margin-bottom:1rem;">Who This Helps</h2>
    <ul style="margin-bottom:2rem; padding-left:1.5rem;">
{helps_html}
    </ul>

    <h2 style="margin-top:2rem; margin-bottom:1rem;">What to Expect</h2>
    <ul style="margin-bottom:2rem; padding-left:1.5rem;">
{expect_html}
    </ul>

    <p style="margin-top:2rem;">{p["closing"]}</p>

    <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid var(--border);">
      <h3 style="font-size:1rem; margin-bottom:1rem;">Related Services</h3>
      <ul style="padding-left:1.5rem;">
{related_html}
      </ul>
    </div>
  </div>
</section>

<section class="cta-banner">
  <div class="container">
    <h2>Book Your Appointment</h2>
    <p>New patients welcome at the Walmer practice. Most appointments scheduled within the same week.</p>
    <a href="/contact" class="btn btn--primary btn--lg">Book an Appointment</a>
    <span class="cta-banner__email">Or email <a href="mailto:contact@matthewaucampphysio.co.za">contact@matthewaucampphysio.co.za</a></span>
  </div>
</section>

{FOOTER}

<script src="/js/nav.js" defer></script>
<script src="/js/animations.js" defer></script>
</body>
</html>
'''

# Article style for service pages: lists need bullet styling
# (already covered by .article ul styles in styles.css if I wrap in .article — but I'm not. Let me add list-style.)

for p in PAGES:
    out = f"services/{p['slug']}.html"
    with open(out, 'w') as f:
        f.write(render(p))
    print(f"  ✓ {out}")
print(f"\n✓ Generated {len(PAGES)} service pages")
