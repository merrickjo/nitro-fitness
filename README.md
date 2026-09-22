# NITRO — Badminton Strength

A single-page generator for badminton-specific strength circuits. Pick your kit, pick your rounds, hit reroll. It gives you a warm-up and three supersets, with reps only — no timers, no clocks, nothing that needs a screen refresh mid-set.

**[Open the app →](https://merrickjo.github.io/nitro-fitness/)** *(update this link after renaming the repo and enabling GitHub Pages)*

---

## What it is

Every movement in the library earns its place by feeding one of six badminton demands. The session skeleton is fixed so a random draw is never lopsided:

| Slot | Demand | Why it's in a badminton session |
|------|--------|---------------------------------|
| **A1** | Knee-dominant / deceleration | The lunge to the net and the push back to base |
| **A2** | Horizontal pull | Mid-back and rear delt — the brake on every overhead swing |
| **B1** | Hip hinge power | Triple extension for the jump smash and explosive push-off |
| **B2** | Scapula + rotator cuff | Keeps the racket shoulder healthy under repeated overhead load |
| **C1** | Lateral / change of direction | Side-to-side court coverage and the ability to stop |
| **C2** | Rotation / anti-rotation | Transfers hip power into the racket head without leaking it |

Reroll redraws all six slots, all three warm-up movements, and the rep counts. Each block also has its own swap button if only one pair needs changing.

## Kit modes

- **TRX + kettlebell** — the full library, nothing that needs a rack, bench, or barbell.
- **Bodyweight** — every slot has real bodyweight entries, including honest horizontal-pull options (inverted row under a table, towel row on a door handle, prone swimmer pulls) rather than pretending the pull slot can be skipped.

The two pools never mix. Switching kit redraws the whole session.

## Built for e-ink

The interface is designed to be read on a reflective e-ink panel first and a backlit screen second:

- Only pure black, pure white, and two grays that land on clean grayscale steps — no gradients, no shadows, no translucency.
- All transitions and animations are disabled globally. Every animated pixel on e-ink is a panel refresh and a ghosting artifact.
- Heavy condensed display type and monospaced numerals, sized for reading at arm's length.
- State is shown by full inversion (black fill, white text) rather than by color or subtle tint.
- 48px minimum touch targets; nothing depends on hover.
- Prints cleanly — controls drop out, the session stays.

Dark mode inverts to pure white-on-black and follows the system setting.

## Install it

NITRO is a PWA — it installs to the home screen and runs with no network, which is the point on an e-ink phone in a gym.

**Brave / Chrome on Android:** open the Pages URL → menu (⋮) → **Install app** (or *Add to Home screen*). It installs as a real WebAPK: own launcher icon, own task in the app switcher, no browser chrome.

**Safari on iOS:** Share → Add to Home Screen.

**Desktop Chrome / Brave / Edge:** install icon in the address bar.

After the first load the service worker precaches the app shell and the IBM Plex fonts, so every launch after that works offline. Updates land on the next launch after a push — the page is served from cache and refreshed behind you.

## Session shape

```
Warm-up  ·  3 movements, one pass
Working  ·  N rounds of  A1→A2  B1→B2  C1→C2
```

Rounds toggle between 2, 3, and 4. Rest is deliberately unprescribed — take what you need between pairs.

Each session gets a four-character code (e.g. `SESSION K4WP`) so you can note in a log which draw you actually did.

## Tech

Vanilla HTML, CSS, and JavaScript. No build step, no framework, no backend. `localStorage` remembers your kit and rounds choice only, wrapped in try/catch so it degrades silently in private windows.

```
index.html              the whole app — markup, styles, movement library, logic
manifest.webmanifest    PWA metadata (name, icons, standalone display)
sw.js                   service worker: precached shell, offline-first
icons/                  192 / 512 / maskable-512 / apple-touch / favicon
```

Icons are generated geometrically (no font dependency) — see the commit that added them if you want to regenerate at other sizes.

## Run it

```bash
git clone https://github.com/merrickjo/nitro-fitness.git
cd nitro-fitness
open index.html
```

Or serve it on GitHub Pages: Settings → Pages → Deploy from a branch → `main` / root.

## Adding movements

Edit the `POOL` and `WARMUP` objects near the top of the script block. Each entry:

```js
{ n:'KB lateral lunge', kit:'trxkb', r:[6,8,10], u:U.SIDE,
  c:'Side-to-side coverage and the push back to base, loaded.' }
```

- `kit` — `'trxkb'`, `'bw'`, or `'both'`
- `r` — candidate rep values; the draw picks one
- `u` — a unit from the `U` map
- `c` — one line on what it does for badminton. If you can't write that line, the movement doesn't belong in the pool.

## License

No license file yet, which reserves all rights to the author. Add one if you want this reusable.
