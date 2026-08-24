# Quality bar

Walk this before saying a site is finished. Anything unticked is a finding.

## System fidelity

- [ ] `DESIGN.md` is committed in the project, with its source URL at the top
- [ ] Every color in the CSS is a token — `grep -nE '#[0-9a-fA-F]{3,8}' ` over the
      stylesheet returns only the token definitions
- [ ] Every font-size is a scale step; no in-between values
- [ ] Only the radii the system allows (usually two or three) appear anywhere
- [ ] Shadows are copied from the system, not from a shadow generator
- [ ] The accent color appears only in the roles its **Role** column permits
- [ ] Each item on the system's **Don't** list checked individually against the build
- [ ] Any deviation is written down in `DESIGN.md` with a one-line reason

## Layout

- [ ] Works at 360, 390, 768, 1024, 1440 — no horizontal scroll at any of them
- [ ] Page max-width and section gaps match the system's Layout block
- [ ] Vertical rhythm is consistent; sections are not all the same height and weight
- [ ] Nothing is centred by default just because it was easier
- [ ] Tables, code blocks, and wide media scroll inside their own container

## Type

- [ ] One `<h1>`, heading levels in order, no level skipped for size reasons
- [ ] Body measure between roughly 45 and 80 characters
- [ ] The named font actually loads; fallback stack present; no FOIT
- [ ] Letter-spacing follows the system's tracking rule at display sizes
- [ ] Real copy throughout — no lorem ipsum, no "Feature One"

## Accessibility

- [ ] Text contrast ≥ 4.5:1 (≥ 3:1 for text ≥ 24px), including text on images
- [ ] Every interactive element reachable by Tab, in a sensible order
- [ ] Visible focus ring on every one of them — never `outline: none` without a
      replacement
- [ ] Touch targets ≥ 44×44px
- [ ] Alt text on content images, `alt=""` on decorative ones
- [ ] Form inputs have real `<label>`s; errors are described in text, not by color alone
- [ ] `prefers-reduced-motion: reduce` disables non-essential animation
- [ ] `<html lang>` set correctly

## Behaviour

- [ ] Hover, focus, active and disabled states exist for every control
- [ ] Motion is short (150–300ms) and eases; nothing loops in the periphery
- [ ] Images have explicit `width`/`height`; no layout shift on load
- [ ] Below-the-fold images `loading="lazy"`
- [ ] No console errors; no 404s in the network tab
- [ ] Renders correctly with JavaScript disabled, if the page is static

## Content

- [ ] The hero says what this is, for whom, in plain words — no "Empower your workflow"
- [ ] The primary action appears in the hero and again at the close, worded identically
- [ ] Claims that need evidence have it
- [ ] Nothing invented about the user's business — placeholders are labelled as such
- [ ] `<title>`, meta description, Open Graph image, favicon all present

## Verification, not inspection

Reading the code is not checking it. Serve the page, open it, screenshot desktop and
mobile, and look at the screenshots.

If Playwright is not installed, a headless Chromium usually still is:

```bash
CHROME=$(command -v chromium chromium-browser google-chrome 2>/dev/null | head -1)
CHROME=${CHROME:-$(ls -d /opt/pw-browsers/*/chrome-linux/headless_shell \
                     /opt/pw-browsers/*/chrome-linux/chrome 2>/dev/null | head -1)}
"$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=1440,900 --screenshot=desktop.png index.html
"$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=390,844 --screenshot=mobile.png index.html
```

A quick way to catch tokens that silently fell through to a fallback:

```bash
grep -nE '#[0-9a-fA-F]{3,8}|[0-9]+px' styles.css | grep -v 'var(--'
```

Then report, unprompted, in the user's language:

**Must fix** — broken, inaccessible, or off-system.
**Should fix** — works, but a careful designer would change it.
**Fine as is** — noticed and deliberately left.

One plain sentence per point, no jargon. Never report "done" with an open Must-fix.
