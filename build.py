#!/usr/bin/env python3
"""Static site generator for meghaldondepradhan.com — writes plain HTML files."""
import os, re, json, datetime

SITE = "https://meghaldondepradhan.com"
NAME = "Meghal Donde Pradhan"
ALT = "Meghal Donde"
EMAIL = "meghal.donde@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/meghal-donde-pradhan/"
GITHUB = "https://github.com/meghaldonde"
YEAR = 2026

# --- SignalCheck status line -------------------------------------------------
# Shown on the homepage feature block and the Independent Projects page.
# Deliberately does not claim shipped, released, or production-ready. Update only when
# a release exists publicly (tag it on GitHub so the claim is verifiable at the source).
SIGNALCHECK_STATUS = "v3 in development &middot; public repository"

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [("/", "Home", "index.html"), ("/projects/", "Independent Projects", "projects/index.html"),
       ("/writing/", "Writing", "writing/index.html"), ("/about/", "About", "about/index.html"),
       ("/contact/", "Contact", "contact/index.html")]

ICON_LI = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 '
           '9h4v12H3zM9 9h3.8v1.71h.05c.53-.95 1.83-1.96 3.77-1.96 4.03 0 4.78 2.5 4.78 5.76V21h-4v-5.6c0-1.34-.03-3.07'
           '-1.9-3.07-1.9 0-2.2 1.46-2.2 2.97V21H9z"/></svg>')
ICON_GH = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5a12 12 0 00-3.79 23.4c.6.11.82-.26.82-.58v-2.2'
           'c-3.34.73-4.04-1.42-4.04-1.42-.55-1.4-1.34-1.77-1.34-1.77-1.09-.75.08-.73.08-.73 1.21.08 1.84 1.24 1.84 '
           '1.24 1.07 1.84 2.81 1.3 3.5 1 .1-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.96 0-1.32.47-2.4 1.24-3.24-'
           '.13-.3-.54-1.52.11-3.18 0 0 1.01-.32 3.3 1.24a11.4 11.4 0 016 0c2.29-1.56 3.3-1.24 3.3-1.24.65 1.66.24 '
           '2.88.12 3.18.77.84 1.23 1.92 1.23 3.24 0 4.63-2.8 5.65-5.48 5.95.43.37.82 1.1.82 2.22v3.29c0 .32.21.7.82'
           '.58A12 12 0 0012 .5z"/></svg>')
EXT = ('<span class="ext" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 '
       '01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/></svg></span>')
ARR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def head(title, desc, path, extra_ld="", og_type="website"):
    canon = SITE + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="author" content="{NAME}">
<meta name="robots" content="index, follow, max-image-preview:large">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{NAME} — Product, AI, Data and User Experience">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{extra_ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
'''


def header(active):
    CUR = ' aria-current="page"'
    links = "".join(
        f'<li><a href="{h}"{CUR if h == active else ""}>{lbl}</a></li>'
        for h, lbl, _ in NAV)
    social = (f'<div class="nav-social">'
              f'<a href="{LINKEDIN}" rel="me noopener" target="_blank" aria-label="{NAME} on LinkedIn">{ICON_LI}</a>'
              f'<a href="{GITHUB}" rel="me noopener" target="_blank" aria-label="{NAME} on GitHub">{ICON_GH}</a>'
              f'</div>')
    return f'''<header class="site-header" id="siteHeader">
  <nav class="wrap nav" aria-label="Primary">
    <a class="brand" href="/">{NAME}</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navMenu">Menu</button>
    <div class="nav-menu" id="navMenu">
      <div class="wrap">
        <ul class="nav-links">{links}</ul>
        {social}
      </div>
    </div>
  </nav>
</header>
<main id="main">
'''


def footer():
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="footer-name">{NAME}</p>
        <p>Product &middot; AI &middot; Data &middot; User Experience</p>
      </div>
      <div>
        <ul class="footer-links">
          <li><a href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn</a></li>
          <li><a href="{GITHUB}" rel="me noopener" target="_blank">GitHub</a></li>
          <li><a href="mailto:{EMAIL}">Email</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
        <p class="footer-note">Earlier publications may appear under {ALT}.</p>
      </div>
    </div>
    <p class="footer-legal">&copy; {YEAR} {NAME}</p>
  </div>
</footer>
<script>
(function () {{
  var t = document.querySelector('.nav-toggle'), m = document.getElementById('navMenu');
  if (t && m) t.addEventListener('click', function () {{
    var open = m.classList.toggle('is-open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
    t.textContent = open ? 'Close' : 'Menu';
  }});
  var h = document.getElementById('siteHeader');
  if (h) {{
    var onScroll = function () {{ h.classList.toggle('is-stuck', window.scrollY > 8); }};
    onScroll();
    window.addEventListener('scroll', onScroll, {{ passive: true }});
  }}
}})();
</script>
</body>
</html>
'''


