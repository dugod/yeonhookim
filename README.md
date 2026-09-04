# Yeonhoo Kim — application site

A static site. No build step, no dependencies, no framework. Open `index.html`
in a browser and it works.

---

## Read this first — three things to verify

These are factual claims that will sit in front of admissions readers. I built
the site around what the certificates actually say, which in three places is not
what the résumé says.

**1. Taekwondo grade.** The certificate reads **4th Poom**, Kukkiwon-registered
June 2022. Poom is the youth grade; it converts to Dan at 15, and the ID card on
the certificate shows a 2009 birth date, so you may hold 4th Dan now by
conversion — but nothing supplied confirms that. The site currently says
"fourth grade, registered with the Kukkiwon in June 2022" and the room figure
reads "4th Kukkiwon grade." The résumé says "4th Dan Black Belt." Decide which
is accurate, then make both match.

**2. Scholastic.** The Silver Key certificate is **2026 only**, for *The Starr*.
The 2025 certificate is participation. The résumé claims Silver Key in both 10th
and 11th grade. The site is built around the 2026 Silver Key alone.

**3. John Locke.** There are **three** commendation certificates — Junior 2023,
Psychology 2023, History 2024 — where the résumé lists two lines. The site says
three commendations and posts all three essays.

**Also:** the Scholastic and CIMC certificates read **Daniel Kim**, as do two of
the supplied filenames. The site uses Yeonhoo Kim throughout. Pick one name and
use it everywhere, including the résumé.

## Roles taken from the workbook, not the résumé

Where the two disagreed, the workbook won — it was more specific. **The résumé
still needs updating to match**, or these need flipping back:

| | Site says | Résumé says |
|---|---|---|
| Volleyball | Player Gr 9, Captain Gr 10–11 | Captain 9th–11th |
| US Pushcart Library | Member Gr 9–11, Co-Leader Gr 12 | Co-Leader 9th–present |
| Beyond the Border | Member Gr 9–10, Leader Gr 11– | Leader 9th–present |
| Culture Protectors | Member Gr 10, Leader Gr 11– | Leader 10th–present |
| J'Blue Jazz Band | Drums, helps organise | Player (Drums) ✓ matches |

---

## Structure

```
site/
├── index.html                        homepage — the wall of six rooms
├── about.html
├── rooms/
│   ├── physics-research.html         Room 01 · 4 entries
│   ├── competitions-programs.html    Room 02 · 9 entries
│   ├── writing.html                  Room 03 · 4 entries
│   ├── service-community.html        Room 04 · 7 entries
│   ├── music.html                    Room 05 · 3 entries
│   └── sport-discipline.html         Room 06 · 3 entries
├── css/
│   ├── main.css                      tokens, header, footer, shared components
│   ├── index.css                     homepage only
│   ├── about.css                     About only
│   ├── room-base.css                 the category-page template
│   └── rooms/<room>.css              one per room
├── js/
│   ├── main.js                       mobile nav, colophon year
│   ├── index.js  about.js  room-base.js
│   └── rooms/<room>.js               one per room
└── assets/
    ├── images/                       photographs and rendered certificates
    ├── docs/                         essays, papers, certificates (PDF)
    ├── media/                        performance video + poster frames
    └── resume/Yeonhoo-Kim-Resume.pdf
```

## Conventions

**No inline CSS or JS.** No `style="..."` attributes, no `<style>` blocks, no
inline `<script>` blocks anywhere. Verified across all eight pages.

**One stylesheet and one script per page**, named after the page.

**Two shared files break that rule deliberately.** `room-base.css` and
`room-base.js` hold the category-page template. All six rooms use the same
layout, so duplicating it six times would mean six places to fix every change.
Per-room files load *after* room-base, so anything in them overrides it.

**Load order:** `main.css` → `room-base.css` → `rooms/<room>.css`.

## Regenerating

`build.py` (kept outside this folder) generates all eight HTML pages from one
data structure, so the rooms cannot drift apart. Edit the content there and
re-run rather than hand-editing six near-identical files. Once the pages
genuinely diverge, retire the script and edit HTML directly.

## Entry variants

- **Default** — media column left, text right. Used where a photograph exists.
- **`.entry--text`** — full width, no media column. Used where no photograph
  exists yet, so a finished page doesn't look half-built. Add an image and drop
  the modifier.
- **`.entry--wide`** — full width with media *underneath*. Used for the jazz
  band entry, because three video players don't fit in a narrow column.

## Certificates are downloads, not pictures

No certificate is shown as an image anywhere. Awards appear as a line in the
entry label and a download chip; the scan itself opens only if a reader asks
for it. Photographs of the actual work carry the pages instead.

The `.room-tile-frame--type` rule in `index.css` draws a room numeral in place
of a photograph. All six rooms have photographs now, so nothing uses it — it is
kept in case a seventh room arrives before its picture does.

## Still missing

- **Blog content** — entry 3.4 is one line; the blog itself wasn't reachable
- **Two Room 01 links** — the GCIMM poster and the journal submission page
- **Photographs** for Physics Bowl, Sir Isaac Newton, WMTC, all of Room 03, and
  the CMAS entry. Those entries run full width instead (`.entry--text`).

One supplied image was not placed: a "Daniel Kim — US Director, Class of 2027"
card, which sat in the CIMC thumbnails in the workbook. Nothing on the résumé
explains it, so rather than guess at a role I left it out. Tell me what it is
and it goes in.

## Images

Photographs use `class="is-photo"` (`object-fit: cover`). Scanned certificates
use `class="is-document"` (`object-fit: contain`, white background) so nothing
gets cropped off. Ratio comes from the utility class on the box, so an `<img>`
inherits it without distorting.

Certificate PDFs that were pure scans have been rasterised to 150 dpi and
re-saved — 22.8 MB down to 2.2 MB, still legible down to the ID-card text.
**Text PDFs were left untouched**, since rasterising an essay would destroy
selectable text and break screen readers.

## Video

Three performance videos, re-encoded to 960px H.264 with `faststart` — 84 MB
down to 27 MB. Each has a poster frame and `preload="none"`, so nothing
downloads until a reader presses play. The Music room tile is a frame pulled
from the Billie's Bounce recording.

## Design rules worth not breaking

- **DM Serif Display ships in one weight (400).** Never bold or lighten it —
  browsers synthesize a smeared fake. Change size instead.
- **Tracking tightens as the serif grows:** `-0.028em` at hero size, `-0.018em`
  at entry titles, `-0.014em` on tiles.
- **`#3EB1C8` appears on hover and focus only.** Never at rest.
- **Italic maroon appears exactly twice** per page — wordmark and headline.
- **Inter labels are uppercase, weight 500–600, tracking `+0.16em`.**

## Local preview

```
cd site
python3 -m http.server 8000
```

Then open `http://localhost:8000`. Opening files directly via `file://` mostly
works, but a local server matches how the site will actually behave — and video
playback is more reliable over HTTP.

## Hosting

Any static host. On Netlify or Cloudflare Pages the `.html` extension is
stripped automatically, giving `/rooms/physics-research`; GitHub Pages keeps the
extension. Decide before sharing links, since changing it later breaks anything
already sent.
