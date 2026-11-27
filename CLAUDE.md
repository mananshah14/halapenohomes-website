# Halapeno Homes — full project context (for Claude Code memory)

Last updated: 28 Sep 2026. Owner: Manan Shah (manan.s@plumhq.com). Working from a Mac ("abcs-macbook-pro-local"), timezone Asia/Kolkata.
Drop this file in as `CLAUDE.md` at the repo root (or `~/.claude/CLAUDE.md`). Everything below was established in one Cowork session that produced three site versions; v3 is current.

---

## 1. The business (facts, not assumptions)

- **Name:** Halapeno Homes (spelled *Halapeno*, not Jalapeno — confirmed by the brand deck).
- **What it is:** curated, premium coliving. Small handpicked homes (a full flat, four residents) for people building a life in a new city.
- **City:** **Ahmedabad only.** The plan is to scale *within* Ahmedabad for now. Never list or hint at other cities on the site.
- **Homes today:** exactly one operating home, but **the website must never say or imply there is only one house.** Copy uses "every Halapeno home", "our homes · Ahmedabad", "same rules, every house", and a "Next home · Ahmedabad · waitlist" entry so it reads as a growing operation without inventing a property.
- **Occupancy model:** co-ed (mixed) homes, 4 residents, twin-sharing (two single beds per bedroom). Each bedroom has its own bathroom. **Do not write "twin-sharing" on the website** (owner, 25 Nov 2026) — say "two bedrooms, bath attached"; the availability table may still list Bed 1–4.
- **Pricing:** **never shown on the site.** Enquire on WhatsApp. Copy says pricing is shared once move-in date is known; "no hidden charges".
- **Enquiry channel:** **WhatsApp only** (pre-filled `wa.me` links). No form backend, no email capture forms.
- **Society disclosure:** **do NOT name the society or flat on the website** (owner reversed this on 25 Nov 2026 — "remove the flat name"). Then "not TMI on the flat name and all" (same day): no room dimensions, no map link. FINAL rule (25 Nov 2026, last word): **"Do not put any name of the society"** — no Godrej, no Green Glades, no Garden City anywhere on the site. The location may be given as "S.G. Highway, Ahmedabad" only. Home name in CONFIG is "S.G. Highway". The Godrej disclaimer was removed with the name. Amenities may still be listed generically. Keep the line that Halapeno is an independent operator and amenities are subject to the society's rules. The society name (Godrej Green Glades, Godrej Garden City) stays in this file for internal reference and in the Customer Service Agreement, not on the site.
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
- **Fonts (updated 26 Oct 2026):** the brand typeface is **Chillax** (Manushi Parikh / Indian Type Foundry, free via Fontshare) — owner supplied the six static weights (200–700). Feedback on 25 Nov 2026: "too many fonts" → the site now uses exactly two faces and two weights: Chillax 600 (headings, wordmark, buttons) and Chillax 400 (body, labels), plus Pinyon Script only for "ghar."-style accents. Only `chillax-regular.woff2` and `chillax-semibold.woff2` ship; the other four weights were removed from `assets/fonts/`, one `@font-face` family "Chillax" declared at the top of `src/template.html`. The deck's Helvetica/Arial are now fallbacks only. The cursive accent ("ghar.") still uses **Pinyon Script** (Google Fonts) as a stand-in for the deck's Magnolia Script until that file is supplied.
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

## 4b. Meeting feedback applied 26 Nov 2026 (14 points)
Hero: only "Ahmedabad" top-left and "Scroll to open" bottom-right; no availability pill, no "curated coliving", no "handpicked housemates · no curfew", no bottom-left location/beds line. Fold: dashes replaced by commas; "small" removed; wording "handpicked homes inside gated societies, where safety has no curfew and premium has no compromise". Our homes: no "wall of books", no projector wall in copy; use "ambient lighting, curated furniture", socialising/networking, personality; only two facts (4 housemates per flat · 2+2); second button is "What's included" → #roster. "The Halapeno way": "per flat" not "per home"; Living = "A projector wall" (the flat does have one); Society row (gated, pool & gym · clubhouse access) separate from a new Security row (Biometric lock & CCTV · 24×7); Included = "Housekeeping & Wi-Fi" (NO utilities — not provided); Pricing = "A predefined contract, no surprises · 0 surprise increments". **Availability section removed entirely** (and the beds data with it; CONFIG.homes is now just code/name/area). Unchanged on purpose: "Book a visit" and the independent-operator disclaimer. Open: the Curfew row's right-hand label — "come & go freely" is a placeholder the meeting did not settle; "List your flat" footer link (a WhatsApp prompt for flat owners who want Halapeno to run their flat) — purpose unconfirmed.

