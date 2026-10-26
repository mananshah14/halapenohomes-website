# Halapeno Homes — full project context (for Claude Code memory)

Last updated: 28 Sep 2026. Owner: Manan Shah (manan.s@plumhq.com). Working from a Mac ("abcs-macbook-pro-local"), timezone Asia/Kolkata.
Drop this file in as `CLAUDE.md` at the repo root (or `~/.claude/CLAUDE.md`). Everything below was established in one Cowork session that produced three site versions; v3 is current.

---

## 1. The business (facts, not assumptions)

- **Name:** Halapeno Homes (spelled *Halapeno*, not Jalapeno — confirmed by the brand deck).
- **What it is:** curated, premium coliving. Small handpicked homes (a full flat, four residents) for people building a life in a new city.
- **City:** **Ahmedabad only.** The plan is to scale *within* Ahmedabad for now. Never list or hint at other cities on the site.
- **Homes today:** exactly one operating home, but **the website must never say or imply there is only one house.** Copy uses "every Halapeno home", "our homes · Ahmedabad", "same rules, every house", and a "Next home · Ahmedabad · waitlist" entry so it reads as a growing operation without inventing a property.
- **Occupancy model:** co-ed (mixed) homes, **4 residents, twin-sharing** (two single beds per bedroom). Each bedroom has its own bathroom.
- **Pricing:** **never shown on the site.** Enquire on WhatsApp. Copy says pricing is shared once move-in date is known; "no hidden charges".
- **Enquiry channel:** **WhatsApp only** (pre-filled `wa.me` links). No form backend, no email capture forms.
- **Society disclosure:** yes — name **Godrej Green Glades, Godrej Garden City** and show its amenities (owner's decision). Always carry the disclaimer: Godrej Green Glades / Godrej Garden City are projects of Godrej Properties; Halapeno Homes is an independent operator and not affiliated with Godrej; amenities subject to society rules and timings.
- **Logo:** not yet supplied ("will add soon"). Site currently uses a text wordmark. **Tagline:** the deck's tagline slide was image-only and could not be extracted — still unknown.
- **Contact details:** not yet supplied. Placeholders in code: WhatsApp `910000000000`, Instagram `halapenohomes`, email `hello@halapenohomes.com`.

## 2. Brand deck (source of truth — "Green Modern Brand Strategy Presentation", 12 slides)

- **Meaning:** "Halapeno Homes is a curated living space where strangers become friends and a house becomes home, a space that finally feels like ghar."
- **Vision:** "Home isn't a place. It's a feeling and we build it, city after city." (Keep the sentence; do not extrapolate it into listing cities.)
- **Mission:** "To make every person building a life away from home feel like they never left it, no matter which city they move to."
- **Core values (exact wording):** Community First · Curated, Not Crowded · Safety, Non-Negotiable · Premium living.
- **Positioning:** "the antidote to scaled, impersonal coliving: a small, handpicked home for people building a life in a new city, where safety doesn't come with a curfew, and premiumness doesn't come with compromise."
- **Differentiation:** "Halapeno Homes isn't your average coliving setup. It's small, handpicked, and full of character, where strangers turn into your people, not just faceless flatmates. Safety here comes with real freedom, not curfews, and premium living that doesn't ask you to compromise on who you are. Because we're not just renting rooms, we're building a home with a little personality, one that finally feels like ghar."
- **Target audience:** 20–30 years old; working professionals; students of reputed colleges (Nirma University is next door to the home).
- **Colours (the ONLY four allowed):** `#eadccc` cream · `#7c714e` olive · `#543e2c` brown · `#9d8164` tan.
- **Fonts:** Arial MT Pro (text), Helvetica World (headings), Magnolia Script (cursive accent). Web stand-ins: Helvetica Neue/Helvetica → Arial stack; **Pinyon Script** (Google Fonts) stands in for Magnolia Script until the font file is supplied.
- **Voice:** warm, confident, slightly playful, personal; never corporate, never "hostel"/"PG" as a self-description; light Hinglish — "ghar" (home) is the signature word, always set in the script face.

## 3. Owner's standing instructions (in the order they were given)

1. Ask questions before assuming. (He explicitly said "Ask me more questions before assuming.")
2. Olive green is the major colour — the deck's `#7c714e`.
3. Then, stricter: **"keep the colours as per brand deck only"** — no tints/shades invented outside the four (cream at reduced opacity is used for hairlines and secondary text; that was accepted).
4. "Make an out of the box website… take the best plugins… it has to be the best website in the world." He wants craft and motion, not a template.
5. Website cannot say there's only one house.
6. He tried to bring in Superdesign (`@superdesign/cli`) — see §8.
7. Latest brief: a **portal-hero, record-label-style spec** (see §6) — translated into the brand's colours and fonts.

## 4. The property (from the architect's layout PDF + Godrej brochure + photos)

**Address:** Godrej Green Glades, Godrej Garden City, Jagatpur, behind Nirma University, off Sarkhej–Gandhinagar (S.G.) Highway, Ahmedabad 382470. RERA: PR/GJ/AHMEDABAD/AHMEDABAD CITY/AUDA/RAA04138/271118. Tower and floor **unknown** (copy says "a high floor" — that is an assumption; verify or remove).

**Unit (layout by Workshop Inc., "Godrej Garden City – Residence", furniture layout dated 22.08.2026, two options):**
- Bedroom 1: 9'10" × 10'6" — two single beds, wardrobe.
- Toilet 1: 4'2" × 6'10" (attached to Bedroom 1).
- Living & dining: 9'10" × 16'3" — L-shaped sofa, dining table for four; the long wall is the **projector wall**.
- Kitchen: 6'9" × 14' — with fridge.
- Bedroom 2: 9'10" × 13'11" — two single beds, wardrobe.
- Toilet 2: 4'8" × 6'11".
- Washing machine (W.M.) in the wash/utility area.
- Brochure 2BHK "Super Max" carpet area ≈ 615–624 sq ft; site says "~620 sq ft" (reasonable, not confirmed for this unit).

**Society amenities (Godrej Green Glades brochure):** swimming pool, gymnasium, badminton court, basketball court & skating area, box cricket, movie hall, lounge cum library, pool & billiards zone, TT cum board games room, multipurpose hall/room, walking track within the cluster, outdoor fitness, meditation + martial arts court, laughter zone + yoga zone, hammock corner, outdoor reading areas, central greens, fruit orchard, swing grove, pet corner, children's/toddler play areas, community interaction zones, stepped plaza. Specs: vitrified tiles, granite kitchen counter, SS sink, aluminium sliding windows, wall-mounted WC, shower mixer, geyser provision, AC points in all bedrooms and living, DG backup for lifts/common areas, 3 lifts per tower (2 in tower D), gated with security.

**Photos on hand (real, from the owner):**
- `living-before` — the bare flat: white walls, vitrified floor, ceiling fan, black-grill window.
- `living-after` — the finished living room at night: ceiling-mounted projector showing football on the wall, built-in wooden shelving with books and plants, floor lamp, grey sofa with blue cushions, round wooden coffee table, navy bean bag. **Hero image.**
- A third image (minimalist projector on a floating oak shelf, beige room) is a **design mood reference, not the property** — do not present it as a Halapeno home.
- Derived crops in `assets/`: `living-after-hero.jpg`, `living-after.jpg`, `living-before.jpg` (bottom watermark strip cropped off), `detail-shelf.jpg`, `detail-lamp.jpg`, `detail-table.jpg`, and square deck crops `sq-living.jpg`, `sq-before.jpg`, `sq-shelf.jpg`, `sq-lamp.jpg`, `sq-table.jpg`.
- **Missing:** bedroom, kitchen, bathroom and society (pool/gym) photos. Deck/plan slots show honest "photo coming soon" states rather than stock imagery.

## 5. Evidence rules (things that must NOT be invented)

- No fabricated testimonials, reviews, press, ratings, resident counts or "X happy residents". A brand-voice card ("What we're building") replaced an earlier invented quote. Add real quotes only with the resident's permission.
- No prices, no "starting from".
- No other cities, no "coming soon: Mumbai/Pune".
- Bed availability in `CONFIG` (Bed 1 open, Bed 2 taken, Bed 3 open, Bed 4 taken, from 1 Oct 2026) is **sample data, not confirmed by the owner.** Ask before publishing.
- Assumptions currently in copy that the owner has not confirmed: "a high floor"; housekeeping, Wi-Fi and utilities included; "first house dinner is on us" (v2 only); deposit = one month, one-month notice (v2 FAQ only); meals add-on (v2 FAQ only). v3 avoids most of these; keep it that way until confirmed.

## 6. Current design spec — v3 "portal hero" (what is live)

The owner supplied a detailed record-label landing-page spec; it was applied with the brand's palette and fonts substituted for the spec's (spec asked for near-black/amber/teal and Syne/Sora — **rejected**, deck colours/fonts only).

**Palette mapping:** ground = olive `#7c714e`; secondary ground = brown `#543e2c`; ink = cream `#eadccc`; accent = tan `#9d8164` **only on type, dots and rules, never a filled area**; hairlines = `rgba(234,220,204,.16)`; secondary ink = cream at .74 opacity; muted = cream at .5. WhatsApp green is *not* used in v3 (buttons are cream/olive). No gradients as banners, no glows, no drop shadows except on deck cards.

**Type:** display = Helvetica Neue/Helvetica 700, tracking −.02 to −.03em; small type = Arial 10.5–16px, labels uppercase at .14em; script accent = Pinyon Script for "ghar." and single-phrase accents.

**Six sections:**
1. **Portal hero** (`.portal` 250vh, sticky `.stage` 100svh, `isolation:isolate`). Layers back→front: full-bleed photo starting at scale 1.18; duotone wash (olive→tan, `mix-blend-mode:overlay`, opacity 0→.38); radial veil; two solid olive panels (52% wide each) meeting in the middle so the hero starts **closed**; two accent dots at centre; wordmark `<h1 class="mark">` split into `<span>Halapeno</span><span>Homes</span>`; corner metadata pinned to the four corners. On scroll (eased progress `e`): panels translate ±115% (clear the frame), image scale 1.18→1, duotone rises, dots travel to opposite corners (±46vw, ±42vh), wordmark **scales up (≤1.34, capped so it fits the viewport) while letter-spacing tightens (−.02→−.06em) and the halves travel outward ~half their width, clamped to page padding**. Everything is bound to scroll position → fully reversible. Measured: 462px panel travel in the first 700px of scroll; panels return to the exact start pixel.
2. **Statement fold** — outlined index "01" (`-webkit-text-stroke`, transparent fill), label, statement at clamp(24px,3.6vw,52px) over ~22ch with one tan phrase and the script "finally feels like ghar.", circular photo (`.orb`, lamp crop) off the right edge at .42 opacity drifting/rotating with scroll.
3. **Homes** — two columns: headline "Homes with a little *personality.*", lede, "Book a visit" + "See availability", three facts (4 housemates per home · 2+2 bedrooms/bathrooms · 0 curfews); on the right a **throwable card deck** (8 cards: projector lounge, before, shelf, floor-plan type card, lamp, dining, Godrej Green Glades amenities, "Next home, Ahmedabad" waitlist CTA). Pointer capture on `pointerdown`, drag with rotation ∝ dx and slight scale, throw threshold = 10% of deck width, `tabindex=0`, ←/→ keys, `touch-action:pan-y`, progress dots + hint line.
4. **Roster** ("The Halapeno way") — hairline rows: label · display-face name · right-aligned count (Curfew: none · Housemates: handpicked & verified, 4 per home · Rooms: twin-sharing, bath attached, 2+2 · Living: projector wall, 16'3" · Society: gated Godrej, 24×7 · Included: housekeeping, Wi-Fi, utilities · Pricing: shared on WhatsApp, 0 hidden charges).
5. **Availability table** — rendered from `CONFIG.homes[].beds[]`: Home · Room · Bed · Status · From · Enquire link. Second row block = "Next home · Ahmedabad · Waitlist · Join waitlist". Collapses to a 2-col grid per row under 640px with `data-h` headers.
6. **Close** — headline "Come see if it *feels like ghar.*", fine print + Godrej disclaimer, "WhatsApp us" + "Email", hairline footer strip (Instagram · Email · List your flat · Map · ©), then the wordmark full width (JS-fitted to the container), translated down so the page edge crops it.

**Motion rules:** hero/orb bound to scroll (reversible). Entry reveals (`.rv` → `.in`) fire once via IntersectionObserver and never un-reveal; they only exist under `html.js-motion`, added only when `prefers-reduced-motion` is not set, so reduced-motion and no-JS renders are the finished page (verified: fold h2 opacity 1 under reduced motion). No horizontal overflow on 390px (verified).

**Nav:** fixed 58px, translucent olive with 14px backdrop blur and bottom hairline; wordmark 15px with a tan trailing period; uppercase 10.5px links turning tan on hover; availability pill; one cream pill button; burger + full-screen brown menu under 960px.

## 7. Code layout and how to work on it

Workspace in the Cowork session (recreate from the zips if starting fresh):

```
hh3/                          ← v3, CURRENT
  template.html               single source: <title>/meta/<style>/markup/<script>, images as {{IMG:name.jpg}}
  build.py                    → dist/halapeno-artifact.html (images inlined base64, no doctype — for the claude.ai artifact)
                              → dist/halapeno-homes-site/{index.html, assets/, README.md} (deployable)
  test.py                     Playwright checks: panel travel >100px/700px, reversibility, deck arrow keys, reduced-motion, mobile overflow, screenshots
  assets/                     the photos listed in §4
hh2/                          ← v2 (olive cinematic; superseded but has reusable pieces)
  template.html, build.py     GSAP 3.12.5 + ScrollTrigger + Lenis 1.1.18 (vendored in assets/ because CDNs are blocked in the sandbox)
  superdesign/                handoff package for Superdesign (see §8)
hh/                           ← v1 (generic multi-city; obsolete — do not reuse copy)
```

Deliverables sent to the owner: `halapeno-homes-site-v3.zip` (current deploy), `halapeno-homes-site.zip` (v2), `halapeno-superdesign.zip`.
Live preview (claude.ai artifact, same URL across versions, currently v3): https://claude.ai/code/artifact/902423a8-45d6-406e-a018-418d797637d4

**Everything editable lives in the `CONFIG` object at the bottom of `template.html` / `index.html`:**
```js
const CONFIG = {
  whatsapp: "910000000000",            // country code + number, no "+"
  instagram: "halapenohomes",
  email: "hello@halapenohomes.com",
  homes: [
    { code:"HH·01", name:"Godrej Green Glades", area:"Godrej Garden City, Jagatpur", status:"open",
      beds:[ {room:"Bedroom 1",bed:"Bed 1",status:"open",from:"1 Oct 2026"}, {room:"Bedroom 1",bed:"Bed 2",status:"taken",from:""},
             {room:"Bedroom 2",bed:"Bed 3",status:"open",from:"1 Oct 2026"}, {room:"Bedroom 2",bed:"Bed 4",status:"taken",from:""} ] },
    { code:"HH·02", name:"Next home", area:"Ahmedabad", status:"waitlist", beds:[] },
  ],
};
```
Changing a bed's status updates the nav pill, hero corner note, availability label, table and Enquire links. Deck cards are the `CARDS` array in the deck IIFE (square ~900px crops).

**Conventions:** single static HTML, no framework, no build tools beyond `build.py`; everything inlined for the artifact build; CDN-free (sandbox egress blocks cdnjs/jsdelivr — vendor any library into `assets/`); all `<a>` need unique ids and full https/#/mailto hrefs if the page is ever re-imported into Superdesign; run `python3 build.py && python3 test.py` after every change and look at the screenshots.

**Deploy plan (not done yet):** owner will grant access to the Halapeno Homes domain. Static hosting (Netlify / Vercel / Cloudflare Pages or cPanel `public_html`). Add Plausible/GA4, a Google Business Profile for "PG near Nirma University" searches, and an Instagram embed later if wanted.

## 8. Superdesign status

- Owner installed `@superdesign/cli` and logged in **on his Mac** (team "Personal"); the `superdesign` skill is installed at `~/.agents/skills/superdesign` (symlinked for Claude Code).
- The Cowork cloud sandbox **cannot reach `api.superdesign.dev`** (org egress policy → 403), so Claude could not drive the CLI; the Mac folder-access request was also blocked. Fix: an Owner of the Plum-HQ Claude org allowlists `superdesign.dev` + `api.superdesign.dev` under Admin settings → Capabilities; or run from the Mac.
- Handoff package `halapeno-superdesign.zip`: `run.sh` (creates project, uploads 4 photos as brand/reference assets, imports the **v2** draft free of credits; `bash run.sh explore` branches 3 olive directions — spends credits), `halapeno-draft.html` (v2 formatted to Superdesign's draft contract: single root div, ids on every link, images inlined, Tailwind preflight off), `design-system.md` (**describes v2**: olive-dominant with extra tints — update to the §6 four-colour rule before reuse), `assets/`.
- Key CLI facts learned: `create-design-draft` takes ONE `-p`; variations only via `iterate-design-draft --mode branch`; `import-design-draft` is free; `--reference-id` passes image pixels; `extract-website` supersedes `extract-brand-guide`.

## 9. Version history (why things are the way they are)

- **v1** — generic coliving site, 3 cities, 6 fake homes, brown-led. Owner corrected: Ahmedabad only, olive, one house, ask questions first. Obsolete.
- **v2** — olive-led cinematic single page: GSAP hero reveal, parallax, word-by-word manifesto, before/after slider, interactive SVG floor plan with per-bed status, pinned horizontal "Life at Halapeno" gallery, Godrej amenities grid, sticky value cards, comparison table, 4-step process, FAQ, three-tap WhatsApp composer, floating WhatsApp button. Used extra olive tints and WhatsApp green. Owner then said: deck colours only, and the site must not read as single-house. Reusable pieces if wanted later: floor-plan SVG (drawn from the architect's layout), FAQ copy, WhatsApp composer.
- **v3 (current)** — the portal-hero spec in the four deck colours, six sections, copy rewritten to plural "homes" with a waitlist second entry. Verified with Playwright (§6).

## 10. Open items — ask the owner, don't assume

1. WhatsApp business number, Instagram handle, email.
2. Logo file (SVG/PNG) and the tagline from the deck.
3. Real bed availability and move-in date; whether to show availability at all.
4. Photos: both bedrooms, kitchen, bathrooms, society (pool/gym/clubhouse). Square crops for the deck.
5. What's included in rent (housekeeping, Wi-Fi, utilities, laundry, meals?), deposit and notice period — for a future FAQ.
6. Tower/floor of the unit (or drop "high floor").
7. Domain registrar/host details for go-live; whether to use Plausible/GA4.
8. Font files: Magnolia Script, Helvetica World, Arial MT Pro (to replace web stand-ins).
9. Whether to keep Helvetica/Arial or switch to the spec's Syne/Sora (two CSS variables: `--display`, `--sans`).
10. Should Superdesign exploration go ahead (costs credits), and which of the 3 directions if so.