# ---------------------------------------------------------------- structured data
# NOTE — when the Global Cyber Alliance role ends:
#   1. Change the GCA entry in EXPERIENCE from "Oct 2021 – Present" to a closed date range.
#   2. Remove the "worksFor" block from PERSON_LD below (or replace it with the new employer),
#      so the site stops asserting GCA as a current employer.
#   3. Update "jobTitle" in PERSON_LD to match.
# Writing & Research entries do not change — published work stays attributed either way.
PERSON_LD = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "{SITE}/#person",
  "name": "{NAME}",
  "alternateName": ["{ALT}"],
  "givenName": "Meghal",
  "additionalName": "Donde",
  "familyName": "Pradhan",
  "url": "{SITE}/",
  "image": "{SITE}/assets/portrait.jpg",
  "email": "mailto:{EMAIL}",
  "jobTitle": "Senior Software Engineer, Data Management & Analytics",
  "description": "Works across product, AI, data, and user experience — AI product workflows, data products, analytics, and the user-facing decision experiences built on them. Applied in cybersecurity and internet measurement. Earlier public work published under the name {ALT}.",
  "knowsAbout": ["Product management", "AI product workflows", "Data products", "Analytics", "User experience design for data products", "Dashboards and decision interfaces", "Cybersecurity data", "Trust and abuse measurement", "Evaluation of AI systems"],
  "worksFor": {{ "@type": "Organization", "name": "Global Cyber Alliance", "url": "https://globalcyberalliance.org/" }},
  "alumniOf": [
    {{ "@type": "CollegeOrUniversity", "name": "Boston University Questrom School of Business" }},
    {{ "@type": "CollegeOrUniversity", "name": "University of Mumbai" }}
  ],
  "address": {{ "@type": "PostalAddress", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "US" }},
  "sameAs": [
    "{LINKEDIN}",
    "{GITHUB}",
    "https://medium.com/@meghal.donde",
    "https://globalcyberalliance.org/team/meghal-donde/"
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{SITE}/#website",
  "url": "{SITE}/",
  "name": "{NAME}",
  "alternateName": "{ALT}",
  "inLanguage": "en-US",
  "publisher": {{ "@id": "{SITE}/#person" }},
  "about": {{ "@id": "{SITE}/#person" }}
}}
</script>'''


def breadcrumb_ld(label, path):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "{label}", "item": "{SITE}{path}" }}
  ]
}}
</script>'''


