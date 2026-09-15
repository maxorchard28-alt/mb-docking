#!/usr/bin/env python3
"""Assembles the M&B Docking static site pages from shared header/footer + page content."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

LOGO_IMG = '<img class="brand-logo" src="assets/mb-logo.png" alt="M&B Docking — Docking Done Right" />'

FACEBOOK_URL = "https://www.facebook.com/p/MB-Docking-61561018682896/"
PHONE = "641-231-2744"
PHONE_TEL = "6412312744"
EMAIL = "mbdockingcl@gmail.com"

def head(title, description, active):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{description}" />
  <title>{title}</title>
  <link rel="icon" type="image/png" href="assets/mb-logo.png" />

  <!-- Fonts -->
  <link rel="preconnect" href="https://api.fontshare.com" />
  <link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@700,800,900&f[]=satoshi@400,500,700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="assets/style.css" />

  <!-- Open Graph -->
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
</head>
<body>
'''

def header(active):
    def link(href, label):
        cls = ' class="active"' if active == href else ''
        return f'<a href="{href}"{cls}>{label}</a>'

    return f'''  <!-- Top Bar -->
  <div class="topbar">
    <div class="container topbar-content">
      <div style="display:flex; align-items:center; gap:12px;">
        <span class="topbar-badge">5+ Years of Trusted Dock Service</span>
        <span>Clear Lake, Iowa</span>
      </div>
      <div>
        <span>Call or Text: </span>
        <a href="tel:{PHONE_TEL}">{PHONE}</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="header">
    <div class="container">
      <nav class="nav" aria-label="Main Navigation">
        <a class="brand" href="index.html">
          {LOGO_IMG}
          <span class="brand-text">
            <span class="brand-name">M&amp;B Docking</span>
            <span class="brand-tagline">Docking Done Right</span>
          </span>
        </a>
        <div class="nav-links" data-nav-links>
          {link('index.html', 'Home')}
          {link('about.html', 'About Us')}
          {link('services.html', 'Services')}
          {link('contact.html', 'Contact')}
        </div>
        <div class="nav-right">
          <button class="theme-toggle" data-theme-toggle aria-label="Toggle dark mode"></button>
          <a class="btn btn-gold" href="contact.html">Get a Free Estimate</a>
          <button class="menu-toggle" data-menu-toggle aria-label="Toggle menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
          </button>
        </div>
      </nav>
    </div>
  </header>
'''

def footer():
    return f'''  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          {LOGO_IMG}
          <span>
            <span class="footer-brand-name" style="display:block;">M&amp;B Docking</span>
            <span class="footer-brand-tag">Docking Done Right</span>
          </span>
        </div>
        <a class="social-link" href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="M&amp;B Docking on Facebook">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.53 17.52 2.04 12 2.04S2 6.53 2 12.06c0 5 3.66 9.13 8.44 9.88v-6.99h-2.54v-2.89h2.54V9.85c0-2.51 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.89h-2.34v6.99C18.34 21.19 22 17.06 22 12.06z"/></svg>
          Follow us on Facebook
        </a>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span id="year"></span> M&amp;B Docking. All rights reserved.</span>
        <span>Max Orchard &amp; Blake Enke &bull; Clear Lake, Iowa</span>
      </div>
    </div>
  </footer>

  <script src="assets/script.js"></script>
</body>
</html>
'''

def write_page(filename, title, description, active, content):
    html = head(title, description, active) + header(active) + content + footer()
    path = os.path.join(BASE, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f"Wrote {filename} ({len(html)} bytes)")

# ============ HOME PAGE ============
home_content = f'''  <main>
    <!-- Hero -->
    <section class="hero">
      <div class="container hero-content">
        <div class="hero-tag">Clear Lake, Iowa &bull; Locally Owned</div>
        <h1>Clear Lake Dock Service <span class="accent">You Can Count On</span></h1>
        <p>Professional dock installation, removal, maintenance, and repair from a team that grew up on Clear Lake and knows what your waterfront needs.</p>
        <div class="hero-ctas">
          <a class="btn btn-gold btn-lg" href="tel:{PHONE_TEL}">Call or Text {PHONE}</a>
          <a class="btn btn-outline btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.4);" href="contact.html">Request a Free Estimate</a>
        </div>
        <div class="hero-stats">
          <div class="stat-item">
            <strong>5+ Years</strong>
            <span>Hands-on dock experience</span>
          </div>
          <div class="stat-item">
            <strong>100%</strong>
            <span>Local, Clear Lake based</span>
          </div>
          <div class="stat-item">
            <strong>4</strong>
            <span>Core dock services</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Overview -->
    <section class="section" id="services">
      <div class="container">
        <div class="section-kicker">What We Do</div>
        <h2 class="section-title">Full-Service Dock Care</h2>
        <p class="section-lead">From spring install to fall removal, we keep your waterfront ready for the season &mdash; done right, every time.</p>

        <div class="services-grid">
          <article class="service-card">
            <div class="service-icon">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 12l4-4M3 12l4 4M21 6v12"/></svg>
            </div>
            <h3>Dock Installation</h3>
            <p>Custom sectional dock installs built for your shoreline and your needs, set up right at the start of the season.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12H4M20 12l-4-4M20 12l-4 4M4 18V6"/></svg>
            </div>
            <h3>Dock Removal</h3>
            <p>Safe, efficient removal at the end of the season to protect your dock investment from winter ice.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20" stroke-linecap="round"/><circle cx="12" cy="12" r="9"/></svg>
            </div>
            <h3>Dock Maintenance</h3>
            <p>Keep your dock strong, secure, and ready to enjoy all season long with regular upkeep and checks.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
            </div>
            <h3>Dock Repair</h3>
            <p>Fast, reliable repairs to get you back on the water &mdash; from bent poles to structural fixes.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Local Trust Section -->
    <section class="section" style="background: var(--color-surface);">
      <div class="container split">
        <div class="split-text">
          <div class="section-kicker">Who We Are</div>
          <h2 class="section-title">Local Roots, Reliable Work</h2>
          <p class="section-lead">Max and Blake both grew up and still live in Clear Lake. With more than five years of hands-on dock experience, we treat every property like it's our own.</p>
          <ul class="highlight-points">
            <li><div class="check-circle">&check;</div><span>5+ years of hands-on dock experience</span></li>
            <li><div class="check-circle">&check;</div><span>Born, raised, and living in Clear Lake, Iowa</span></li>
            <li><div class="check-circle">&check;</div><span>Careful work and clear communication</span></li>
            <li><div class="check-circle">&check;</div><span>Free, no-pressure estimates</span></li>
          </ul>
          <div style="margin-top: var(--space-8);">
            <a class="btn btn-black" href="about.html">Learn More About Us</a>
          </div>
        </div>
        <div class="split-visual">
          <div class="photo-frame">
            <img src="assets/max-and-blake.jpg" alt="Max Orchard and Blake Enke of M&B Docking at Clear Lake, Iowa" style="width:100%; height:100%; object-fit:cover; border-radius: var(--radius-lg);" />
          </div>
        </div>
      </div>
    </section>

    <!-- Gallery Section -->
    <section class="section">
      <div class="container">
        <div class="section-kicker">Our Work</div>
        <h2 class="section-title">Docks We've Installed &amp; Maintained</h2>
        <p class="section-lead">A look at the kind of work we do around Clear Lake &mdash; real project photos coming soon.</p>
        <div class="gallery-grid">
          <div class="gallery-item"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 12h18M3 12l4-4M3 12l4 4M21 6v12"/></svg></div>
          <div class="gallery-item"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 16l4.5-6 4 5 3-4L20 16M4 8h.01M4 4h16v16H4z" stroke-linejoin="round"/></svg></div>
          <div class="gallery-item"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="14" r="3"/><path d="M4 4h16v14a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"/></svg></div>
          <div class="gallery-item"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 12H4M20 12l-4-4M20 12l-4 4M4 18V6"/></svg></div>
        </div>
      </div>
    </section>

    <!-- Final CTA -->
    <section class="section-sm">
      <div class="container">
        <div class="cta-banner">
          <div>
            <h2>Ready for the season?</h2>
            <p>Get a free, no-obligation estimate for your dock project today.</p>
          </div>
          <a class="btn btn-gold btn-lg" href="contact.html">Request a Free Estimate</a>
        </div>
      </div>
    </section>
  </main>
'''

write_page(
    "index.html",
    "M&amp;B Docking | Clear Lake Dock Service You Can Count On",
    "M&B Docking provides reliable dock installation, removal, maintenance, and repair for Clear Lake, Iowa homeowners. Free estimates.",
    "index.html",
    home_content,
)
print("Home page built.")

# ============ ABOUT PAGE ============
about_content = f'''  <main>
    <!-- About Hero -->
    <section class="hero" style="padding-block: clamp(var(--space-12), 7vw, var(--space-24));">
      <div class="container hero-content">
        <div class="hero-tag">About M&amp;B Docking</div>
        <h1>Local Dock Service, <span class="accent">Built to Last</span></h1>
        <p>Proudly based in Clear Lake, Iowa. Max and Blake both grew up here, and we've been working on docks for more than five years.</p>
      </div>
    </section>

    <!-- About Story -->
    <section class="section">
      <div class="container split">
        <div class="split-text">
          <div class="section-kicker">Our Story</div>
          <h2 class="section-title">Clear Lake's Trusted Waterfront Partner</h2>
          <p class="section-lead">M&amp;B Docking is proudly based in Clear Lake, Iowa. Max Orchard and Blake Enke both grew up here, live here, and understand how important it is to keep your lake property ready for the season.</p>
          <p style="margin-top: var(--space-4); color: var(--color-text-muted);">With more than five years of hands-on experience working with docks, we provide reliable, straightforward service for local homeowners and lake-property owners. Whether you need help getting your dock in, taking it out, making repairs, or preparing your waterfront for the season, we focus on doing the work carefully and making the process easy for you.</p>
          <p style="margin-top: var(--space-4); color: var(--color-text-muted);">We are a local team that values dependable work, clear communication, and taking care of our neighbors around Clear Lake.</p>

          <ul class="highlight-points">
            <li><div class="check-circle">&check;</div><span><strong>5+ years of experience</strong> serving residential lake docks</span></li>
            <li><div class="check-circle">&check;</div><span><strong>Clear Lake locals</strong> &mdash; born, raised, and living here</span></li>
            <li><div class="check-circle">&check;</div><span><strong>Careful, dependable work</strong> every time</span></li>
            <li><div class="check-circle">&check;</div><span><strong>Clear communication</strong> and honest pricing</span></li>
          </ul>
        </div>

        <div class="split-visual">
          <div class="photo-frame">
            <img src="assets/max-and-blake.jpg" alt="Max Orchard and Blake Enke of M&B Docking at Clear Lake, Iowa" style="width:100%; height:100%; object-fit:cover; border-radius: var(--radius-lg);" />
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="section" style="background: var(--color-surface);">
      <div class="container">
        <div class="section-kicker">What We Stand For</div>
        <h2 class="section-title">Why Homeowners Choose M&amp;B Docking</h2>
        <p class="section-lead">We do the work carefully and make the process easy for you.</p>

        <div class="steps-grid">
          <div class="step-card">
            <div class="step-number">Value 01</div>
            <h3>Dependable Work</h3>
            <p>Every dock install, removal, and repair gets done right &mdash; the kind of work we'd want on our own waterfront.</p>
          </div>
          <div class="step-card">
            <div class="step-number">Value 02</div>
            <h3>Clear Communication</h3>
            <p>We keep you in the loop from first call to finished job. No surprises, no pressure, no jargon.</p>
          </div>
          <div class="step-card">
            <div class="step-number">Value 03</div>
            <h3>Taking Care of Neighbors</h3>
            <p>We're your neighbors around Clear Lake. Treating your property like our own is the only way we know how to work.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-sm">
      <div class="container">
        <div class="cta-banner">
          <div>
            <h2>Need a hand with your dock?</h2>
            <p>Reach out today for a free estimate. We're always happy to answer questions.</p>
          </div>
          <a class="btn btn-gold btn-lg" href="contact.html">Get in Touch</a>
        </div>
      </div>
    </section>
  </main>
'''

write_page(
    "about.html",
    "About M&amp;B Docking | Clear Lake, Iowa Dock Service",
    "M&B Docking is a Clear Lake, Iowa based dock service company with 5+ years of experience, owned by Max Orchard and Blake Enke. Learn about our story and values.",
    "about.html",
    about_content,
)
print("About page built.")

# ============ SERVICES PAGE ============
services_content = f'''  <main>
    <!-- Services Hero -->
    <section class="hero" style="padding-block: clamp(var(--space-12), 7vw, var(--space-24));">
      <div class="container hero-content">
        <div class="hero-tag">Our Services</div>
        <h1>Dock Services <span class="accent">Done Right</span></h1>
        <p>From spring install to fall removal and everything in between &mdash; we handle all your dock needs around Clear Lake.</p>
        <div class="hero-ctas">
          <a class="btn btn-gold btn-lg" href="tel:{PHONE_TEL}">Call or Text {PHONE}</a>
          <a class="btn btn-outline btn-lg" style="color:#fff; border-color:rgba(255,255,255,0.4);" href="contact.html">Request a Free Estimate</a>
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="section">
      <div class="container">
        <div class="section-kicker">What We Offer</div>
        <h2 class="section-title">Full-Service Dock Care</h2>
        <p class="section-lead">Clear, simple service options to keep your waterfront ready all season. Free estimates on every job.</p>

        <div class="services-grid">
          <article class="service-card">
            <div class="service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 12l4-4M3 12l4 4M21 6v12"/></svg>
            </div>
            <h3>Dock Installation</h3>
            <p>Custom sectional dock installs built for your needs. We handle the setup, leveling, and placement so you're ready to enjoy the lake from day one.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 12H4M20 12l-4-4M20 12l-4 4M4 18V6"/></svg>
            </div>
            <h3>Dock Removal</h3>
            <p>Safe, efficient removal at the end of the season. We disassemble and stage your dock carefully to protect it from winter ice damage.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20" stroke-linecap="round"/><circle cx="12" cy="12" r="9"/></svg>
            </div>
            <h3>Dock Maintenance</h3>
            <p>Keep your dock strong, secure, and ready. Regular checks and upkeep so your waterfront is always in top shape when you need it.</p>
          </article>

          <article class="service-card">
            <div class="service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
            </div>
            <h3>Dock Repair</h3>
            <p>Fast, reliable repairs to get you back on the water. From bent poles and damaged brackets to structural fixes &mdash; we solve it quickly.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="section" style="background: var(--color-surface);">
      <div class="container">
        <div class="section-kicker">Simple Process</div>
        <h2 class="section-title">How It Works</h2>
        <p class="section-lead">Getting your dock project started with M&amp;B Docking is easy.</p>

        <div class="steps-grid">
          <div class="step-card">
            <span class="step-number">Step 01</span>
            <h3>Request a Quote</h3>
            <p>Call, text, or fill out our contact form with your dock details and location around Clear Lake.</p>
          </div>
          <div class="step-card">
            <span class="step-number">Step 02</span>
            <h3>Get a Free Estimate</h3>
            <p>We review your lakefront layout, dock type, and seasonal schedule to give you a clear, honest quote.</p>
          </div>
          <div class="step-card">
            <span class="step-number">Step 03</span>
            <h3>Enjoy Your Waterfront</h3>
            <p>Our team handles install, repair, or removal cleanly and efficiently &mdash; without interrupting your lake time.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-sm">
      <div class="container">
        <div class="cta-banner">
          <div>
            <h2>Ready to get started?</h2>
            <p>Call or text us, or send a message and we'll get back to you promptly.</p>
          </div>
          <a class="btn btn-gold btn-lg" href="contact.html">Request a Free Estimate</a>
        </div>
      </div>
    </section>
  </main>
'''

write_page(
    "services.html",
    "Dock Services | M&amp;B Docking | Clear Lake, Iowa",
    "M&B Docking offers dock installation, removal, maintenance, and repair in Clear Lake, Iowa. Free estimates. 5+ years of experience.",
    "services.html",
    services_content,
)
print("Services page built.")

# ============ CONTACT PAGE ============
contact_content = f'''  <main>
    <!-- Contact Hero -->
    <section class="hero" style="padding-block: clamp(var(--space-12), 7vw, var(--space-24));">
      <div class="container hero-content">
        <div class="hero-tag">Get in Touch</div>
        <h1>Let's Get Your <span class="accent">Dock Done Right</span></h1>
        <p>Reach out today for a free, no-obligation estimate. We're always happy to answer any questions about your dock project.</p>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="section">
      <div class="container contact-grid">
        <div class="contact-info">
          <div class="section-kicker">Contact Details</div>
          <h2 class="section-title">Reach M&amp;B Docking</h2>
          <p style="color: var(--color-text-muted); font-size: var(--text-base);">Call or text us, send an email, or use the form. We serve Clear Lake, Iowa and surrounding areas.</p>

          <ul class="contact-details">
            <li>
              <strong>Phone / Text</strong>
              <a href="tel:{PHONE_TEL}">{PHONE}</a>
            </li>
            <li>
              <strong>Email</strong>
              <a href="mailto:{EMAIL}">{EMAIL}</a>
            </li>
            <li>
              <strong>Service Area</strong>
              <span>Clear Lake, Iowa and surrounding areas</span>
            </li>
            <li>
              <strong>Hours</strong>
              <span>Call or text anytime &mdash; we&rsquo;ll respond as soon as we can</span>
            </li>
          </ul>

          <a class="social-link" href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="M&amp;B Docking on Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.53 17.52 2.04 12 2.04S2 6.53 2 12.06c0 5 3.66 9.13 8.44 9.88v-6.99h-2.54v-2.89h2.54V9.85c0-2.51 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.89h-2.34v6.99C18.34 21.19 22 17.06 22 12.06z"/></svg>
            Follow us on Facebook
          </a>
        </div>

        <form class="contact-form" id="contact-form">
          <h3 style="color: var(--color-text); margin-bottom: var(--space-2); font-size: var(--text-lg);">Request a Free Estimate</h3>
          <p style="color: var(--color-text-muted); font-size: var(--text-sm); margin-bottom: var(--space-6);">Fill in your details and we'll reach back out promptly.</p>

          <div class="form-grid">
            <div>
              <label for="name">Your Name *</label>
              <input type="text" id="name" name="name" required placeholder="John Smith" />
            </div>
            <div>
              <label for="phone">Phone Number *</label>
              <input type="tel" id="phone" name="phone" required placeholder="(641) 000-0000" />
            </div>
            <div>
              <label for="email">Email Address</label>
              <input type="email" id="email" name="email" placeholder="john@example.com" />
            </div>
            <div>
              <label for="service">Service Needed</label>
              <select id="service" name="service">
                <option>Dock Installation</option>
                <option>Dock Removal</option>
                <option>Dock Maintenance</option>
                <option>Dock Repair</option>
                <option>Full Seasonal Package</option>
              </select>
            </div>
            <div class="form-wide">
              <label for="location">Property / Location</label>
              <input type="text" id="location" name="location" placeholder="e.g. South Shore, Clear Lake, IA" />
            </div>
            <div class="form-wide">
              <label for="message">Message</label>
              <textarea id="message" name="message" placeholder="Tell us about your dock &mdash; type, length, timeline, any specific needs..."></textarea>
            </div>
            <div class="form-wide">
              <button type="submit" class="btn btn-gold btn-block" style="padding: 16px;">Submit Free Estimate Request</button>
              <div id="form-notice" class="form-notice">
                Opening your email app with your request filled in &mdash; just hit send. If nothing opens, email us directly at {EMAIL}.
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>
  </main>
'''

write_page(
    "contact.html",
    "Contact M&amp;B Docking | Clear Lake, Iowa Dock Service",
    "Contact M&B Docking for dock installation, removal, maintenance, and repair in Clear Lake, Iowa. Call 641-231-2744 or request a free estimate online.",
    "contact.html",
    contact_content,
)
print("Contact page built.")
print("\nAll pages built successfully.")
