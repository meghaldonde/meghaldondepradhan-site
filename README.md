# meghaldondepradhan.com

Personal site for Meghal Donde Pradhan. Positioning: **Product · AI · Data · User Experience**,
with cybersecurity as a domain where that work has been applied — not as a primary identity label.
Plain static HTML, one shared stylesheet, no build step, no JavaScript framework.

**There is deliberately no resume page.** The site is the stable professional profile; tailored
resumes are application documents sent directly, per role.

---

## What's here

```
index.html              Home
projects/index.html     Independent Projects (SignalCheck)
writing/index.html      Publication index (10 items)
about/index.html        Professional story
contact/index.html      Contact + consulting
404.html                Not-found page (noindex)
assets/
  site.css              The entire design system
  portrait.jpg          Hero portrait (1000×1250)
  portrait-sm.jpg       Mobile portrait (560×700)
  og-image.jpg          Social preview card (1200×630)
  cspo-badge.png        Scrum Alliance CSPO badge (rendered inline at 62px)
  favicon.svg
sitemap.xml
robots.txt
netlify.toml            Netlify config (headers + caching)
build.py                Regenerates the HTML from content data
```

### Previewing locally

Pages use root-relative links (`/writing/`), so `file://` won't resolve them. Run a server:

```
python3 -m http.server 8000
```

### Editing

Either edit the HTML directly — they're plain files, nothing will break — or edit `build.py` and
re-run `python3 build.py`. All content lives in Python lists near the top: `WRITING`, `PROJECTS`,
`SHORTS`, `EXPERIENCE`, `EARLIER_NOTE`, `CRED_GROUPS`, `HERO_CREDS`, `CONSULT_AREAS`. Re-running
overwrites the HTML, so don't mix the two approaches on the same page.

---

## Before you publish

| # | Item | Where |
|---|------|-------|
| 1 | Delete the dashed **"To add"** box | `writing/index.html`, bottom of the list |
| 2 | Confirm the domain is right | `build.py` line 5, `SITE = ...` |
| 3 | Update `SIGNALCHECK_STATUS` once v3 is actually released (and tag it on GitHub) | `build.py` |
| 4 | Open the Notion product-thinking link in a private window | see below |
| 5 | Read the SignalCheck case study and the GCA contributions once for accuracy | `projects/index.html`, `index.html` |

### The Notion link

The SignalCheck case study and homepage card both link to your Notion product-thinking page. **I
could not verify it renders for a logged-out visitor** — the sandbox this was built in can't reach
`notion.site`. Notion pages are private by default, and this is the one supporting link on your
only independent project. Open it in a private/incognito window before launch.

### The SignalCheck status line

One constant near the top of `build.py`:

```python
SIGNALCHECK_STATUS = "v3 in development &middot; public repository"
```

Deliberately does not say shipped, released, or production-ready. Update it only once a release
exists publicly, and tag it on GitHub at the same time so the claim is verifiable at the source.

Nothing on the site claims users, adoption, or production deployment.

---

## The five things the site does, and where

This separation is the whole structure. Worth preserving if you edit later.

| Section | Answers | Contains |
|---|---|---|
| Independent Projects | What she builds | Only work she owns outright. SignalCheck today. |
| Writing & Research | What she has authored | Publications under her byline, including GCA work |
| Professional Experience | What she contributed | Employer programs, framed as contributions |
| Credentials | The foundation behind it | Degrees and certifications, grouped as evidence |
| Consulting | How to engage her | Four focus areas, one CTA |

### Employer work vs. her own

- **Independent Projects** contains nothing employer-owned. A build check fails if "AIDE",
  "Domain Trust", or "Internet Pollution Index" appear on that page.
- **Professional Experience** is where AIDE and Domain Trust live, as four contribution bullets
  under the GCA role. The section intro states the programs are the employer's. Pinac Solutions
  and On-site Analysis get one line each; everything older is a single summary sentence.
- **Writing & Research** keeps the GCA articles, because those are published under her byline.

Figures used: 3M+ daily events, 200+ sensors, 40% cost reduction, 28% query improvement — all at
the level already public in her reports. No partner names, contract detail, or internal figures.

One figure worth a second look: the TPM resume says **50M+ daily events** where the more recent
data resume says **3M+**. The site uses **3M+**, the conservative number.

### Credentials

Two touchpoints:

- **`HERO_CREDS`** — one-line strip under the hero buttons. Always seen, low weight.
- **`CRED_GROUPS`** — three columns (Business & Strategy / Engineering Foundation / AI & Product)
  after Professional Story, with a framing line. The grouping is the argument: engineering depth,
  business training, and current AI practice, as evidence for the three-part hero positioning
  rather than a flat list of eight equal things.

One Scrum Alliance CSPO badge sits inline beside the CSPO entry at 62px, so it reads as part of
that credential rather than floating at the column foot. Deliberately the only badge on the site —
adding more turns an editorial section into a badge wall. CSPO is shown as completed; no
"expected" language appears anywhere.

---

## Deploying

### GitHub Pages — read this carefully

**Use a user site, not a project site.** Create a repo named exactly **`meghaldonde.github.io`**
and push this folder's contents to its default branch. The site then serves from the domain root,
which every link and canonical URL assumes.

A normal project repo (`github.com/meghaldonde/website`) serves at `/website/` and **every
root-relative link breaks** — stylesheet, portrait, nav. A custom domain avoids this entirely.

1. Create the repo `meghaldonde.github.io` (public).
2. Push everything here to `main`.
3. Settings → Pages → Source: *Deploy from a branch*, `main`, `/ (root)`.
4. `.nojekyll` is included, which stops Jekyll from ignoring files and folders.
5. Custom domain: Settings → Pages → Custom domain → `meghaldondepradhan.com`, tick *Enforce
   HTTPS*. GitHub writes the `CNAME` file. (`CNAME.example` is here rather than a real `CNAME`,
   because committing one before DNS is pointed makes Pages serve nothing.)
6. DNS — four `A` records for the apex: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
   `185.199.111.153`, plus a `CNAME` for `www` → `meghaldonde.github.io`.

### Netlify