## 4c. Photos of the real flat + "Step inside" hero (27 Nov 2026)
Owner sent 18 photos and two 6-second clips of the actual flat (tower/flat number visible on the door sign in two shots — cropped out; never show it). It is the ONLY home (POC); the projector living room on the site is the design that this flat's living room is being finished to. Usable: bedroom symmetrical day (curtains open), day (curtains closed), night with cove lighting (hero), entrance with backlit round mirror (lit and dark versions), door open, wardrobe + floating shelves, dining with green cane chairs. Not usable yet: kitchen (mop/towels), bathroom (broom), living room (boxes). Pillows still in plastic and labels visible in bedroom shots — a reshoot checklist was given (tripod spots, plastic off, labels off, living room from the boxes-photo position, lights-on evening shots, corridor and door-opening frames).
**REVERTED the same day** — owner: "looks shit and pictures are cropped" (portrait phone photos crop badly as full-bleed desktop frames). The portal hero with the projector living room is back and must stay until there are landscape, tripod-shot photos. The step-inside idea is parked; notes kept for reference: it was a 400vh (300svh mobile) sticky stage with four full-bleed frames bound to scroll — door (wordmark grows/tightens/splits over it, caption "Lock clicks.") → entrance mirror ("The mirror lights up.") → bedroom by day ("Your room, by day.") → evening falls (dusk veil to ~0.96) → **Lights on** (night frame revealed under the dark, warm glow bloom, caption "Lights on. You're home."). Day and night frames are not pixel-aligned (different distance), which is why the swap happens under full dusk. Reversible; reduced-motion shows the night frame static. Frames: `assets/hero-door.jpg` (cropped to remove the sign), `hero-mirror.jpg`, `hero-day.jpg`, `hero-night.jpg`.
Also added: **Before/after** section (`#ba`, drag wipe, settles to 46% on first view) using the bare-flat photo vs the projector living-room design, captioned "Living room · finishing now"; a **phone-framed 12-second loop** (`assets/walk.mp4`, both clips stitched, muted/autoplay/loop/playsinline, poster `walk-poster.jpg`) under the facts in Homes; deck re-cut to 9 cards (bed night, entrance, bed day, floor-plan card, dining, wardrobe, living room design, gated society, next-home waitlist). The fold's floating orb now uses the entrance crop. `build.py` handles `{{VID:name}}` (relative path for deploy, base64 data URI for the artifact).

