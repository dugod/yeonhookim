# Yeonhoo Kim — application site

A static site.

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
