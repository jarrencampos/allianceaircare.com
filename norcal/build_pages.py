import os

PHONE     = "(530) 718-9271"
PHONE_RAW = "+15307189271"
PHONE_TEL = "tel:+15307189271"
SMS_TEL   = "sms:+15307189271"

PHONE_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'
CHECK_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20,6 9,17 4,12"/></svg>'
STAR_SVG  = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
SHIELD_SVG= '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0 1 12 2.944a11.955 11.955 0 0 1-8.618 3.04A12.02 12.02 0 0 0 3 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>'
CLOCK_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
PIN_SVG   = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>'

REVIEWS = [
    ("Vic Marquez", "AC unit was having issues. He diagnosed the problem fast and had it running again the same day. Polite, knowledgeable, really appreciate the honest work Cam! Highly recommend.", "Google Review"),
    ("Samantha Barker", "Very fast response time. Figured out what was wrong and had it fixed the same day. Also a great guy overall. Already recommended him to a friend!", "Google Review"),
    ("Cynthia Gibbs", "Cameron was so friendly, knowledgeable, and professional! We really enjoyed having him work for us. He explained every question we had and love his prices.", "Google Review"),
]

GOOGLE_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>'

WHY_CARDS = [
    ("Fast Response", "Call in the morning, we're there that day. No booking out weeks in advance.", CLOCK_SVG),
    ("Upfront Pricing",  "You get the full quote before we start. No surprises on the invoice.", SHIELD_SVG),
    ("Stocked Trucks",   "Most repairs happen in one visit — we carry the parts NorCal homes need.", PHONE_SVG),
    ("Local & Licensed", "Fully licensed and insured. We live and work in the Sacramento Valley.", PIN_SVG),
]

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --navy:   #111827;
  --blue:   #1d4ed8;
  --blue-d: #1e40af;
  --light:  #f9fafb;
  --text:   #1f2937;
  --muted:  #6b7280;
  --border: #e5e7eb;
  --white:  #ffffff;
  --green:  #166534;
  --radius: 8px;
}
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  color: var(--text);
  background: var(--white);
  font-size: 16px;
  line-height: 1.6;
  padding-top: 112px;
  padding-bottom: 64px;
}
a { color: inherit; text-decoration: none; }

/* NAV */
.site-nav { background:#000; position:fixed; top:0; left:0; right:0; z-index:1000; border-bottom:1px solid rgba(255,255,255,.08); }
.nav-inner { max-width:100%; padding:0 24px; display:grid; grid-template-columns:1fr auto 1fr; align-items:center; min-height:112px; }
.nav-stars { display:flex; flex-direction:column; align-items:center; justify-content:center; justify-self:start; }
.nav-stars .stars-row { color:#fff; font-size:1.3rem; letter-spacing:3px; line-height:1; font-weight:900; }
.nav-stars .stars-label { font-size:.78rem; color:#fff; font-weight:700; margin-top:4px; letter-spacing:.04em; }
.nav-logo { display:flex; align-items:center; justify-content:center; }
.nav-logo img { height:80px; width:auto; display:block; }
.nav-cta-wrap { display:flex; align-items:center; justify-content:flex-end; }
.nav-cta { background:var(--blue); color:#fff!important; font-size:.88rem; font-weight:700; padding:10px 20px; border-radius:999px; white-space:nowrap; transition:background .15s; }
.nav-cta:hover { background:var(--blue-d); }
@media(max-width:480px){ .nav-cta { font-size:.78rem; padding:8px 14px; } }
@media(max-width:640px){ body { padding-top: 76px; } .nav-inner { min-height: 76px; padding: 0 14px; } .nav-logo img { height: 54px; } .nav-stars .stars-row { font-size: .95rem; letter-spacing: 2px; } .nav-stars .stars-label { font-size: .62rem; margin-top: 2px; } }

/* HERO */
.hero {
  position: relative;
  background: url('/norcal/images/tech-working.jpg') center center / cover no-repeat;
  min-height: 88vh;
  display: flex;
  align-items: center;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(0,0,0,0.88) 0%, rgba(17,24,39,0.80) 100%);
}
.hero-inner {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 1100px;
  margin: 0 auto;
  padding: 3.5rem 1.5rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}
@media(max-width:780px){
  .hero { min-height: auto; }
  .hero-inner { grid-template-columns: 1fr; gap: 2rem; padding: 2.5rem 1.25rem; }
  .hero-text { text-align: center; }
  .hero-badges { justify-content: center; }
}
.hero-text h1 {
  font-size: clamp(2rem, 4.5vw, 3.2rem);
  font-weight: 900;
  color: var(--white);
  line-height: 1.08;
  margin-bottom: 1rem;
  letter-spacing: -.02em;
}
.hero-text h1 span { color: #60a5fa; }
.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-bottom: 1.25rem;
}
.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.2);
  color: var(--white);
  font-size: .8rem;
  font-weight: 600;
  padding: .3rem .8rem;
  border-radius: 50px;
  backdrop-filter: blur(4px);
}
.badge-pill.hl { background: var(--blue); border-color: var(--blue); }
.hero-sub { color: rgba(255,255,255,.82); font-size: 1rem; line-height: 1.7; margin-bottom: 1.5rem; }
.hero-phone {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  background: var(--blue);
  color: var(--white);
  font-size: 1rem;
  font-weight: 700;
  padding: .9rem 2rem;
  border-radius: 50px;
  transition: background .2s, transform .1s;
}
.hero-phone:hover { background: var(--blue-d); transform: scale(1.02); }

/* FORM CARD */
.form-card {
  background: var(--white);
  border-radius: 14px;
  padding: 2rem 1.75rem;
  box-shadow: 0 20px 60px rgba(0,0,0,.4);
}
.form-card-head { text-align: center; margin-bottom: 1.4rem; }
.free-tag {
  display: inline-block;
  background: #dcfce7;
  color: #166534;
  font-size: .74rem;
  font-weight: 700;
  padding: .22rem .75rem;
  border-radius: 50px;
  margin-bottom: .45rem;
  letter-spacing: .05em;
  text-transform: uppercase;
}
.form-card-head h2 { font-size: 1.2rem; color: var(--navy); font-weight: 700; margin-bottom: .2rem; }
.form-card-head p { font-size: .83rem; color: var(--muted); }
.form-card input,
.form-card select {
  width: 100%;
  padding: .8rem 1rem;
  border: 1.5px solid var(--border);
  border-radius: var(--radius);
  font-size: .92rem;
  font-family: inherit;
  color: var(--text);
  background: var(--white);
  margin-bottom: .7rem;
  transition: border-color .2s;
  appearance: none;
  -webkit-appearance: none;
}
.form-card input:focus,
.form-card select:focus { outline: none; border-color: var(--blue); }
.select-wrap { position: relative; }
.select-wrap::after { content:'▾'; position:absolute; right:1rem; top:50%; transform:translateY(-55%); color:var(--muted); pointer-events:none; }
.btn-submit {
  width: 100%;
  padding: 1rem;
  background: var(--blue);
  color: var(--white);
  border: none;
  border-radius: var(--radius);
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  letter-spacing: .03em;
  transition: background .2s, transform .1s;
  margin-top: .2rem;
}
.btn-submit:hover { background: var(--blue-d); }
.btn-submit:active { transform: scale(.98); }
.form-trust {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: .4rem .9rem;
  margin-top: .8rem;
}
.form-trust span {
  font-size: .72rem;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: .25rem;
}
.form-success {
  display: none;
  text-align: center;
  padding: 1.5rem 0;
  color: var(--blue);
  font-weight: 600;
  font-size: 1rem;
}

/* TRUST BAR */
.trust-bar {
  background: var(--light);
  border-top: 3px solid var(--blue);
  padding: 1.4rem 1.25rem;
}
.trust-bar-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: .8rem 2.5rem;
}
.trust-item {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .88rem;
  font-weight: 600;
  color: var(--navy);
}
.trust-item svg { color: var(--blue); flex-shrink: 0; }

