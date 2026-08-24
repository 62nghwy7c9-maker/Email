---
name: website-design
description: Use for ANY request to build, create, design, redesign, restyle or improve a website, landing page, homepage, web page, marketing site, portfolio, docs site, dashboard UI or web app front end — including "make me a site for X", "build a landing page", "give this page a design", or a new HTML/React/Next/Astro/Tailwind page. Pulls a real DESIGN.md design system from styles.refero.design (colors, type scale, spacing, radii, shadows, components, do/don't) and builds strictly against those tokens instead of inventing a look. Also covers generating realistic imagery for the page. Do NOT use for backend-only work, scripts, or documents that are not web pages.
---

# Website design, built on a Refero design system

**Rule: no website gets designed from memory.** Before writing any markup, a concrete
design system is chosen, fetched, and written into the project as `DESIGN.md`. Every
color, size, radius and font in the build then traces back to a line in that file.
That is the whole point of this skill — the alternative is the default AI look
(purple gradient, Inter, 8px radius, three feature cards), which is what the user is
trying to avoid.

## Order of operations

Do these in order. Do not skip to step 4.

1. **Brief** — one short paragraph, out loud.
2. **Style** — pick and fetch a DESIGN.md.
3. **Tokens** — turn it into real CSS variables.
4. **Build** — the page, using only those tokens.
5. **Imagery** — generate what the page actually needs.
6. **Check** — run it, look at it, report findings.

---

## 1. Brief

Write two or three lines and show them to the user before building:

- **Subject** — what this site is, and for whom.
- **Job** — the one thing a visitor should do or understand.
- **Sections** — the page list, in order.
- **Mood** — three adjectives, e.g. "quiet, technical, expensive".

If the request is vague ("a website for my business"), pick a concrete reading, state
it in one sentence, and continue. Only stop and ask when two readings would produce
completely different sites.

## 2. Pick and fetch a design system

Match the mood and the sector to a category, then a style.

```bash
cd .claude/skills/website-design      # or wherever this skill lives
python3 scripts/refero_style.py categories
python3 scripts/refero_style.py list ai-startup-websites
python3 scripts/refero_style.py search stripe
```

Categories: `clean-saas`, `editorial-websites`, `dark-mode-websites`, `fintech-websites`,
`devtools-websites`, `ai-startup-websites`, `ecommerce-websites`, `minimal-websites`,
`agency-websites`, `productivity-apps`. Full list with links:
[references/refero-styles.md](references/refero-styles.md).

Offer the user **three** candidates by name with one line each on why, and a default
recommendation. Then fetch the chosen one into the project:

```bash
python3 scripts/refero_style.py get "Stripe" -o <project>/DESIGN.md
```

Four ways to obtain the system, in order of preference:

| Route | When | How |
|---|---|---|
| Refero MCP | `refero`/`mcp__refero__*` tools are connected | Use them — they search 150k+ real screens and flows, not just styles |
| Bundled script | Default | `refero_style.py get …` — one page, for the style actually chosen |
| User paste | Script blocked, or the user already has a favourite | Ask them to open the style page and press **Copy .md**, then paste it in |
| Author one | Fully offline, or a brand with its own guidelines | Write a DESIGN.md by hand in the same shape — see [references/design-md-spec.md](references/design-md-spec.md) |

Fetch only the one style that was chosen. Do not loop the script over the catalog:
`styles.refero.design/robots.txt` asks AI crawlers not to bulk-crawl the site, and the
Refero MCP is the sanctioned high-volume route. A single user-directed lookup is fine.

**Never mix two style systems in one site.** If the user likes the type of one and the
color of another, say so explicitly and record the graft as a deviation in `DESIGN.md`.

## 3. Tokens before markup

Commit `DESIGN.md` to the project. Its **Quick Start** section already contains two
ready-made code blocks — a `:root { … }` block of CSS custom properties and a Tailwind v4
`@theme { … }` block. Paste the right one into the project's token layer **before** the
first component:

- plain CSS / HTML → the `:root` block, in a `tokens.css` loaded first
- Tailwind v4 → the `@theme` block
- React / Next → the same CSS variables, referenced from components; no hex literals
- fonts → load the named face from Google Fonts / Fontsource **with the stated fallback
  stack**; if the face is commercial (Söhne, Geist Mono Pro, custom), use the fallback
  and note the substitution at the bottom of `DESIGN.md`

Token *names* differ from style to style — one system exposes `--radius-buttons` and
`--radius-cards`, another `--radius-md` and `--radius-lg`. Read the block you pasted;
do not write against remembered names, or you will silently fall through to defaults.

From here on: **no raw hex, no ad-hoc px radius, no font-size outside the scale.** If
the page needs something the system does not have, add it to `DESIGN.md` first, with a
one-line reason.

## 4. Build

Work section by section, following the DESIGN.md **Components** entries — they specify
padding, radius, border, and shadow per component. The file's **Do / Don't** list is
binding; read it again before you finish.

Structure that holds up for most sites:

- **Hero** — the single most characteristic thing about the subject. A big number with
  a gradient accent and three feature cards is the template answer; only use it if it
  is genuinely right.
- **Proof** — what makes the claim believable (numbers, logos, a real screenshot, a quote).
- **Substance** — how it works, what you get, what it costs. Real copy, not lorem ipsum.
- **Close** — one clear action, repeated from the hero.

Non-negotiables regardless of style: responsive from 360 px up, keyboard-reachable
interactive elements with a visible focus ring, `prefers-reduced-motion` respected,
text contrast ≥ 4.5:1, real `<h1>`/`<h2>` hierarchy, alt text on every image.
Full list: [references/quality-bar.md](references/quality-bar.md).

## 5. Imagery

The DESIGN.md **Imagery** section says what kind of visuals the system uses — some
systems (Linear, shadcn) use almost none, and adding stock photography to those breaks
them. Follow it.

When the page does need photography or illustration, **generate it** rather than
hotlinking stock URLs, which rot and often are not licensed:

- Higgsfield MCP available → `mcp__Higgsfield__generate_image` (or `_batch` for several),
  then download into `assets/` and reference locally.
- Not available → build the visual from CSS/SVG in the system's own language, or leave a
  clearly-labelled placeholder box with the exact prompt in a comment. Say which you did.

Prompt recipe, aspect ratios, and how to keep generated images inside the palette:
[references/imagery.md](references/imagery.md).

## 6. Check before reporting done

Never report "finished" on unexecuted code.

1. Serve it (`python3 -m http.server`, or the project's dev server) and open the page —
   with the `run` skill or Playwright/Chromium if a browser is available.
2. Screenshot desktop (1440) and mobile (390). Look at both.
3. Walk the DESIGN.md **Don't** list item by item against what you built.
4. Check the quality bar list.
5. Report findings, unprompted, in the user's language, grouped as:
   **Must fix / Should fix / Fine as is** — one plain sentence each, no jargon.

If anything is in "Must fix", fix it, then re-check. Only then say it is done.

---

## Notes

- The user's own brand guidelines always outrank the fetched system. Fetch a style for
  structure and rhythm, then swap the palette to the brand's and record it in `DESIGN.md`.
- Refero also ships an official plugin with deeper research tools (needs a Refero Pro
  account): `/plugin marketplace add referodesign/refero_skill`, then
  `/plugin install refero@refero`. MCP endpoint: `https://api.refero.design/mcp`.
  This skill works without it.
- Style names in the catalog are real products. Take the *system*, not the brand — do
  not reproduce a company's logo, wordmark, or copy on someone else's site.