Drag this folder onto [app.netlify.com/drop](https://app.netlify.com/drop) or connect a Git repo.
`netlify.toml` is configured. Clean URLs work automatically.

### Domain handling

- `SITE` in `build.py` is set to **non-www**. Canonical tags follow it. Change that one line and
  rebuild if you prefer www, then redirect the other.
- If you own `meghaldonde.com`, **301 it** to the primary domain. Don't run a second site there —
  a duplicate splits the search signal you're consolidating.

### After launch

1. Add the property in [Google Search Console](https://search.google.com/search-console), submit
   `https://meghaldondepradhan.com/sitemap.xml`.
2. URL Inspection on the homepage and About, request indexing.
3. Test the social card with the LinkedIn [Post Inspector](https://www.linkedin.com/post-inspector/).
4. Validate structured data at [validator.schema.org](https://validator.schema.org/).

---

## When the Global Cyber Alliance role ends

Do this before the change becomes public, so the site never asserts a stale employer. There is a
matching reminder comment above `PERSON_LD` in `build.py`.

1. **`EXPERIENCE`** — change the GCA entry's `when` from `"Oct 2021 – Present"` to a closed range,
   e.g. `"Oct 2021 – Mar 2027"`.
2. **`PERSON_LD`** — delete the `"worksFor"` block, or replace it with the new employer. Leaving it
   means search engines and AI systems keep reporting GCA as where she works now.
3. **`PERSON_LD`** — update `"jobTitle"` to match the new role.
4. Re-run `python3 build.py`.

**Writing & Research does not change.** Published work stays attributed regardless of employment —
the bylines are historical fact, not a current-employer claim. Same for the Professional Experience
contributions; they just move into past tense by virtue of the closed date range.

---

## SEO

Everything on-page is done. What is here:

- **Distinct, name-first titles** on all five pages, each under 62 characters so nothing truncates.
- **Meta descriptions** at 146–161 characters, each leading with the full name.
- **`Person` + `WebSite`** structured data on the homepage — the canonical entity, with
  `alternateName` carrying "Meghal Donde".
- **`ProfilePage`** on About and **`ContactPage`** on Contact, both with `mainEntity` pointing at
  that same Person `@id`. This is what tells a crawler these pages are *about* one person rather
  than being five unrelated documents.
- **`CollectionPage` + `ItemList`** on Writing, declaring all ten works as authored by her with
  real publishers, dates, and external URLs — authorship of work hosted elsewhere, without
  claiming the articles live here.
- **`CollectionPage` + `SoftwareSourceCode`** on Independent Projects for SignalCheck, with
  `codeRepository` pointing at the public repo.
- **`BreadcrumbList`** on every inner page, canonical URLs everywhere, sitemap, robots.txt,
  descriptive alt text, semantic headings with no level skips.

**What this can realistically achieve.** Ranking for *your name* is winnable, and this site is
built to win it — a well-structured personal site on a matching domain is usually the strongest
candidate for a person-name query. Expect weeks, not days: a brand-new domain has no history, and
Google needs to crawl, index, and build confidence.

**What it cannot do.** You will not outrank globalcyberalliance.org for "Salt Typhoon report" or
Medium for the essay title. Those domains have years of authority and host the actual articles.
That is the correct outcome and not worth fighting. The win condition is that someone searching
"Meghal Donde Pradhan" or "Meghal Donde" lands here and sees the whole body of work at once.

**The three things that will move the needle more than anything on this page**, in order:

1. **Reciprocal links.** `sameAs` is a one-way claim until the other end agrees. Put
   `meghaldondepradhan.com` in your LinkedIn contact info, your GitHub profile website field, and
   your Medium bio. If GCA will add it to your staff bio page, that is the strongest of the four —
   it is the domain your publications already sit on.
2. **Search Console.** Submit the sitemap, then use URL Inspection on the homepage and About to
   request indexing directly. This is the difference between being found in days versus weeks.
3. **Publishing.** Each new piece under "Meghal Donde Pradhan", linked from the writing page,
   compounds the association between the name and the work. One essay a quarter beats any
   technical tweak available on this site.

Do not buy links, add hidden keyword text, or stuff name variants into the markup. Search is
case-insensitive, so "meghal donde" and "Meghal Donde" are already the same query — adding case
variants would read as spam and risk the thing you are trying to build.

---

## Name continuity

Handled quietly, but functional. Don't delete these:

- **`Person` structured data** carries `"name": "Meghal Donde Pradhan"` and
  `"alternateName": ["Meghal Donde", ...]` — the machine-readable claim that both are one person.
- **`sameAs`** links LinkedIn, GitHub, Medium, and the GCA staff page to that Person entity.
- **The writing page** prints each byline as published — nine *Published as Meghal Donde*, one
  *Meghal Donde Pradhan* — with `CollectionPage` + `ItemList` structured data declaring all ten as
  authored works hosted elsewhere. That asserts authorship without claiming the articles live
  here, which is the line Google penalises people for crossing.
- **One sentence** in Professional Story and a quiet footer line. No dedicated section.

The highest-leverage thing left is external: `sameAs` is a one-way claim until the other end
agrees. Add `meghaldondepradhan.com` to the LinkedIn contact info, GitHub profile website field,
and Medium bio.

---

## Design system

Tokens at the top of `assets/site.css`.

| Role | Hex | Use |
|---|---|---|
| Deep navy | `#14283D` | Headings, nav, footer, consulting band |
| Muted teal | `#2F6F73` | Accents, rules, bullets |
| Teal deep | `#245659` | Link text (the AA-contrast variant) |
| Warm ivory | `#FAFAF7` | Page background |
| Ivory warm | `#F4F3ED` | Alternating section tint |
| Charcoal | `#22252A` | Body copy |
| Cool gray | `#66707A` | Metadata, dates, captions |
| Muted brass | `#B58D4A` | Section ticks, active nav underline, pull-quote rule |

Manrope for headings, Inter for body, from Google Fonts with a system fallback. Source Serif 4 for
the pull quote only. To drop the Google Fonts dependency, delete the `fonts.googleapis.com` link
from each `<head>` — the fallback stack renders cleanly.

### Accessibility

- Every text/background pair on all five pages passes WCAG AA at its rendered size, verified with
  alpha compositing rather than declared colors.
- One `<h1>` per page, no heading-level skips.
- Skip link is the first tab stop; visible focus rings throughout.
- Mobile menu has working `aria-expanded`; nav marks the current page with `aria-current`.
- Decorative glyphs are `aria-hidden`; icon links have `aria-label`; the badge has real alt text.
- Respects `prefers-reduced-motion`. Content renders with JavaScript disabled.

---

## Not built

- **A second independent project.** `PROJECTS` and both layouts scale to more without changes.
- **Project screenshots or diagrams.** A SignalCheck screenshot would strengthen that page.
- **More writing.** Add entries to `WRITING` and re-run.