# ---------------------------------------------------------------- content data
WRITING = [
    dict(year="2026", date="2026-04-02", human="2 April 2026", feature=True,
         title="Cyberattacks on France Are Rising—Here’s What the AIDE Data Shows",
         url="https://globalcyberalliance.org/cyberattacks-on-france-are-rising-heres-what-the-aide-data-shows/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="A threefold rise in attacks against French networks, a Mirai-linked outbound surge from French infrastructure, and where the traffic originates."),
    dict(year="2025", date="2025-12", human="December 2025", feature=True,
         title="Salt Typhoon Across the Internet: What AIDE Honeypots Reveal About a Persistent State-Linked Campaign",
         url="https://globalcyberalliance.org/wp-content/uploads/2025/12/PUBLIC-REPORT-Salt-Typhoon-Across-the-Internet.pdf",
         pub="Global Cyber Alliance", byline=ALT, kind="Full Report",
         ctx="Two years of telecom-decoy telemetry examined against the Salt Typhoon espionage campaign, with mitigation recommendations for network operators."),
    dict(year="2025", date="2025-12-09", human="9 December 2025",
         title="New Report: Salt Typhoon Across the Internet",
         url="https://globalcyberalliance.org/new-report-salt-typhoon-across-the-internet/",
         pub="Global Cyber Alliance", byline=ALT, kind="Announcement Post",
         ctx="The launch post introducing the report and its headline findings."),
    dict(year="2025", date="2025-09-05", human="5 September 2025", feature=True,
         title="Dark Pink APT Campaigns Through the Lens of AIDE Telemetry",
         url="https://globalcyberalliance.org/aide-data-darkpink/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="Attack sessions targeting government, defense, and education organizations across Southeast Asia and APAC, including command-and-control via webhook abuse."),
    dict(year="2025", date="2025-09-04", human="4 September 2025",
         title="AIDE Uncovers RedTail: Persistent Cryptomining with APT Tactics",
         url="https://globalcyberalliance.org/aide-data-redtail/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="A six-month, 25-country cryptomining campaign traced through honeypot data, and the tactical overlaps that made it look like something else."),
    dict(year="2025", date="2025-09-03", human="3 September 2025",
         title="Tracking Kimsuky: North Korean Espionage Operations in GCA’s AIDE",
         url="https://globalcyberalliance.org/aide-data-kimsuky/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="Two years of reconnaissance activity in AIDE telemetry, including a distinctive user-agent signature and linked login attempts."),
    dict(year="2025", date="2025-08-28", human="28 August 2025",
         title="AIDE Data on APT36: Regional Infrastructure Risks and Security Gaps",
         url="https://globalcyberalliance.org/aide-data-apt36/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="Detected incidents mapped across regional autonomous systems, paired with an analysis of routing-security gaps (RPKI, IRR, MANRS)."),
    dict(year="2025", date="2025-05-12", human="12 May 2025",
         title="Catching Flax Typhoon in the Honeypot: Footprints in AIDE",
         url="https://globalcyberalliance.org/flax-typhoon-aide/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="VPN tunnelling, web shells, and living-off-the-land binaries surfacing in honeypot data, concentrated against Taiwan-based sensors."),
    dict(year="2024", date="2024-03-14", human="14 March 2024",
         title="Tracing Volt Typhoon: Insights from GCA’s AIDE Honey Farm",
         url="https://globalcyberalliance.org/tracing-volt-typhoon-insights-from-gcas-aide-honey-farm/",
         pub="Global Cyber Alliance", byline=ALT,
         ctx="Measuring how much of the published indicator set actually appeared in sensor data, and what end-of-life router exploitation looked like up close."),
    dict(year="2026", date="2026-05-29", human="29 May 2026", feature=True,
         title="Recurrence Is Not Persistence: Why Repeated Signals Can Mislead Data Teams",
         url="https://medium.com/@meghal.donde/recurrence-is-not-persistence-why-repeated-signals-can-mislead-data-teams-76bfc5872f2b",
         pub="Medium", byline=NAME, kind="Essay",
         ctx="A repeated signal on a dashboard is not evidence that a problem is ongoing. Three questions worth asking about concentration, confounds, and corroboration before an engineering team acts on one."),
]

PROJECTS = [
    dict(
        slug="signalcheck", tag="AI Product · Independently Created",
        title="SignalCheck — A Trust Score for What You’re Reading",
        summary="A browser extension and API that combine domain reputation with AI-generated-content detection into a single, explainable trust score. Built end to end, outside of any employer.",
        meta=["Chrome Extension (MV3)", "FastAPI", "Google Safe Browsing", "Gemini", "Evaluation", "Human review"],
        links=[("https://carpal-gum-931.notion.site/SignalCheck-AI-Digital-Provenance-Trust-Extension-3b9eb84ed72681aa90c6e5fe5e84801d",
                "Read the product thinking", True),
               ("https://github.com/meghaldonde/trustsignalcheck", "View the repository", False)],
        facts=[("Role", "Product &middot; Design &middot; Builder"),
               ("Context", "Built end to end, outside of any employer"),
               ("Status", SIGNALCHECK_STATUS)],
        problem="Domain reputation and AI-content detection answer different questions and live in different tools. A reader deciding whether to trust a page has to hold both in their head, and neither signal means much alone.",
        role="Product &middot; Design &middot; Builder. I framed the problem, designed the scoring model and system boundaries, and built it. Independent work, outside of any employer.",
        work=["Manifest V3 Chrome extension with a FastAPI backend.",
              "Fuses Google Safe Browsing reputation with Gemini AI-content detection into one 0–100 Signal Trust Score.",
              "The score surfaces inline as the reader browses, with the contributing signals shown separately rather than hidden behind the number.",
              "An admin view tracks scoring behavior across requests, which is how the weighting gets tuned."],
        outcome="A working prototype and a public repository, plus a written account of how the score is composed, where the two signals disagree, and which judgments stay with the reader.",
        ai_boundaries=["The score prompts a closer look. It is not a verdict, and it is not a moderation decision.",
                       "AI-content detection is probabilistic. It is never presented as proof of authorship.",
                       "Low-confidence results display as low-confidence rather than rounding to a clean number.",
                       "Where reputation and content signals disagree, the disagreement is shown rather than averaged away."],
    ),
]

EXPERIENCE = [
    dict(when="Oct 2021 – Present",
         role="Senior Software Engineer, Data Management &amp; Analytics",
         org="Global Cyber Alliance",
         note="Co-Chair, Domain Trust Data Working Group",
         contributions=[
             ("", "Built and evolved large-scale cybersecurity data and analytics systems processing 3M+ daily events across 200+ sensors."),
             ("", "Defined measurement, scoring, data, and product requirements across AIDE Internet Pollution Index and Domain Trust work."),
             ("", "Reduced AWS OpenSearch cost by 40% and improved query performance by 28% through index, shard, and storage design changes."),
             ("", "Worked with research institutions, registries, registrars, and other partners to translate user needs into data access, reporting, and product improvements."),
         ]),
    dict(when="2017 – 2018",
         role="Co-owner &amp; Lead Software Developer",
         org="Pinac Solutions",
         body="Industrial software, HMI and analytics work."),
    dict(when="2007 – 2012",
         role="Head of Software Development",
         org="On-site Analysis",
         body="Engineering leadership and platform modernization."),
]

EARLIER_NOTE = "Earlier roles across healthcare, industrial automation, edtech, and software engineering."

CRED_GROUPS = [
    ("Business &amp; Strategy", [
        ("MBA", "Boston University Questrom School of Business", ""),
        ("Beta Gamma Sigma", "Top 20% of graduating class", ""),
    ]),
    ("Engineering Foundation", [
        ("Master of Computer Applications", "University of Mumbai", ""),
        ("B.S., Computer Science", "University of Mumbai", ""),
    ]),
    ("AI &amp; Product", [
        ("Certified Scrum Product Owner", "Scrum Alliance", ""),
        ("Google AI Professional Certificate", "Google", ""),
        ("Building AI-Powered Systems", "Anthropic", ""),
        ("Advanced Google Analytics", "Google", ""),
    ]),
]

HERO_CREDS = ["MBA, BU Questrom", "MCA + BS Computer Science",
              "Certified Scrum Product Owner", "Google AI Professional",
              "Anthropic AI Systems"]

CONSULT_AREAS = [
    ("AI product strategy", "Framing what a model should and should not decide, and designing the workflow around it."),
    ("Data products &amp; analytics", "Measurement frameworks, analytical data models, and reporting people actually use."),
    ("Cybersecurity data &amp; measurement", "Turning high-volume security telemetry into analysis that supports decisions."),
    ("Evaluation &amp; decision workflows", "Evidence handling, uncertainty, and where human review belongs."),
]


# ---------------------------------------------------------------- helpers
def featured_project(pr):
    facts = "".join(f'<div class="pf-fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pr["facts"])
    tags = "".join(f"<li>{m}</li>" for m in pr["meta"][:4])
    EXTA = ' rel="noopener" target="_blank"'
    parts = []
    for u, lbl, _primary in pr["links"]:
        # on the homepage the case study is the primary action; these are supporting
        ext = EXTA if u.startswith("http") else ""
        parts.append(f'<a class="btn btn-secondary" href="{u}"{ext}>{lbl}</a>')
    btns = "".join(parts)
    return f'''      <article class="feature">
        <p class="work-tag">{pr["tag"]}</p>
        <h3><a href="/projects/#{pr["slug"]}">{pr["title"]}</a></h3>
        <p class="feature-lede">{pr["lede_short"]}</p>
        <dl class="pf-facts">{facts}</dl>
        <ul class="case-meta">{tags}</ul>
        <div class="btn-group">
          <a class="btn btn-primary" href="/projects/#{pr["slug"]}">Read the case study {ARR}</a>
          {btns}
        </div>
      </article>'''


SHORTS = {
    "signalcheck": dict(
        lede_short="Two imperfect signals about a web page — domain reputation and AI-generated-content detection — combined into one explainable 0–100 trust score, with the disagreements between them left visible. Built end to end, outside of any employer."),
}
for p in PROJECTS:
    p.update(SHORTS[p["slug"]])


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]


def writing_item(w, show_ctx=True, lvl=3):
    kind = w.get("kind", "Article")
    ctx = f'<p class="writing-context">{w["ctx"]}</p>' if show_ctx else ""
    return f'''      <li id="{slugify(w["title"])}">
        <div class="writing-item">
          <p class="writing-year"><time datetime="{w["date"]}">{w["human"]}</time></p>
          <div>
            <h{lvl} class="writing-title"><a href="{w["url"]}" rel="noopener" target="_blank">{w["title"]}{EXT}</a></h{lvl}>
            <p class="writing-meta"><span>{w["pub"]}</span><span aria-hidden="true">&middot;</span><span>{kind}</span><span aria-hidden="true">&middot;</span><span>{w["year"]}</span></p>
            <p class="writing-byline">{w.get("bylabel", "Published as " + w["byline"])}</p>
            {ctx}
          </div>
        </div>
      </li>'''


def write(fn, html):
    dest = os.path.join(OUT, fn)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fn, f"({len(html.encode()):,} bytes)")


# ================================================================ INDEX
def build_index():
    cards = "\n".join(featured_project(pr) for pr in PROJECTS)
    writing = "\n".join(writing_item(w) for w in WRITING if w.get("feature"))
    def tl_item(e):
        contrib = ""
        if e.get("contributions"):
            if all(not k for k, _ in e["contributions"]):
                rows = "".join(f"<li>{v}</li>" for _, v in e["contributions"])
                contrib = f'<ul class="contrib-plain">{rows}</ul>'
            else:
                rows = "".join(f'<div class="contrib"><dt>{k}</dt><dd>{v}</dd></div>'
                               for k, v in e["contributions"])
                contrib = f'<dl class="contrib-list">{rows}</dl>'
        note = f'<p class="tl-note">{e["note"]}</p>' if e.get("note") else ""
        body = f'<p class="tl-body">{e["body"]}</p>' if e.get("body") else ""
        return f'''      <li>
        <p class="tl-when">{e["when"]}</p>
        <div>
          <p class="tl-role">{e["role"]}</p>
          <p class="tl-org">{e["org"]}</p>
          {note}
          {body}
          {contrib}
        </div>
      </li>'''

    tl = "\n".join(tl_item(e) for e in EXPERIENCE)
    BADGE = ('<img class="cred-badge" src="/assets/cspo-badge.png" width="240" height="240" '
             'alt="Scrum Alliance Certified Scrum Product Owner badge" decoding="async">')

    def cred_col(title, items):
        out = []
        for n, w, y in items:
            where = w + (" &middot; " + y if y else "")
            if n.startswith("Certified Scrum Product Owner"):
                out.append(f'<li class="cred-badged">{BADGE}<span>'
                           f'<span class="cred-name">{n}</span>'
                           f'<span class="cred-where">{where}</span></span></li>')
            else:
                out.append(f'<li><span class="cred-name">{n}</span>'
                           f'<span class="cred-where">{where}</span></li>')
        rows = "".join(out)
        return (f'      <div class="cred-col">\n        <h3>{title}</h3>\n'
                f'        <ul>{rows}</ul>\n      </div>')

    creds = "\n".join(cred_col(t, items) for t, items in CRED_GROUPS)
    hero_creds = "".join(f"<li>{c}</li>" for c in HERO_CREDS)
    areas = "".join(f'<div class="consult-area"><h3>{t}</h3><p>{d}</p></div>' for t, d in CONSULT_AREAS)

    html = head(
        f"{NAME} | Product, AI, Data &amp; User Experience",
        "Meghal Donde Pradhan — product, AI, data, and user experience. Data and AI products, decision workflows, and cybersecurity measurement. Earlier work published as Meghal Donde.",
        "/", PERSON_LD)
    html += header("/")
    html += f'''<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1>{NAME}</h1>
      <p class="hero-kicker">Product<span aria-hidden="true">&middot;</span>AI<span aria-hidden="true">&middot;</span>Data<span aria-hidden="true">&middot;</span>User Experience</p>
      <p class="hero-lede">I build data and AI products that turn complex information into useful decisions &mdash; with evidence, trust, and human judgment built in.</p>
      <div class="btn-group">
        <a class="btn btn-primary" href="/projects/">View Projects {ARR}</a>
        <a class="btn btn-secondary" href="/writing/">Read My Work</a>
      </div>
      <ul class="hero-creds">{hero_creds}</ul>
    </div>
    <div class="hero-portrait">
      <img src="/assets/portrait.jpg" srcset="/assets/portrait-sm.jpg 560w, /assets/portrait.jpg 1000w" sizes="(max-width: 860px) 340px, 40vw" width="1000" height="1250" alt="Portrait of {NAME}" fetchpriority="high" decoding="async">
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2-marked">Independent projects</h2>
      <p>Products and experiments I conceived, designed, and built independently, outside of employer work.</p>
    </div>
{cards}
  </div>
</section>

<section id="writing" class="section-tint">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Writing &amp; Research</p>
      <h2>Published analysis</h2>
      <p>Threat-actor research, internet measurement analysis, and essays on working with data. Earlier pieces carry the byline {ALT}.</p>
    </div>
    <ol class="writing-list">
{writing}
    </ol>
    <p style="margin-top:1.75rem"><a class="link-arrow" href="/writing/">All writing and research</a></p>
  </div>
</section>

<section id="about">
  <div class="wrap-narrow">
    <p class="eyebrow">About</p>
    <h2>Professional story</h2>
    <p>I work across product, AI, data, and user experience, turning technical systems and complex datasets into interfaces and workflows people can actually make decisions with. Much of that work has been in cybersecurity and internet measurement.</p>
    <p>My background spans software engineering, analytics, data products, partner-facing work, and 0&rarr;1 product definition. More recently, I have been focusing on AI product workflows, evaluation, evidence, uncertainty, and human review.</p>
    <blockquote class="pullquote">The useful question is rarely what a model can predict. It is what someone is supposed to do next.</blockquote>
    <p>Earlier professional publications and public work may appear under the name {ALT}.</p>
    <p style="margin-top:1.5rem"><a class="link-arrow" href="/about/">More about my background</a></p>
  </div>
</section>

<section id="credentials" class="section-tint">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Credentials</p>
      <h2>Engineering depth, business training, current AI practice</h2>
      <p>The three things the work above depends on. I came up through computer science rather than into product from the side, and the AI credentials are recent by design.</p>
    </div>
    <div class="cred-grid">
{creds}
    </div>
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Professional Experience</p>
      <h2>Where I have worked</h2>
      <p>Selected contributions, not a full career history. Employer programs are described only in terms of my contributions.</p>
    </div>
    <ol class="timeline">
{tl}
    </ol>
    <p class="earlier-note">{EARLIER_NOTE}</p>
  </div>
</section>

<section id="consulting" class="consult">
  <div class="wrap">
    <p class="eyebrow">Consulting &amp; Collaboration</p>
    <h2>Available for selected engagements</h2>
    <p style="max-width:56ch">Available for selected engagements involving AI product strategy, data products and analytics, cybersecurity data, and decision workflows.</p>
    <div class="consult-grid">{areas}</div>
    <div class="btn-group">
      <a class="btn btn-primary" href="/contact/">Discuss a Project {ARR}</a>
    </div>
  </div>
</section>
'''
    html += footer()
    write("index.html", html)


# ================================================================ PROJECTS
def build_projects():
    cases = []
    for pr in PROJECTS:
        meta = "".join(f"<li>{m}</li>" for m in pr["meta"])
        facts = "".join(f'<div class="pf-fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pr["facts"])
        parts = []
        for u, lbl, primary in pr["links"]:
            cls = "btn-primary" if primary else "btn-secondary"
            arrow = " " + ARR if primary else ""
            parts.append(f'<a class="btn {cls}" href="{u}" rel="noopener" target="_blank">{lbl}{arrow}</a>')
        btns = "".join(parts)
        work = "".join(f"<li>{x}</li>" for x in pr["work"])
        bounds = "".join(f"<li>{x}</li>" for x in pr["ai_boundaries"])
        cases.append(f'''<section class="case" id="{pr["slug"]}">
  <div class="wrap">
    <div class="case-head">
      <p class="eyebrow">{pr["tag"]}</p>
      <h2>{pr["title"]}</h2>
      <p class="case-summary">{pr["summary"]}</p>
      <dl class="pf-facts">{facts}</dl>
      <ul class="case-meta">{meta}</ul>
      <div class="btn-group">{btns}</div>
    </div>

    <div class="case-body">
      <div class="case-block">
        <h3>The problem</h3>
        <p>{pr["problem"]}</p>
      </div>
      <div class="case-block">
        <h3>My role</h3>
        <p>{pr["role"]}</p>
      </div>
      <div class="case-block">
        <h3>What it does</h3>
        <ul class="tight">{work}</ul>
      </div>
      <div class="case-block">
        <h3>What it deliberately does not do</h3>
        <ul class="tight">{bounds}</ul>
      </div>
    </div>

    <div class="case-outcome">
      <h3>Outcome</h3>
      <p>{pr["outcome"]}</p>
    </div>
  </div>
</section>''')

    html = head(f"Independent Projects by {NAME}",
                "Independent projects by Meghal Donde Pradhan, including SignalCheck — a browser extension and API scoring web page trustworthiness with AI and domain reputation.",
                "/projects/",
                breadcrumb_ld("Independent Projects", "/projects/") + "\n" + f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "{SITE}/projects/#collection",
  "url": "{SITE}/projects/",
  "name": "Independent projects by {NAME}",
  "isPartOf": {{ "@id": "{SITE}/#website" }},
  "about": {{ "@id": "{SITE}/#person" }},
  "mainEntity": {{
    "@type": "SoftwareSourceCode",
    "@id": "{SITE}/projects/#signalcheck",
    "name": "SignalCheck",
    "description": "A Chrome extension and FastAPI service that combine domain reputation with AI-generated-content detection into a single explainable 0-100 trust score.",
    "codeRepository": "https://github.com/meghaldonde/trustsignalcheck",
    "programmingLanguage": ["Python", "JavaScript"],
    "runtimePlatform": "Chrome Extension (Manifest V3), FastAPI",
    "author": {{ "@id": "{SITE}/#person" }},
    "creator": {{ "@id": "{SITE}/#person" }},
    "inLanguage": "en-US"
  }}
}}
</script>''')
    html += header("/projects/")
    html += f'''<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Independent Projects</p>
    <h1>Independent projects</h1>
    <p class="lede">Products and experiments I conceived, designed, and built independently, outside of employer work. Work done for employers is described under <a href="/#experience">experience</a>, and published research under <a href="/writing/">writing</a>.</p>
  </div>
</section>
''' + "\n".join(cases)
    html += footer()
    write("projects/index.html", html)


def publications_ld():
    """CreativeWork entries authored by the Person and hosted elsewhere.

    This asserts authorship of external works; it does NOT claim the articles are
    hosted on this site (no Article type, no local mainEntityOfPage)."""
    items = []
    for i, w in enumerate(WRITING, 1):
        ctype = "Report" if "report" in w.get("kind", "").lower() else "Article"
        items.append({
            "@type": "ListItem",
            "position": i,
            "item": {
                "@type": ctype,
                "@id": f"{SITE}/writing/#{slugify(w['title'])}",
                "headline": w["title"],
                "name": w["title"],
                "url": w["url"],
                "datePublished": w["date"],
                "inLanguage": "en",
                "abstract": w["ctx"],
                "author": {
                    "@type": "Person",
                    "@id": f"{SITE}/#person",
                    "name": NAME,
                    "alternateName": w["byline"],
                },
                "publisher": {"@type": "Organization", "name": w["pub"]},
                "isAccessibleForFree": True,
            },
        })
    ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": f"{SITE}/writing/#collection",
        "url": f"{SITE}/writing/",
        "name": f"Writing and research by {NAME}",
        "description": (f"Complete index of articles and reports authored by {NAME}. "
                        f"Work published at the Global Cyber Alliance carries the byline {ALT}."),
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#person"},
        "author": {"@id": f"{SITE}/#person"},
        "mainEntity": {
            "@type": "ItemList",
            "name": f"Publications by {NAME}",
            "numberOfItems": len(WRITING),
            "itemListOrder": "https://schema.org/ItemListOrderDescending",
            "itemListElement": items,
        },
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(ld, indent=2, ensure_ascii=False) + "\n</script>")


# ================================================================ WRITING
def build_writing():
    items = "\n".join(writing_item(w, lvl=2) for w in WRITING)
    html = head(f"Writing &amp; Research by {NAME}",
                "Ten articles and reports by Meghal Donde Pradhan: threat-actor research and internet measurement for the Global Cyber Alliance, published as Meghal Donde.",
                "/writing/", breadcrumb_ld("Writing", "/writing/") + "\n" + publications_ld())
    html += header("/writing/")
    html += f'''<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Writing &amp; Research</p>
    <h1>Published articles and reports</h1>
    <p class="lede">Cybersecurity threat-actor research, internet measurement analysis, and essays on working with data, written for network operators, researchers, and practitioners. Earlier professional publications may appear under the name {ALT}.</p>
  </div>
</section>

<section style="padding-top:0;border-top:0">
  <div class="wrap">
    <ol class="writing-list">
{items}
    </ol>
    <div class="callout" style="margin-top:2.5rem">
      <p><strong>To add:</strong> any further Medium essays, talks, panels, or conference appearances you want indexed here. Send the links and they slot straight into this list. Delete this box before publishing.</p>
    </div>
  </div>
</section>
'''
    html += footer()
    write("writing/index.html", html)


# ================================================================ ABOUT
def build_about():
    html = head(f"About {NAME}",
                "About Meghal Donde Pradhan: product, AI, data, and user experience in Boston. Engineering, analytics, and AI product work. Earlier work published as Meghal Donde.",
                "/about/",
                breadcrumb_ld("About", "/about/") + "\n" + f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "@id": "{SITE}/about/#profilepage",
  "url": "{SITE}/about/",
  "name": "About {NAME}",
  "isPartOf": {{ "@id": "{SITE}/#website" }},
  "mainEntity": {{ "@id": "{SITE}/#person" }},
  "about": {{ "@id": "{SITE}/#person" }},
  "inLanguage": "en-US"
}}
</script>''',
                og_type="profile")
    html += header("/about/")
    html += f'''<section class="page-header">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">About</p>
      <h1>Meghal Donde Pradhan</h1>
      <p class="lede">I work across product, AI, data, and user experience, turning technical systems and complex datasets into interfaces and workflows people can actually make decisions with. Much of that work has been in cybersecurity and internet measurement.</p>
    </div>
    <div class="hero-portrait">
      <img src="/assets/portrait.jpg" srcset="/assets/portrait-sm.jpg 560w, /assets/portrait.jpg 1000w" sizes="(max-width: 860px) 340px, 34vw" width="1000" height="1250" alt="Portrait of {NAME}" decoding="async">
    </div>
  </div>
</section>

<section style="padding-top:var(--space-l)">
  <div class="wrap-narrow">
    <h2>How the work has evolved</h2>
    <p>I started in software engineering, building enterprise systems and learning platforms, and spent the early part of my career leading development teams and modernizing the systems underneath them. What kept pulling my attention was not the code so much as the reporting layer on top of it: who was reading it, what decision it was meant to support, and how often it failed at that.</p>
    <p>That interest moved me into data and analytics, then into industrial telemetry and healthcare data, where the gap between a working system and a usable one is very visible. An operator standing at a machine does not want a data feed; they want to know whether something is about to go wrong.</p>
    <p>At the Global Cyber Alliance I have worked on cybersecurity data products, where the same problem appears at internet scale. Millions of daily attack events are only worth collecting if someone can act on what they show. That has meant building the pipelines, but also co-developing the measurement models, defining what counts and what does not, and writing up the analysis for people who need to make decisions with it.</p>
    <p>More recently my focus has been AI product work: evaluation, evidence handling, uncertainty, and human review. My background spans software engineering, analytics, data products, partner-facing work, and 0&rarr;1 product definition.</p>
    <p>Earlier professional publications and public work may appear under the name {ALT}.</p>

    <blockquote class="pullquote">Millions of daily events are only worth collecting if someone can act on what they show.</blockquote>

    <h2>What I am working on now</h2>
    <p>AI product workflows and the parts of them that are easy to skip: how a system handles evidence, what it does when it is uncertain, how you evaluate whether it is actually working, and where a person needs to stay in the loop. My independent project <a href="/projects/#signalcheck">SignalCheck</a> is a working exercise in exactly that &mdash; combining two imperfect signals into one score without pretending the result is a verdict.</p>
    <p>I co-chair the Domain Trust Data Working Group, which brings registries, registrars, DNS providers, and academic partners to a shared measurement standard, and I write up threat-actor and internet-measurement analysis for public audiences.</p>

    <h2>Background</h2>
    <p>Based in Boston, Massachusetts. MBA from Boston University&rsquo;s Questrom School of Business, where I graduated in the top 20% of my class and was inducted into Beta Gamma Sigma. Master of Computer Applications and a BS in Computer Science, both from the University of Mumbai. Certified Scrum Product Owner, with recent certificates in Google AI Professional and Anthropic&rsquo;s Building AI-Powered Systems.</p>
    <p>Outside of work I have volunteered with public school programs, running Python coding sessions and programming workshops, and contributed to open-source projects.</p>

    <div class="btn-group">
      <a class="btn btn-primary" href="/contact/">Get in touch {ARR}</a>
      <a class="btn btn-secondary" href="/writing/">Read my writing</a>
    </div>
  </div>
</section>
'''
    html += footer()
    write("about/index.html", html)


# ================================================================ CONTACT
def build_contact():
    areas = "".join(f'<div class="consult-area"><h3>{t}</h3><p>{d}</p></div>' for t, d in CONSULT_AREAS)
    html = head(f"Contact {NAME}",
                "Contact Meghal Donde Pradhan about product, AI, and data roles, consulting in AI product strategy and cybersecurity data, or writing and speaking.",
                "/contact/",
                breadcrumb_ld("Contact", "/contact/") + "\n" + f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "@id": "{SITE}/contact/#contactpage",
  "url": "{SITE}/contact/",
  "name": "Contact {NAME}",
  "isPartOf": {{ "@id": "{SITE}/#website" }},
  "mainEntity": {{ "@id": "{SITE}/#person" }},
  "inLanguage": "en-US"
}}
</script>''')
    html += header("/contact/")
    html += f'''<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Get in touch</h1>
    <p class="lede">The best way to reach me is by email. I&rsquo;m happy to hear about relevant roles, consulting engagements, writing, speaking, or collaboration.</p>
  </div>
</section>

<section style="padding-top:0;border-top:0">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-primary">
        <p class="contact-label">Email</p>
        <p class="contact-email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <ul class="contact-links">
          <li><a href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn{EXT}</a></li>
          <li><a href="{GITHUB}" rel="me noopener" target="_blank">GitHub{EXT}</a></li>
          <li><a href="https://medium.com/@meghal.donde" rel="me noopener" target="_blank">Medium{EXT}</a></li>
        </ul>
        <p class="contact-loc">Boston, Massachusetts</p>
      </div>
      <div class="contact-notes">
        <div class="contact-note">
          <h2>Opportunities</h2>
          <p>Open to senior product, AI, and data roles. I maintain tailored materials for product management and data/analytics roles &mdash; tell me which opportunity you&rsquo;re considering and I&rsquo;ll share the most relevant version.</p>
        </div>
        <div class="contact-note">
          <h2>Writing and speaking</h2>
          <p>Happy to talk about internet measurement, trust and abuse data, user experience for data products, or evaluating AI systems in production. My published work is on the <a href="/writing/">writing page</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="consult">
  <div class="wrap">
    <p class="eyebrow">Consulting &amp; Collaboration</p>
    <h2>Available for selected engagements</h2>
    <p style="max-width:58ch">Available for selected engagements involving AI product strategy, data products and analytics, cybersecurity data, and decision workflows.</p>
    <div class="consult-grid">{areas}</div>
    <div class="btn-group">
      <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Project%20enquiry">Discuss a Project {ARR}</a>
    </div>
  </div>
</section>
'''
    html += footer()
    write("contact/index.html", html)


# ================================================================ 404 / sitemap / robots
def build_extras():
    html = head(f"Page not found | {NAME}",
                "That page could not be found on meghaldondepradhan.com. Browse the projects, writing, about, or contact pages instead.",
                "/404")
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                        '<meta name="robots" content="noindex, follow">')
    html = html.replace('<link rel="canonical" href="' + SITE + '/404">\n', '')
    html += header("")
    html += f'''<section class="page-header">
  <div class="wrap-narrow">
    <p class="eyebrow">404</p>
    <h1>That page could not be found</h1>
    <p class="lede">The link may be out of date. Try the projects, writing, or about pages.</p>
    <div class="btn-group">
      <a class="btn btn-primary" href="/">Back to home {ARR}</a>
      <a class="btn btn-secondary" href="/writing/">Writing</a>
    </div>
  </div>
</section>
'''
    html += footer()
    write("404.html", html)

    today = "2026-08-13"
    urls = [("/", "1.0", "monthly"), ("/projects/", "0.9", "monthly"), ("/writing/", "0.9", "monthly"),
            ("/about/", "0.8", "yearly"), ("/contact/", "0.7", "yearly")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, pr, cf in urls:
        sm += f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n"
    sm += "</urlset>\n"
    write("sitemap.xml", sm)

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="8" fill="#14283D"/>'
           '<text x="32" y="44" font-family="Manrope,Inter,Helvetica,sans-serif" font-size="34" font-weight="700" '
           'fill="#FAFAF7" text-anchor="middle">M</text>'
           '<rect x="14" y="50" width="36" height="2" fill="#B58D4A"/></svg>')
    with open(os.path.join(OUT, "assets", "favicon.svg"), "w") as f:
        f.write(fav)
    print("wrote assets/favicon.svg")


if __name__ == "__main__":
    build_index(); build_projects(); build_writing(); build_about(); build_contact(); build_extras()
    print("\nDone.")
