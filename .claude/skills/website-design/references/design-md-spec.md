# The DESIGN.md format

This is the shape of the files published on styles.refero.design. Read it to know what
you are getting; use it as the template when you have to author a system by hand
(offline, or for a brand with its own guidelines).

A real file runs 15–25 KB. Sections appear in this order. Not every file carries every
one — a system with no shadows has no Shadows table, and *Design Philosophy* and
*Type Scale Detail* only appear on some styles. The stable core, present everywhere, is:
**Tokens — Colors**, **Tokens — Typography**, **Tokens — Spacing & Shapes**,
**Components**, **Do's and Don'ts**, **Surfaces**, **Elevation**, **Imagery**,
**Layout**, **Agent Prompt Guide**, **Similar Brands**, **Quick Start**.

---

## Header

```markdown
# <Name> — Style Reference
> <five-word sensory summary, e.g. "indigo-ink ledger on frosted glass">

**Theme:** light | dark

<One paragraph: what the system feels like and why. Names the accent discipline,
the type voice, and how depth is handled. This paragraph is the brief — read it twice.>
```

## Tokens — Colors

A table, never a naked swatch list. The **Role** column is the important one: it says
where each color is allowed to appear.

| Name | Value | Token | Role |
|------|-------|-------|------|
| Canvas | `#f5f5f5` | `--color-canvas` | Page background, muted surface fills |
| Ink | `#0a0a0a` | `--color-ink` | Primary text, headings, button labels |
| Ember | `#e7000b` | `--color-ember` | Destructive states only — never decoration |

Typical count: 8–16 colors. If a role says "only", treat it as a hard constraint.

## Tokens — Typography

Per font family: usage, weights, sizes, line heights, and a letter-spacing rule that
usually tightens at display sizes and loosens for small uppercase labels. Then the scale:

| Step | Size | Line height | Tracking | Token |
|------|------|-------------|----------|-------|
| caption | 12px | 1.33 | 0.6px | `--text-caption` |
| body | 14px | 1.43 | — | `--text-body` |
| display | 48px | 1.1 | -2.4px | `--text-display` |

Named ratio (e.g. "Major Second (1.125) from 16px base") plus 7–9 steps. Do not
introduce sizes between steps.

## Tokens — Spacing & Shapes

- **Base unit** (usually 4px) and **density** (compact / comfortable)
- **Spacing scale** — the allowed values, as tokens
- **Border radius** — per element class: cards, buttons, inputs, badges, small, nested
- **Shadows** — named, with full values
- **Layout** — page max-width, section gap, card padding, element gap

The radius table is where most builds go wrong: systems usually allow exactly two or
three radii, and mixing in a fourth reads as sloppy immediately.

## Components

10–15 entries. Each one:

```markdown
### Primary Filled Button
**Role:** High-emphasis action (Submit, Save, Create)

Background #0a0a0a, text #fafafa, no border, radius 18px, padding 0 12px,
font 14px weight 500, height ≈36–40px. <One sentence on why it looks that way.>
```

Build components from these specs verbatim rather than from your own defaults.

## Do's and Don'ts

Two bullet lists, 5–8 items each, in imperative voice and specific to this system
("Do not use border-radius values other than 18px or 24px"). Binding. Re-read before
declaring the build finished.

## Surfaces

Numbered elevation levels (0 = canvas, up to 3–4), each with a value and a purpose.
Tells you how to layer without inventing new grays.

## Elevation

Per-component shadow values, including the honest "none — relies on tonal contrast".

## Imagery

Prose: whether the system uses photography, illustration, product screenshots, or no
imagery at all; icon style and stroke weight; how graphics relate to the palette.
This governs step 5 of the skill — a system that says "minimal imagery, the UI is the
visual language" must not get stock photos added to it.

## Layout

A short prose section on page structure: grid behaviour, how sections are banded, where
the system uses full-bleed vs. contained width, nav and footer treatment.

## Agent Prompt Guide

- **Quick Color Reference** — six or seven lines: background, surface, text, muted,
  border, primary action, destructive.
- **Example Component Prompts** — five ready-made specs you can hand to a builder.

## Design Philosophy

Three numbered principles that explain the system's internal logic. Use these to decide
anything the tokens do not cover.

## Similar Brands

Four or five neighbours with one line on what they share. Useful when the chosen style
is nearly right — a neighbour may fit better.

## Quick Start

Two code blocks: a `:root { … }` block of CSS custom properties (typically 60–90 tokens)
and a Tailwind v4 `@theme { … }` block with the same values. **This is what you paste
into the project.** Copy one wholesale; delete nothing.

---

## Authoring one by hand

When there is no network, or the user has brand guidelines instead:

1. Fill every section above — an incomplete system is worse than none, because the gaps
   get filled with defaults.
2. Start from the brand's real assets: logo colors, existing print, the founder's slide
   deck. Extract, don't invent.
3. Give each color a **Role** sentence that forbids something. Constraints are what make
   a system look designed.
4. Pick two radii and two shadows. No more.
5. Set the type scale from a named ratio and stick to it.
6. Write the Don't list last, from the mistakes you can already feel yourself about to
   make on this particular page.