## 4d. v5 — research-led upgrade (27 Nov 2026)
Owner asked to "go to the internet and figure out the best ways to make this the world's best website in this space" and to edit the photos. Research (Cohabs, Outsite, Stanza Living, Zolo; Common and Settl unreachable) → recurring patterns: a feeling-led hero promise; a numbered enquiry→move-in path; "what's included" in plain words (Cohabs "All included", Zolo's four-row "Your Stay. Your Way." panel); named-member proof (NOT usable — no invented quotes); scale numbers and press rows (NOT usable — none real); one verb-led CTA repeated; location as search key (NOT usable — no location detail); the operator's own tools as trust (lock, support). Anti-patterns avoided: scale counts, city grids, discount banners, persona testimonials, link directories.
Applied, all from the owner's own Customer Service Agreement draft (so FLAG to the owner if the terms change): **"Your stay, your way"** panel (`#way`): share a room or take one; 11-month term, 3-month minimum, 30 days' notice, rent fixed for the term; biometric lock with a personal access code, deactivated on move-out; support 10–7 on working days, emergencies any hour. **Included / paid at actuals** two-column list under the roster (Wi-Fi, housekeeping of common areas, maintenance coordination, lock access, society amenities vs electricity share, LPG, cook/house-help if wanted, society move-in charges, refundable deposit). **Four steps** (`#steps`, "No brokers in between" — says no brokers, does not promise a timeline). **FAQ** (`#faq`, six answers drawn only from the agreement and owner statements; guest hours deliberately unspecified; pets not permitted per Schedule 1). **WhatsApp composer** in the Close (who · when · visit / video walk-through / terms first → pre-filled message). **Mobile sticky CTA bar** (≤640px: Book a visit + The terms; body gets bottom padding). **OG share image** `assets/og-image.jpg` (1200×630, wordmark set in Chillax from the WOFF2 + the night bedroom) + canonical + twitter card — matters for WhatsApp link previews. Nav now: Homes · Terms · Included · FAQ · Contact. Deck images lazy-load.
Photo edits made in code (OpenCV): AC brand/energy stickers inpainted out of both bedroom shots; gentle warm LAB grade (+4–6 b, 1.04 contrast) on all five deck squares; squares re-cut. Pillow plastic and the mattress label are NOT removable by inpainting — reshoot needed.

## 4e. v6 — Niraj Mehta review applied (27 Nov 2026)
Owner relayed a review meeting (Niraj Mehta); every point below was approved by the owner and is now live. Do not undo any of it without asking.
- **Headers brighter, bigger, catchier.** All h2 now set in full cream `#eadccc` (no tan/muted phrases inside headings) and ~20% larger: fold clamp(30px,4.6vw,68px); gallery/FAQ clamp(34px,4.6vw,64px); "Tell us what we missed." and the close clamp(38px,5.4vw,80px).
- **Fold:** the opening line stays word for word ("A curated living space where strangers become friends and a house becomes home, a space that *finally feels like ghar.*"); the paragraph under it was removed.
- **Homes:** "Homes with a little personality." replaced by **"After a long day, sometimes all you want is a little privacy, a moment of quiet, and a space that feels like *yours.*"** followed by the bold underlined link **"Come experience it yourself."** → `#book`. The facts strip and the small phone-loop video were dropped from this section; the throwable card deck stays.
- **Gallery** (`#gallery`, new nav tab): the full-house walk-through video goes here, never as a small screen on the home page. Until the owner's friend delivers the film, `walk.mp4` (the two WhatsApp clips) plays there with controls, labelled "Full house walk-through · coming soon". Layout: portrait video sticky on the left, nine full-frame photos (`assets/g-*.jpg`, AC labels inpainted, warm grade, door-sign cropped, **no square crops**) in a 2-col grid on the right, closing with a "See it for yourself → Book a viewing" tile. JS reads the video's real aspect on `loadedmetadata`; a landscape film automatically switches `.gbody.wide` (video full-width above a 3-col grid). To swap in the final film: replace `assets/walk.mp4` + `walk-poster.jpg`, rebuild.
- **Removed:** the before/after "shell to home" slider (`#ba`), the "Your stay, your way" terms panel (`#way`), the four-step "from hello to move-in" (`#steps`), and the three-tap WhatsApp composer in the close.
- **Amenities → "Tell us what we missed."** (`#missed`): h2, then "What's the one thing you wish your last place had?", then "We've thought about what makes everyday life easier in a shared home. Take a look at what's included, then come see it for yourself." Two boxes: **What's included** (`<details id="included">`, click to expand: the eight roster rows + In the rent / Paid at actuals + nothing else) and **Book a viewing** (`#book`, form: name · phone/WhatsApp number · how (In person / On a live video call / Send me the walk-through video) → opens WhatsApp with a pre-filled message; no backend, nothing stored).
- Nav: Gallery · What's included · Contact (FAQ tab removed with the section); nav button and mobile sticky bar: "Book a viewing" (→ `#book`) + "Gallery". The close (heading, disclaimer, WhatsApp/Email, footer, bigmark) is unchanged; the FAQ was removed afterwards ("for now").
- Direction from the meeting to keep applying: the site should feel **personal and lavish**; "the first page carries the whole brand".

## 5. Evidence rules (things that must NOT be invented)

- No fabricated testimonials, reviews, press, ratings, resident counts or "X happy residents". A brand-voice card ("What we're building") replaced an earlier invented quote. Add real quotes only with the resident's permission.
- No prices, no "starting from".
- No other cities, no "coming soon: Mumbai/Pune".
- Availability was removed from the site (26 Nov 2026). Never show bed status again without the owner supplying real data.
- Assumptions currently in copy that the owner has not confirmed: "a high floor"; housekeeping, Wi-Fi and utilities included; "first house dinner is on us" (v2 only); deposit = one month, one-month notice (v2 FAQ only); meals add-on (v2 FAQ only). v3 avoids most of these; keep it that way until confirmed.

## 6. Current design spec — v3 "portal hero" (what is live)

The owner supplied a detailed record-label landing-page spec; it was applied with the brand's palette and fonts substituted for the spec's (spec asked for near-black/amber/teal and Syne/Sora — **rejected**, deck colours/fonts only).

**Palette mapping:** ground = olive `#7c714e`; secondary ground = brown `#543e2c`; ink = cream `#eadccc`; accent = tan `#9d8164` **only on type, dots and rules, never a filled area**; hairlines = `rgba(234,220,204,.16)`; secondary ink = cream at .74 opacity; muted = cream at .5. WhatsApp green is *not* used in v3 (buttons are cream/olive). No gradients as banners, no glows, no drop shadows except on deck cards.

**Type:** Chillax throughout — display 600 at tracking −.02 to −.03em; small type 400 at 10.5–16px; uppercase labels 500 at .14em; outlined index 700 (Chillax has no 800). Script accent = Pinyon Script for "ghar." and single-phrase accents.

**Sections, in order (v6, live):** hero → fold → homes+deck → gallery → tell-us-what-we-missed (included box + viewing form) → close. (FAQ removed 27 Nov 2026 at the owner's request — "remove questions section for now"; the six answers are in git history at commit 811cb1c if wanted back.)
1. **Portal hero** (reinstated 27 Nov 2026 after a one-day step-inside experiment, see §4c) (`.portal` 250vh on desktop, **150svh under 960px**, sticky `.stage` 100svh, `isolation:isolate`). Layers back→front: full-bleed photo (the projector living room, `living-after-hero.jpg`) starting at scale 1.18; duotone wash (olive→tan, `mix-blend-mode:overlay`, opacity 0→.38); radial veil; two solid olive panels (52% wide each) meeting in the middle so the hero starts **closed**; two accent dots at centre; wordmark `<h1 class="mark">` split into `<span>Halapeno</span><span>Homes</span>`; corner metadata = "Ahmedabad" top-left and "Scroll to open" bottom-right only. On scroll (eased progress `e`): panels translate ±115%, image scale 1.18→1, duotone rises, dots travel to opposite corners, wordmark scales up (≤1.34) while letter-spacing tightens and the halves travel outward, clamped to page padding. Everything is bound to scroll position → fully reversible.
2. **Statement fold** — outlined index "01", label "What Halapeno Homes means", the opening line only (see §4e), circular photo (`.orb`, entrance) off the right edge drifting with scroll.
3. **Homes** — label "Our homes · Ahmedabad", the privacy headline + "Come experience it yourself." link (§4e); on the right the **throwable card deck** (two-way: drag/swipe left or → = next, right or ← = previous; dots clickable; `tabindex=0`; `touch-action:pan-y`). 9 cards: bedroom night · entrance · bedroom day · floor-plan type card "Two rooms. Four people." · dining · wardrobes · living room ("Finishing now — this is the design") · "A gated society" type card · "Next home, Ahmedabad." waitlist CTA.
4. **Gallery** — see §4e.
5. **Tell us what we missed** — see §4e. Roster rows inside the box: Curfew "come & go freely" (placeholder wording, owner to confirm) · Housemates handpicked & verified, 4 per flat · Rooms two bedrooms, bath attached, 2+2 · Living a projector wall · Society gated, pool & gym, clubhouse access · Security biometric lock & CCTV, 24×7 · Included housekeeping & Wi-Fi, in the rent · Pricing a predefined contract, 0 surprise increments.
6. **Close** — headline "Come see if it *feels like ghar.*", the independent-operator disclaimer (fixed wording, do not change), "WhatsApp us" + "Email", footer strip (Instagram · Email · List your flat · ©), then the wordmark full width (JS-fitted, never cropped).

**Motion rules:** hero/orb bound to scroll (reversible). Entry reveals (`.rv` → `.in`) fire once via IntersectionObserver and never un-reveal; they only exist under `html.js-motion`, added only when `prefers-reduced-motion` is not set, so reduced-motion and no-JS renders are the finished page (verified: fold h2 opacity 1 under reduced motion). No horizontal overflow on 390px (verified).

**Nav:** fixed 58px, translucent olive with 14px backdrop blur and bottom hairline; wordmark 15px with a tan trailing period; uppercase 10.5px links (Gallery · What's included · Contact) turning tan on hover; one cream pill button "Book a viewing" → `#book`; burger + full-screen brown menu under 960px; ≤640px a fixed bottom bar (Book a viewing · Gallery).

## 7. Code layout and how to work on it

Repo: https://github.com/mananshah14/halapenohomes-website (public, branch `main`, GitHub Pages deploy-from-branch at root, `CNAME` = halapenohomes.com, Cloudflare DNS — see `DEPLOY.md`). Live: https://halapenohomes.com. Claude.ai preview artifact (same URL every version): https://claude.ai/code/artifact/902423a8-45d6-406e-a018-418d797637d4

```
index.html            built output — DO NOT hand-edit; regenerated by src/build.py
assets/               fonts/ (Chillax 400 + 600 WOFF2), hero + deck squares (sq-*.jpg), gallery full-frames (g-*.jpg),
                      walk.mp4 + walk-poster.jpg, og-image.jpg, living-after/before.jpg
src/template.html     THE single source: <title>/meta/<style>/markup/<script>; images as {{IMG:name.jpg}}, video as {{VID:name.mp4}}
src/build.py          → index.html (relative asset paths) and src/dist/halapeno-artifact.html (everything base64-inlined, no doctype, for the artifact)
src/test.py           Playwright checks (older; the quick loop below is what was used for v5/v6)
CNAME, .nojekyll, README.md, DEPLOY.md, CLAUDE.md
```

**Loop for every change:** edit `src/template.html` → `python3 src/build.py` → serve the repo over `python3 -m http.server` and run Playwright (Chromium) at 1440×900 and 390×844: no page errors (file:// font CORS and the blocked Google-Fonts tunnel are sandbox noise), `scrollWidth === clientWidth`, every `a[href^="#"]` resolves, all `.rv` end up `.in`, the viewing form opens `wa.me/<CONFIG.whatsapp>?text=…`, and look at the screenshots → commit → push → republish the artifact from `src/dist/halapeno-artifact.html`. `src/dist/` and `*.png` are git-ignored.

**Everything editable lives in the `CONFIG` object at the bottom of `src/template.html`:**
```js
const CONFIG = {
  whatsapp: "910000000000",   // placeholder — owner has not supplied the number yet
  instagram: "halapenohomes",
  email: "hello@halapenohomes.com",
  homes: [ { code:"HH·01", name:"S.G. Highway", area:"Ahmedabad" }, { code:"HH·02", name:"Next home", area:"Ahmedabad" } ],
};
```
Deck cards are the `CARDS` array in the deck IIFE (square ~900px crops in `assets/sq-*.jpg`). Gallery photos are plain `<figure>`s in `#gallery`. All WhatsApp links come from `data-wa="message"` attributes wired to `CONFIG.whatsapp`; the viewing form builds its own message.

**Conventions:** single static HTML, no framework, no build tools beyond `build.py`; CDN-free (sandbox egress blocks cdnjs/jsdelivr — vendor anything into `assets/`); Chillax 400/600 only + Pinyon Script (Google Fonts) for script accents; four brand colours only; never name the society or the flat; no prices; never say there is only one home.

**Pushing from a Claude session:** the owner supplies a GitHub token in chat; use it only as an `http.extraheader` on the push command (never write it to git config), and remind the owner to revoke it afterwards. The GitHub REST API is blocked through the sandbox proxy; `git push` to github.com works.

## 8. Superdesign status

- Owner installed `@superdesign/cli` and logged in **on his Mac** (team "Personal"); the `superdesign` skill is installed at `~/.agents/skills/superdesign` (symlinked for Claude Code).
- The Cowork cloud sandbox **cannot reach `api.superdesign.dev`** (org egress policy → 403), so Claude could not drive the CLI; the Mac folder-access request was also blocked. Fix: an Owner of the Plum-HQ Claude org allowlists `superdesign.dev` + `api.superdesign.dev` under Admin settings → Capabilities; or run from the Mac.
- Handoff package `halapeno-superdesign.zip`: `run.sh` (creates project, uploads 4 photos as brand/reference assets, imports the **v2** draft free of credits; `bash run.sh explore` branches 3 olive directions — spends credits), `halapeno-draft.html` (v2 formatted to Superdesign's draft contract: single root div, ids on every link, images inlined, Tailwind preflight off), `design-system.md` (**describes v2**: olive-dominant with extra tints — update to the §6 four-colour rule before reuse), `assets/`.
- Key CLI facts learned: `create-design-draft` takes ONE `-p`; variations only via `iterate-design-draft --mode branch`; `import-design-draft` is free; `--reference-id` passes image pixels; `extract-website` supersedes `extract-brand-guide`.

## 9. Version history (why things are the way they are)

- **v1** — generic coliving site, 3 cities, 6 fake homes, brown-led. Owner corrected: Ahmedabad only, olive, one house, ask questions first. Obsolete.
- **v2** — olive-led cinematic single page: GSAP hero reveal, parallax, word-by-word manifesto, before/after slider, interactive SVG floor plan with per-bed status, pinned horizontal "Life at Halapeno" gallery, Godrej amenities grid, sticky value cards, comparison table, 4-step process, FAQ, three-tap WhatsApp composer, floating WhatsApp button. Used extra olive tints and WhatsApp green. Owner then said: deck colours only, and the site must not read as single-house. Reusable pieces if wanted later: floor-plan SVG (drawn from the architect's layout), FAQ copy, WhatsApp composer.
- **v3** — the portal-hero spec in the four deck colours, six sections, copy rewritten to plural "homes" with a waitlist second entry. Deployed to halapenohomes.com.
- **v4** — Chillax self-hosted (400/600 only), society/flat names removed, no "twin-sharing", footer wordmark uncropped, mobile hero 150svh, two-way deck, the 14-point meeting list (§4b), real photos in the deck, one-day "step inside" photo hero (rejected, reverted).
- **v5** — research-led additions (§4d): terms panel, included/at-actuals, steps, FAQ, composer, sticky mobile bar, OG image.
- **v6 (current)** — Niraj Mehta review (§4e): bigger cream headings, privacy headline, Gallery tab with the walk-through video and full-frame photos, "Tell us what we missed." with the What's-included box and the Book-a-viewing form; before/after, terms panel, steps and composer removed.

## 10. Open items — ask the owner, don't assume

1. WhatsApp business number (CONFIG still `910000000000` — the viewing form and every button point at it), Instagram handle, email.
2. The full-house walk-through film (being recorded by the owner's friend) → `assets/walk.mp4` + poster; the gallery label "coming soon" then goes.
3. Logo in the header (`halapeno-homes-logo-transparent.png` exists; the site still uses the text wordmark).
4. Clean reshoot of the flat (pillow plastic, mattress label, kitchen and bathroom are unusable as shot); the living room once the projector wall is finished.
5. Wording of the Curfew row ("come & go freely" is a placeholder) and confirmation that the included / at-actuals and FAQ terms still match the agreement.
6. What "List your flat" in the footer should do.
7. Whether Superdesign exploration should go ahead (costs credits).