/* COST CALLOUT */
.cost-callout {
  background: var(--navy);
  padding: 3.5rem 1.25rem;
  text-align: center;
}
.cost-callout-inner { max-width: 960px; margin: 0 auto; }
.cost-callout h2 {
  font-size: clamp(1.6rem, 3.5vw, 2.4rem);
  font-weight: 900;
  color: var(--white);
  letter-spacing: -.02em;
  margin-bottom: 1.5rem;
  line-height: 1.15;
}
.cost-callout h2 span { color: #60a5fa; }
.cost-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}
.cost-card {
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 10px;
  padding: 1.5rem 1rem;
}
.cost-card .cost-amount {
  font-size: 2rem;
  font-weight: 900;
  color: #60a5fa;
  display: block;
  margin-bottom: .25rem;
  line-height: 1;
}
.cost-card p { color: rgba(255,255,255,.75); font-size: .83rem; line-height: 1.5; margin-top: .4rem; }
.cost-note { color: rgba(255,255,255,.45); font-size: .82rem; margin-top: 1.5rem; }

/* SECTIONS */
.section { padding: 4rem 1.25rem; }
.section.alt { background: var(--light); }
.section-inner { max-width: 1100px; margin: 0 auto; }
.section-title {
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  font-weight: 900;
  color: var(--navy);
  letter-spacing: -.02em;
  margin-bottom: .4rem;
  line-height: 1.15;
}
.section-title span { color: var(--blue); }
.section-sub { color: var(--muted); margin-bottom: 2.25rem; font-size: .93rem; }

/* CHECKLIST */
.checklist-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: .75rem;
}
.check-item {
  display: flex;
  align-items: flex-start;
  gap: .7rem;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem 1.2rem;
}
.section.alt .check-item { background: var(--white); }
.check-icon {
  width: 22px; height: 22px;
  background: var(--blue);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  margin-top: 2px;
}
.check-icon svg { color: var(--white); }
.check-item span { font-size: .88rem; color: var(--text); font-weight: 500; line-height: 1.5; }

/* WHY GRID */
.why-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
}
.why-card {
  background: var(--white);
  border-radius: 10px;
  padding: 1.6rem 1.4rem;
  border: 1.5px solid var(--border);
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
}
.why-card h3 { font-size: .97rem; font-weight: 700; color: var(--navy); margin-bottom: .35rem; }
.why-card p { font-size: .86rem; color: var(--muted); line-height: 1.65; }

