# Imagery for the page

## First: does this system want images at all?

Read the **Imagery** section of the fetched `DESIGN.md` before generating anything.
Systems fall into three groups, and the wrong choice is instantly visible:

| System says | Do this |
|---|---|
| "Minimal imagery — the UI is the visual language" (Linear, shadcn, most devtools) | No photography. Build the visual from real UI: cards, tables, a fake terminal, an SVG diagram |
| "Editorial photography", "full-bleed hero image", "product shots" | Generate real images |
| Illustration / abstract gradient / 3D render | Generate, but match the named medium exactly |

Adding stock photography to a system that does not use it is the fastest way to make a
careful build look cheap.

## Generating

Use the Higgsfield MCP when it is connected:

- `mcp__Higgsfield__generate_image` — one image (`count: 2-4` for variants of the *same*
  prompt)
- `mcp__Higgsfield__generate_image_batch` + `jobs_wait` — several different images
- `mcp__Higgsfield__models_explore` with `action: 'recommend'` when unsure which model
  fits; it also lists the valid `aspect_ratio` values per model
- rough starting points: photoreal people/editorial → `soul_2`; product and commercial
  shots → `marketing_studio_image`; anything with legible text, diagrams, or 4K needs →
  `nano_banana_pro`

Then **download the result into the project** (`assets/`) and reference it locally.
Never leave a page pointing at a generation URL or a stock-photo hotlink — both rot,
and the licence usually does not cover the user's site.

If Higgsfield is not connected: build the visual in CSS/SVG in the system's own visual
language, or leave a labelled placeholder box containing the exact prompt as a comment.
Say plainly which of the two you did — do not quietly ship a grey box.

## Prompt recipe

Derive the prompt from the DESIGN.md, not from taste. Five parts:

```
<subject and action, concrete> ·
<medium: photograph / 3D render / editorial illustration> ·
<lighting and mood, from the system's summary line> ·
<palette: name the 2-3 actual hex values from Tokens — Colors> ·
<framing: composition, negative space where the headline sits>
```

Example, for a fintech system whose palette is `#061b31` ink, `#f8fafd` mist,
`#533afd` indigo:

> Photograph of a woman at a standing desk reviewing a payments dashboard on a laptop,
> shot from a low three-quarter angle · editorial photography, 50mm, shallow depth of
> field · soft cool daylight from a large window, calm and unhurried · palette limited
> to deep navy #061b31, cool off-white #f8fafd and a single indigo #533afd accent ·
> wide 16:9 framing with the subject on the right third and clean empty wall on the
> left for headline text

Always name the hex values. It is the single biggest lever on whether the image sits
inside the design system or fights it.

## Rules

- **Aspect ratios** — hero 16:9 or 21:9; card thumbnails 4:3 or 1:1; portraits 3:4.
  Generate at the ratio you will display; do not squash in CSS.
- **Negative space** — if text overlays the image, ask for empty space where the text
  goes, and still add a scrim so contrast holds at ≥ 4.5:1.
- **Consistency** — one lighting setup and one palette line across every image on the
  page. Reuse the same prompt tail for all of them.
- **Weight** — export/convert to WebP, cap hero images around 200 KB, and set explicit
  `width`/`height` so the layout does not jump. `loading="lazy"` on everything below
  the fold.
- **Alt text** — describe the content, not the file. Decorative images get `alt=""`.
- **People** — generated faces are fine for mood, never for testimonials, team pages,
  reviews, or anything a visitor would read as a real named person. Say in the handover
  which images are generated.
- **Never generate** logos of real companies, a real person's likeness, or images that
  imply endorsement.