/* REVIEWS */
.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
}
.review-card {
  background: var(--white);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 16px rgba(0,0,0,.07);
  border: 1px solid var(--border);
}
.stars { color: #f59e0b; font-size: 1rem; letter-spacing: 2px; margin-bottom: .5rem; }
.review-text { font-size: .88rem; color: var(--text); line-height: 1.7; margin-bottom: .75rem; font-style: italic; }
.review-author { font-size: .82rem; font-weight: 700; color: var(--navy); }
.review-source { font-size: .74rem; color: var(--muted); display: flex; align-items: center; gap: .3rem; margin-top: .2rem; }

/* TECH SECTION */
.tech-section { background: var(--navy); padding: 4rem 1.25rem; }
.tech-inner {
  max-width: 960px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 2.5rem;
  align-items: center;
}
@media(max-width:640px){
  .tech-inner { grid-template-columns: 1fr; text-align: center; }
  .tech-photo { margin: 0 auto; }
}
.tech-photo {
  width: 140px; height: 140px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  border: 4px solid var(--blue);
  flex-shrink: 0;
  display: block;
}
.tech-text h3 { font-size: 1.5rem; font-weight: 900; color: var(--white); margin-bottom: .6rem; letter-spacing: -.01em; }
.tech-text p { color: rgba(255,255,255,.82); font-size: .93rem; line-height: 1.75; margin-bottom: .6rem; }
.tech-sig { font-weight: 700; color: #60a5fa; font-size: .88rem; }

/* CTA */
.cta-section { background: var(--blue); padding: 4rem 1.25rem; text-align: center; }
.cta-section h2 { font-size: clamp(1.7rem, 3.5vw, 2.6rem); font-weight: 900; color: var(--white); letter-spacing: -.02em; margin-bottom: .5rem; }
.cta-section p { color: rgba(255,255,255,.88); font-size: .95rem; margin-bottom: 2rem; }
.cta-btns { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; }
.btn-cta-call {
  display: inline-flex; align-items: center; gap: .5rem;
  background: var(--white); color: var(--blue);
  font-weight: 700; font-size: 1.05rem;
  padding: .95rem 2rem; border-radius: 50px;
  transition: transform .15s;
}
.btn-cta-call:hover { transform: scale(1.03); }
.btn-cta-form {
  display: inline-flex; align-items: center; gap: .5rem;
  background: rgba(0,0,0,.18); color: var(--white);
  font-weight: 600; font-size: .97rem;
  padding: .95rem 2rem; border-radius: 50px;
  border: 2px solid rgba(255,255,255,.45);
  transition: background .2s;
}
.btn-cta-form:hover { background: rgba(0,0,0,.3); }

/* FAQ */
.faq-wrap { max-width: 740px; margin: 0 auto; }
.faq-row { border-bottom: 1px solid var(--border); }
.faq-row:first-child { border-top: 1px solid var(--border); }
.faq-q-btn {
  width: 100%; text-align: left; background: none; border: none;
  padding: 1.1rem 0; font-size: .92rem; font-weight: 600;
  color: var(--navy); cursor: pointer;
  display: flex; justify-content: space-between; align-items: center; gap: .75rem;
  font-family: inherit;
}
.faq-caret { font-size: 1.2rem; color: var(--blue); font-weight: 300; flex-shrink: 0; transition: transform .25s; }
.faq-row.open .faq-caret { transform: rotate(45deg); }
.faq-ans { max-height: 0; overflow: hidden; transition: max-height .3s ease; }
.faq-row.open .faq-ans { max-height: 400px; }
.faq-ans-inner { padding-bottom: 1rem; font-size: .87rem; color: var(--muted); line-height: 1.75; }

/* FOOTER */
.lp-footer {
  background: #080c14;
  color: #6b7280;
  text-align: center;
  padding: 1.5rem 1.25rem;
  font-size: .78rem;
  line-height: 1.9;
}
.lp-footer a { color: #60a5fa; }

/* STICKY BAR */
.sticky-bar { position:fixed; bottom:0; left:0; right:0; display:flex; z-index:999; box-shadow:0 -1px 8px rgba(0,0,0,.25); }
.s-btn { flex:1; display:flex; align-items:center; justify-content:center; gap:.4rem; padding:15px 8px; font-size:.9rem; font-weight:700; color:#fff; border:none; cursor:pointer; text-decoration:none; font-family:inherit; }
.s-sms  { background:#166534; }
.s-call { background:var(--blue); }
"""

NAV_HTML = """<nav class="site-nav">
  <div class="nav-inner">
    <div class="nav-stars">
      <div class="stars-row">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="stars-label">5.0 Google Reviews</div>
    </div>
    <div class="nav-logo">
      <img src="/norcal/images/logo.png" alt="Alliance Air Care" width="80" height="80">
    </div>
    <div class="nav-cta-wrap">
      <a class="nav-cta" href="tel:+15307189271" onclick="return gtag_report_conversion('tel:+15307189271');">(530) 718-9271</a>
    </div>
  </div>
</nav>"""

def trust_bar(city="Sacramento Valley"):
    return f"""<div class="trust-bar">
  <div class="trust-bar-inner">
    <div class="trust-item">{STAR_SVG} 5.0 Google Rating</div>
    <div class="trust-item">{SHIELD_SVG} Licensed &amp; Insured</div>
    <div class="trust-item">{CLOCK_SVG} Fast Response</div>
    <div class="trust-item">{PIN_SVG} Serving {city}</div>
  </div>
</div>"""

def cost_section(title, items, note):
    cards = ""
    for amt, desc in items:
        cards += f'<div class="cost-card"><span class="cost-amount">{amt}</span><p>{desc}</p></div>\n'
    return f"""<div class="cost-callout">
  <div class="cost-callout-inner">
    <h2>{title}</h2>
    <div class="cost-grid">{cards}</div>
    <p class="cost-note">{note}</p>
  </div>
</div>"""

def checklist_section(title, sub, items, alt=False):
    checks = ""
    for item in items:
        checks += f'<div class="check-item"><div class="check-icon">{CHECK_SVG}</div><span>{item}</span></div>\n'
    cls = "section alt" if alt else "section"
    return f"""<section class="{cls}">
  <div class="section-inner">
    <h2 class="section-title">{title}</h2>
    <p class="section-sub">{sub}</p>
    <div class="checklist-grid">{checks}</div>
  </div>
</section>"""

def why_section(title, sub, alt=True):
    cards = ""
    for h, p, icon in WHY_CARDS:
        cards += f"""<div class="why-card">
  <h3>{h}</h3>
  <p>{p}</p>
</div>\n"""
    cls = "section alt" if alt else "section"
    return f"""<section class="{cls}">
  <div class="section-inner">
    <h2 class="section-title">{title}</h2>
    <p class="section-sub">{sub}</p>
    <div class="why-grid">{cards}</div>
  </div>
</section>"""

def reviews_section():
    cards = ""
    for author, text, src in REVIEWS:
        cards += f"""<div class="review-card">
  <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
  <p class="review-text">"{text}"</p>
  <div class="review-author">{author}</div>
  <div class="review-source">{GOOGLE_SVG} {src}</div>
</div>\n"""
    return f"""<section class="section">
  <div class="section-inner">
    <h2 class="section-title">What NorCal Homeowners<br><span>Are Saying</span></h2>
    <p class="section-sub">Real reviews from the Sacramento Valley — 5.0 stars on Google.</p>
    <div class="reviews-grid">{cards}</div>
  </div>
</section>"""

def tech_section(h3, body):
    return f"""<section class="tech-section">
  <div class="tech-inner">
    <img src="/norcal/images/cameron-habib.png" alt="Cameron Habib, Owner &amp; Operator — Alliance Air Care" class="tech-photo">
    <div class="tech-text">
      <h3>{h3}</h3>
      <p>{body}</p>
      <div class="tech-sig">— Cameron Habib, Owner &amp; Operator</div>
    </div>
  </div>
</section>"""

def cta_section(h2, sub, form_id):
    return f"""<section class="cta-section">
  <h2>{h2}</h2>
  <p>{sub}</p>
  <div class="cta-btns">
    <a href="tel:+15307189271" class="btn-cta-call" onclick="return gtag_report_conversion('tel:+15307189271');">{PHONE_SVG} Call {PHONE}</a>
    <a href="#" class="btn-cta-form" onclick="document.getElementById('{form_id}').scrollIntoView({{behavior:'smooth',block:'center'}});return false;">Fill Out the Form</a>
  </div>
</section>"""

def faq_section(items):
    rows = ""
    for q, a in items:
        rows += f"""<div class="faq-row">
  <button class="faq-q-btn">{q}<span class="faq-caret">+</span></button>
  <div class="faq-ans"><div class="faq-ans-inner">{a}</div></div>
</div>\n"""
    return f"""<section class="section">
  <div class="section-inner">
    <h2 class="section-title" style="margin-bottom:1.5rem;">Frequently Asked <span>Questions</span></h2>
    <div class="faq-wrap">{rows}</div>
  </div>
</section>"""

def hero_section(h1, badges, sub, form_id, form_title, form_sub, form_options, form_source, form_btn, form_tag='Free Estimate &mdash; No Obligation'):
    badge_html = ""
    for hl, label in badges:
        cls = "badge-pill hl" if hl == "hl" else "badge-pill"
        badge_html += f'<span class="{cls}">{label}</span>\n'
    opts = ""
    for val, label in form_options:
        opts += f'<option value="{val}">{label}</option>\n'
    return f"""<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-badges">{badge_html}</div>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <a href="tel:+15307189271" class="hero-phone" onclick="return gtag_report_conversion('tel:+15307189271');">Call Now &mdash; {PHONE}</a>
    </div>
    <div class="form-card">
      <div class="form-card-head">
        <div class="free-tag">{form_tag}</div>
        <h2>{form_title}</h2>
        <p>{form_sub}</p>
      </div>
      <form id="{form_id}">
        <input type="hidden" name="source" value="{form_source}">
        <input type="text" name="name" placeholder="Your name" required autocomplete="name">
        <input type="tel" name="phone" placeholder="Your phone number" required autocomplete="tel">
        <input type="email" name="email" placeholder="Email address">
        <div class="select-wrap">
          <select name="service" required>
            <option value="">— What do you need? —</option>
            {opts}
          </select>
        </div>
        <button type="submit" class="btn-submit">{form_btn}</button>
      </form>
      <div class="form-success" id="{form_id}Success">Got it! We&rsquo;ll call you shortly. &mdash; Alliance Air Care</div>
      <div class="form-trust">
        <span>{SHIELD_SVG} Licensed &amp; Insured</span>
        <span>{STAR_SVG} 5.0 Google Rating</span>
        <span>{CLOCK_SVG} Fast Response</span>
      </div>
    </div>
  </div>
</section>"""

def footer_html(page_name):
    return f"""<footer class="lp-footer">
  &copy; 2025 Alliance Air Care &mdash; Northern California &mdash; HVAC License #1129578<br>
  <a href="/norcal/">All NorCal Services</a> &nbsp;&middot;&nbsp; <a href="/privacy-policy.html">Privacy Policy</a>
</footer>"""

def sticky_bar():
    return f"""<div class="sticky-bar">
  <a class="s-btn s-sms" href="sms:+15307189271" onclick="return gtag_report_text_conversion('sms:+15307189271');">Text Us</a>
  <a class="s-btn s-call" href="tel:+15307189271" onclick="return gtag_report_conversion('tel:+15307189271');">Call {PHONE}</a>
</div>"""

def scripts(form_id, label):
    return f"""<script>
function gtag_report_conversion(url){{var c=function(){{if(typeof url!='undefined'){{window.location=url;}}}};gtag('event','conversion',{{'send_to':'AW-18069143145/AW_conversion','event_callback':c}});return false;}}
function gtag_report_text_conversion(url){{var c=function(){{if(typeof url!='undefined'){{window.location=url;}}}};gtag('event','conversion',{{'send_to':'AW-18069143145/text_conversion','event_callback':c}});return false;}}
document.getElementById('{form_id}').addEventListener('submit',function(e){{
  e.preventDefault();var d=new FormData(this),btn=this.querySelector('.btn-submit');
  btn.textContent='Sending...';btn.disabled=true;
  fetch('/send-mail.php',{{method:'POST',body:d}}).then(r=>r.text()).then(t=>{{
    if(t.trim()==='SUCCESS'){{this.style.display='none';document.getElementById('{form_id}Success').style.display='block';gtag('event','form_submit',{{'event_category':'Lead','event_label':'{label}'}});}}
    else{{btn.textContent='{{}}'.replace('{{}}','Request Service →');btn.disabled=false;}}
  }}).catch(()=>{{btn.textContent='Request Service →';btn.disabled=false;}});
}});
document.querySelectorAll('.faq-q-btn').forEach(btn=>{{
  btn.addEventListener('click',function(){{
    var row=this.closest('.faq-row'),open=row.classList.contains('open');
    document.querySelectorAll('.faq-row').forEach(r=>r.classList.remove('open'));
    if(!open)row.classList.add('open');
  }});
}});
</script>"""

def build_page(meta, body_sections, form_id, label):
    schema = f"""{{
  "@context":"https://schema.org",
  "@graph":[
    {{"@type":"HVACBusiness","name":"Alliance Air Care","url":"https://allianceaircare.com","telephone":"+15307189271","areaServed":"Northern California"}},
    {{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://allianceaircare.com/"}},
      {{"@type":"ListItem","position":2,"name":"NorCal HVAC","item":"https://allianceaircare.com/norcal/"}},
      {{"@type":"ListItem","position":3,"name":"{meta['bc']}","item":"{meta['canonical']}"}}
    ]}}
  ]
}}"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta['title']}</title>
<meta name="description" content="{meta['desc']}">
<link rel="canonical" href="{meta['canonical']}">
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-WG429BHX');</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CST45VC15M"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-CST45VC15M');gtag('config','AW-18069143145');</script>
<style>{CSS}</style>
<script type="application/ld+json">{schema}</script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WG429BHX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{NAV_HTML}
{''.join(body_sections)}
{footer_html(meta['bc'])}
{sticky_bar()}
{scripts(form_id, label)}
</body>
</html>"""

# ─────────────────────────────────────────────
# PAGE DEFINITIONS
# ─────────────────────────────────────────────

pages = {}

# ── AC REPAIR ──
pages['ac-repair'] = build_page(
    meta={
        'title': 'AC Repair in Northern California — Fast Service | Alliance Air Care',
        'desc':  'Fast AC repair across NorCal\'s Sacramento Valley. All makes and models, upfront pricing. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/ac-repair/',
        'bc': 'AC Repair',
    },
    form_id='acForm',
    label='norcal-ac-repair',
    body_sections=[
        hero_section(
            h1='AC Repair in<br>Northern California.<br><span>Fast Service.</span>',
            badges=[('hl','Fast Service'),('','All Makes &amp; Models')],
            sub='When your AC dies in a Sacramento Valley heat wave, it\'s a health risk — not just an inconvenience. We respond fast, arrive with a stocked truck, and give you the price before we touch anything.',
            form_id='acForm', form_title='Request AC Repair',
            form_sub='We\'ll call to confirm — usually within the hour.',
            form_options=[('Not cooling at all','Not cooling at all'),('Not cooling enough','Not cooling enough'),('Making unusual noise','Making unusual noise'),('Unit not turning on','Unit not turning on'),('Leaking water','Leaking water'),('Thermostat issues','Thermostat issues'),('Other / Not sure','Other / Not sure')],
            form_source='norcal-ac-repair', form_btn='Request Fast Service &rarr;',
            form_tag='$85 Diagnostic',
        ),
        trust_bar(),
        cost_section(
            'The Real Cost of<br><span>Waiting on AC Repair</span>',
            [('$85','Diagnostic visit — full quote before any work begins'),('$350','Average repair cost when caught on the first visit'),('$4,500+','Average system replacement from ignored small issues'),('70%','Of failures can be avoided with early diagnosis')],
            'Most AC problems get worse — and more expensive — the longer you wait.',
        ),
        checklist_section(
            'Common AC Problems<br><span>We Fix</span>',
            'Our trucks carry the parts for the most common NorCal failures. Most calls are resolved in one visit.',
            ['AC blowing warm air or not cooling','Unit won\'t turn on at all','Low refrigerant or refrigerant leak','Frozen evaporator coils','Loud banging, rattling, or squealing','Water leaking from indoor unit','Thermostat not communicating with system','Compressor not running','Bad capacitor or contactor','Short cycling — unit turns on and off constantly'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','We\'re a local crew — not a dispatch center. You get us, directly, every time.',alt=True),
        reviews_section(),
        tech_section('We Fix It Right,<br>First Time.','I\'ve seen too many homeowners get stuck with a $4,500 replacement that should have been a $350 repair — if someone had just shown up honest and on time. That\'s what we do. Fast response, diagnosed correctly, priced upfront. No pressure, no runaround.'),
        faq_section([
            ('How fast can you respond?','For most of NorCal\'s Sacramento Valley — Yuba City, Marysville, Chico, Woodland, Oroville, Auburn, Lincoln — we respond fast. Call in the morning and we\'re usually there that day.'),
            ('Do you charge a diagnostic fee?','Yes, $85 for a diagnostic visit. That fee applies toward the repair if you proceed. You get a full quote before any work begins.'),
            ('What brands do you work on?','All major brands — Carrier, Trane, Lennox, Rheem, Goodman, York, American Standard, and more.'),
            ('What if my unit can\'t be repaired?','We\'ll be honest with you. If repair doesn\'t make financial sense, we\'ll explain why and give you an install quote — no pressure either way.'),
            ('Do you warranty your repairs?','Yes. All parts and labor are warrantied. We stand behind every job.'),
        ]),
        cta_section('Ready to Fix Your AC?','Fast service · Upfront pricing · All makes and models','acForm'),
    ]
)

# ── MAINTENANCE ──
pages['maintenance'] = build_page(
    meta={
        'title': 'HVAC Maintenance in Northern California | Alliance Air Care',
        'desc':  'Preventive HVAC maintenance across NorCal\'s Sacramento Valley. Stop breakdowns before they start, extend system life, lower energy bills. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/maintenance/',
        'bc': 'Maintenance',
    },
    form_id='maintForm',
    label='norcal-maintenance',
    body_sections=[
        hero_section(
            h1='HVAC Maintenance in<br>Northern California.<br><span>Stop Breakdowns Early.</span>',
            badges=[('hl','Prevent Costly Failures'),('','Fast Response')],
            sub='A $150 tune-up today prevents a $3,500 emergency tomorrow. We keep your system running clean, efficient, and reliable — so it\'s ready when NorCal summer hits.',
            form_id='maintForm', form_title='Schedule Your Tune-Up',
            form_sub='We\'ll call back within the hour.',
            form_options=[('AC Tune-Up / Maintenance','AC Tune-Up / Maintenance'),('Furnace Tune-Up / Maintenance','Furnace Tune-Up / Maintenance'),('Full System Inspection','Full System Inspection'),('Filter Check &amp; Replacement','Filter Check &amp; Replacement'),('Not Sure — Just Need a Check','Not Sure — Just Need a Check')],
            form_source='norcal-maintenance', form_btn='Schedule My Tune-Up &rarr;',
        ),
        trust_bar(),
        cost_section(
            'The Cost of<br><span>Skipping Maintenance</span>',
            [('$150','Annual tune-up — keeps your system running right all year'),('$800+','Average repair when a small issue goes unnoticed'),('$3,500+','Emergency system replacement from neglected maintenance'),('20%','Average energy savings when your HVAC is properly tuned')],
            'Regular maintenance costs a fraction of emergency repairs — and keeps your manufacturer warranty valid.',
        ),
        checklist_section(
            'What\'s Included in Your<br><span>HVAC Tune-Up</span>',
            'A thorough inspection — not a 15-minute checkmark job.',
            ['Inspect and clean condenser &amp; evaporator coils','Check and top off refrigerant levels','Test and calibrate thermostat accuracy','Inspect all electrical connections and capacitors','Lubricate all moving mechanical parts','Inspect and replace air filter if needed','Check ductwork for leaks or disconnections','Test system startup, shutdown, and safety controls','Measure airflow and temperature differential','Full written condition report — every visit'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','Honest maintenance — no scare tactics, no upsell pressure. If it\'s fine, we tell you it\'s fine.',alt=True),
        reviews_section(),
        tech_section('We Treat Your System<br>Like It\'s Our Own.','I\'ve seen too many homeowners get blindsided by a $4,000 repair that could\'ve been caught at a $150 tune-up. When I come out, I\'m thorough — because catching something small now is how I save you money later. That\'s the kind of service I\'d want for my own family.'),
        faq_section([
            ('How often should I have my HVAC serviced?','Twice a year is ideal — once before cooling season (spring) and once before heating season (fall). At minimum, once a year keeps your warranty valid and catches developing issues.'),
            ('Will you try to upsell me on parts I don\'t need?','No. If your system checks out clean, we tell you that and you\'re on your way. We only recommend work when it\'s genuinely needed.'),
            ('How long does a tune-up take?','Most maintenance visits take 45–75 minutes depending on system type and condition.'),
            ('Do you service both AC and furnace?','Yes — we service all HVAC equipment: central AC, heat pumps, gas furnaces, and mini-split systems.'),
            ('What areas do you serve?','Yuba City, Marysville, Chico, Woodland, Oroville, Lincoln, Auburn, Gridley, and surrounding Sacramento Valley communities.'),
        ]),
        cta_section('Don\'t Wait for a Breakdown.','Schedule your tune-up today · Free estimate · Same-day response','maintForm'),
    ]
)

# ── NEW INSTALLS ──
pages['new-installs'] = build_page(
    meta={
        'title': 'New HVAC Installation in Northern California | Alliance Air Care',
        'desc':  'New HVAC system installation across NorCal\'s Sacramento Valley. All major brands, free estimates, licensed installation. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/new-installs/',
        'bc': 'New Installs',
    },
    form_id='installForm',
    label='norcal-new-installs',
    body_sections=[
        hero_section(
            h1='New HVAC Installation<br>in Northern California.<br><span>Done Right, Day One.</span>',
            badges=[('hl','Free Estimate'),('','All Major Brands')],
            sub='A new system is a 15-year investment. We help you pick the right unit for your home and NorCal\'s climate — then install it cleanly, correctly, and on schedule.',
            form_id='installForm', form_title='Get a Free Install Estimate',
            form_sub='No pressure. We\'ll size your home and give you an honest quote.',
            form_options=[('New Central AC System','New Central AC System'),('New Furnace / Heater','New Furnace / Heater'),('Full System Replacement (AC + Furnace)','Full System Replacement (AC + Furnace)'),('Mini-Split Installation','Mini-Split Installation'),('Heat Pump System','Heat Pump System'),('Not sure — need recommendation','Not sure — need recommendation')],
            form_source='norcal-new-installs', form_btn='Get My Free Estimate &rarr;',
        ),
        trust_bar(),
        cost_section(
            'What to Expect with<br><span>a New Install</span>',
            [('Free','Full load calculation and estimate — no obligation, no surprise pricing'),('$4,500','Average new central AC install, fully sized for your home'),('15 yrs','Average lifespan of a properly installed, maintained system'),('30%','Typical energy savings upgrading from a 10+ year old system')],
            'The right system, properly installed, pays for itself in lower energy bills and fewer repair calls.',
        ),
        checklist_section(
            'Our Installation<br><span>Process</span>',
            'We don\'t rush installs. Every step is done right so your system runs reliably for years.',
            ['Free in-home assessment and load calculation','Brand and model recommendation based on your home and budget','Transparent written quote — no hidden fees','Removal and disposal of old equipment','Full system installation to manufacturer spec','Ductwork inspection and sealing if needed','Thermostat installation and programming','System test and performance verification','Walk-through of your new system and controls','Follow-up call to confirm everything\'s working right'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','We install brands we\'d put in our own homes — and we stand behind every job.',alt=True),
        reviews_section(),
        tech_section('A Good Install Lasts<br>15 Years. A Bad One Doesn\'t.','Most system failures I\'ve seen trace back to an undersized unit, a rushed install, or skipped ductwork. We take the time to size it right, seal it right, and test it before we leave. That\'s why our installs last.'),
        faq_section([
            ('How long does a new HVAC installation take?','Most residential installations take 4–8 hours. A full system replacement (AC + furnace) may take a full day. We give you a realistic timeline upfront.'),
            ('What brands do you install?','Carrier, Trane, Lennox, Rheem, Goodman, and more. We\'ll recommend the best fit for your home and budget — not the highest margin unit.'),
            ('Do you handle permits?','Yes. We pull all required permits and ensure the installation meets California code requirements.'),
            ('Can I finance a new system?','Yes, financing options are available. Ask us when you call for your estimate.'),
            ('What if my ductwork needs work too?','We inspect ductwork as part of every new install assessment. If it needs sealing or repair, we\'ll include that in the quote.'),
        ]),
        cta_section('Ready for a New System?','Free estimate · All major brands · Licensed installation','installForm'),
    ]
)

# ── MINI-SPLITS ──
pages['mini-splits'] = build_page(
    meta={
        'title': 'Mini-Split Installation & Repair in Northern California | Alliance Air Care',
        'desc':  'Mini-split installation and repair across NorCal. Perfect for room additions, garages, and older homes. Single and multi-zone systems. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/mini-splits/',
        'bc': 'Mini-Splits',
    },
    form_id='miniForm',
    label='norcal-mini-splits',
    body_sections=[
        hero_section(
            h1='Mini-Split Installation<br>&amp; Repair in NorCal.<br><span>Zone by Zone.</span>',
            badges=[('hl','No Ductwork Needed'),('','Up to 40% More Efficient')],
            sub='Perfect for room additions, garages, older homes, and any space central AC can\'t reach. We install and service single-zone and multi-zone mini-splits across the Sacramento Valley.',
            form_id='miniForm', form_title='Get a Mini-Split Quote',
            form_sub='We\'ll recommend the right system for your space.',
            form_options=[('Mini-Split Installation (Single Zone)','Mini-Split Installation (Single Zone)'),('Mini-Split Installation (Multi-Zone)','Mini-Split Installation (Multi-Zone)'),('Mini-Split Repair','Mini-Split Repair'),('Mini-Split Maintenance','Mini-Split Maintenance'),('Not sure — need advice','Not sure — need advice')],
            form_source='norcal-mini-splits', form_btn='Get My Quote &rarr;',
        ),
        trust_bar(),
        cost_section(
            'Mini-Split vs.<br><span>Other Options</span>',
            [('$1,800','Single-zone mini-split installed — heat and cool one room'),('$4,500+','Multi-zone system serving 3–4 rooms from one outdoor unit'),('40%','More efficient than window units — lower electric bills year-round'),('0','Ductwork required — ideal for homes without existing ducts')],
            'Mini-splits heat and cool — one system, year-round comfort, no ductwork.',
        ),
        checklist_section(
            'Where Mini-Splits<br><span>Work Best</span>',
            'If central HVAC can\'t reach it — or doesn\'t exist — a mini-split is the right answer.',
            ['Room additions and converted garages','Older homes without existing ductwork','Home offices and workshops','Bonus rooms and finished attics','Guest suites and in-law units','Sunrooms and three-season spaces','Server rooms and equipment areas','Any room that\'s always too hot or too cold'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','We size and install mini-splits correctly — the right BTU for your space, every time.',alt=True),
        reviews_section(),
        tech_section('The Right Mini-Split,<br>Installed Right.','I\'ve seen cheap installs where the unit is undersized for the space or poorly placed — and they never cool right. We do a proper heat load calculation, position the head correctly, and make sure the refrigerant line is sealed and insulated. Done right, these systems last 20 years.'),
        faq_section([
            ('How long does a mini-split installation take?','Most single-zone installs take 3–5 hours. Multi-zone systems take a full day depending on the number of indoor heads and line routing.'),
            ('What brands do you install?','Mitsubishi, Daikin, LG, Carrier, and others. We\'ll recommend based on your space, budget, and reliability needs.'),
            ('Do mini-splits work for heating too?','Yes — modern mini-splits are heat pumps. They provide efficient heating down to well below freezing, making them a year-round solution.'),
            ('Do I need to do anything to my existing system?','No. Mini-splits are completely independent. They\'re often added to supplement an existing central system for rooms that need extra conditioning.'),
            ('What maintenance do mini-splits need?','Filter cleaning every 1–2 months (takes 5 minutes) and an annual professional service visit. Much lower maintenance than central systems.'),
        ]),
        cta_section('Ready to Add a Mini-Split?','Free estimate · Same-day response · All major brands','miniForm'),
    ]
)

# ── FILTER REPLACEMENTS ──
pages['filter-replacements'] = build_page(
    meta={
        'title': 'Air Filter Replacement in Northern California | Alliance Air Care',
        'desc':  'Professional air filter replacement and HVAC filter service across NorCal. Improve air quality, protect your system, lower energy bills. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/filter-replacements/',
        'bc': 'Filter Replacements',
    },
    form_id='filterForm',
    label='norcal-filter-replacements',
    body_sections=[
        hero_section(
            h1='Air Filter Replacement<br>in Northern California.<br><span>Protect Your System.</span>',
            badges=[('hl','Improve Air Quality'),('','MERV 8–13 Available')],
            sub='A clogged filter strains your blower, freezes your coils, and drives up your energy bill. We replace filters and set you up with the right schedule — so you\'re never running dirty air through a stressed system.',
            form_id='filterForm', form_title='Schedule Filter Service',
            form_sub='Quick visit, big difference.',
            form_options=[('Standard Filter Replacement','Standard Filter Replacement'),('MERV 11 Upgrade','MERV 11 Upgrade'),('MERV 13 High-Efficiency Filter','MERV 13 High-Efficiency Filter'),('Filter + System Inspection','Filter + System Inspection'),('Not sure — need recommendation','Not sure — need recommendation')],
            form_source='norcal-filter-replacements', form_btn='Schedule Filter Service &rarr;',
        ),
        trust_bar(),
        cost_section(
            'What a Dirty Filter<br><span>Actually Costs You</span>',
            [('15%','Average increase in energy consumption from a clogged filter'),('$800+','Average coil repair when restricted airflow causes freezing'),('3 mo.','Recommended replacement interval for 1-inch filters in NorCal'),('MERV 11','The sweet spot — captures dust, pollen, and pet dander without overworking your system')],
            'A $25 filter replacement is the cheapest maintenance you can do — and one of the most important.',
        ),
        checklist_section(
            'MERV Ratings<br><span>Explained Simply</span>',
            'Not all filters are equal. Here\'s what to know for NorCal homes.',
            ['MERV 6–8: Basic filtration — stops large particles, low restriction','MERV 11: Recommended for most homes — captures dust, pollen, pet dander','MERV 13: Best for allergy sufferers — captures fine particles and smoke','Higher isn\'t always better — too-high MERV can restrict airflow on older systems','1-inch filters: Replace every 60–90 days in NorCal (dust season)','4-inch media filters: Can last 6–12 months with proper system maintenance','Dirty filter = restricted airflow = frozen coils = expensive repair','Check your filter monthly — takes 30 seconds'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','We don\'t just swap the filter — we check the system while we\'re there.',alt=True),
        reviews_section(),
        tech_section('The Filter Is the<br>Cheapest Insurance You Have.','I see system failures every week that started with a filter that hadn\'t been changed in 8 months. The blower runs hot, the coil freezes, and suddenly a $25 filter became a $900 repair. We can help you stay on schedule and make sure you\'re running the right filter for your system.'),
        faq_section([
            ('How often should I change my air filter?','For 1-inch filters: every 60–90 days in NorCal, more often if you have pets or allergies. For 4-inch media filters: every 6–12 months. We\'ll tell you the right interval for your system.'),
            ('What MERV rating do you recommend?','MERV 11 for most homes. It captures dust, pollen, and pet dander without restricting airflow. MERV 13 for households with allergies or asthma. We don\'t recommend MERV 16+ for residential systems.'),
            ('Can a dirty filter damage my AC?','Yes. Restricted airflow causes the evaporator coil to freeze, which can damage the compressor. It also overworks the blower motor. A clogged filter is one of the leading causes of AC failure.'),
            ('Can you set me up on a filter schedule?','Absolutely. We\'ll note your filter size and type and can remind you when it\'s time to change it, or include it in an annual maintenance visit.'),
            ('Do you supply the filters?','Yes — we bring the right filter for your system. No need to source it yourself.'),
        ]),
        cta_section('Ready to Breathe Cleaner Air?','Quick service · Right filter for your system · Same-day available','filterForm'),
    ]
)

# ── DUCTWORK ──
pages['ductwork'] = build_page(
    meta={
        'title': 'Ductwork Repair & Sealing in Northern California | Alliance Air Care',
        'desc':  'Ductwork leak testing, sealing, and repair across NorCal\'s Sacramento Valley. Stop losing 20–30% of your conditioned air. Call (530) 718-9271.',
        'canonical': 'https://allianceaircare.com/norcal/ductwork/',
        'bc': 'Ductwork',
    },
    form_id='ductForm',
    label='norcal-ductwork',
    body_sections=[
        hero_section(
            h1='Ductwork Repair &amp;<br>Sealing in NorCal.<br><span>Stop Wasting Air.</span>',
            badges=[('hl','Most Homes Lose 20–30%'),('','Leak Testing Available')],
            sub='Leaky ducts dump your cooled air into the attic instead of your rooms. The result: rooms that never get comfortable, and an AC that runs constantly. We find the leaks and seal them — and the energy savings often pay for the job in under a year.',
            form_id='ductForm', form_title='Request Ductwork Service',
            form_sub='Free assessment — we quote before we start.',
            form_options=[('Duct Inspection / Leak Test','Duct Inspection / Leak Test'),('Duct Sealing','Duct Sealing'),('Duct Repair','Duct Repair'),('Duct Replacement (partial)','Duct Replacement (partial)'),('Full Ductwork Replacement','Full Ductwork Replacement'),('Not sure — need assessment','Not sure — need assessment')],
            form_source='norcal-ductwork', form_btn='Request Duct Assessment &rarr;',
        ),
        trust_bar(),
        cost_section(
            'What Leaky Ducts<br><span>Are Costing You</span>',
            [('20–30%','Of conditioned air lost in the average home with leaky ducts'),('$400+','Annual energy waste from duct leakage in a typical NorCal home'),('1 yr','Average payback period on duct sealing from energy savings alone'),('$0','Extra equipment needed — sealing existing ducts solves most problems')],
            'Your AC may be working perfectly — but if the ducts are leaking, you\'re paying to cool your attic.',
        ),
        checklist_section(
            'Warning Signs Your<br><span>Ducts Are Leaking</span>',
            'Leaky ducts are often invisible — but the symptoms are clear.',
            ['Rooms that won\'t cool down even on max AC','Uneven temperatures room to room','Higher-than-expected electric bills','Dusty rooms despite regular cleaning','AC runs constantly but never reaches set temperature','Visible gaps, tears, or disconnections in attic ductwork','Rooms above garage or over crawlspace that won\'t cool','System short-cycling or running longer than it should'],
            alt=False,
        ),
        why_section('Why NorCal Homeowners<br>Choose <span>Alliance Air Care</span>','We test before we quote — so you only pay for work that actually needs doing.',alt=True),
        reviews_section(),
        tech_section('Fix the Ducts First.<br>Everything Else Follows.','Half the "AC problems" I\'m called out for are actually duct problems. The system is fine — but it\'s pumping air into the attic. We test with pressure diagnostics to find exactly where the leaks are before we start. No guessing, no unnecessary work.'),
        faq_section([
            ('How do you test for duct leaks?','We use a duct blaster test — a calibrated fan that pressurizes the duct system and measures air loss. This tells us exactly how much is leaking and helps us locate the problem areas.'),
            ('How much can duct sealing save me?','Most homeowners see 15–25% reductions in cooling and heating costs after duct sealing. In a 2,000 sq ft NorCal home, that\'s often $300–$600 per year.'),
            ('Do you use mastic or tape to seal ducts?','We use mastic sealant and UL-listed metal tape — not standard duct tape, which fails within a few years. Our seals are built to last.'),
            ('Can you seal ducts in a finished home?','Yes. We access ducts through the attic, crawlspace, or existing access points. We can seal most duct systems without opening walls or ceilings.'),
            ('When does ductwork need to be replaced vs. just sealed?','If ducts are severely deteriorated, crushed, or incorrectly sized, sealing alone won\'t fix the problem. We\'ll assess and give you an honest recommendation — repair where possible, replace where necessary.'),
        ]),
        cta_section('Ready to Stop Wasting Cool Air?','Free assessment · Quote before we start · Licensed & insured','ductForm'),
    ]
)

# ─────────────────────────────────────────────
# WRITE FILES
# ─────────────────────────────────────────────
base = os.path.dirname(os.path.abspath(__file__))
for slug, html in pages.items():
    out_dir = os.path.join(base, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w') as f:
        f.write(html)
    print(f"Written: {slug}/index.html ({len(html):,} bytes)")

print("\nDone — 6 pages rebuilt.")
