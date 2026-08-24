# website-design skill

Builds websites against a real design system pulled from
[styles.refero.design](https://styles.refero.design) instead of an invented look.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The workflow Claude follows — brief → style → tokens → build → imagery → check |
| `references/refero-styles.md` | 200 catalogued styles with links, grouped by site type |
| `references/design-md-spec.md` | The DESIGN.md format, and how to author one offline |
| `references/imagery.md` | When to generate images, prompt recipe, image rules |
| `references/quality-bar.md` | The checklist run before anything is called finished |
| `scripts/refero_style.py` | Catalog search + single-style DESIGN.md fetch |
| `scripts/catalog.json` | The catalog data |

## Make it available everywhere

As committed here it applies to this repository only. To have it trigger in every
project:

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/website-design ~/.claude/skills/
```

Then start a new Claude Code session. `/skills` should list `website-design`.

## Quick use

```bash
cd ~/.claude/skills/website-design      # or .claude/skills/website-design
python3 scripts/refero_style.py categories
python3 scripts/refero_style.py list fintech-websites
python3 scripts/refero_style.py search linear
python3 scripts/refero_style.py get "Linear" -o ~/myproject/DESIGN.md
```

`get` fetches one style page at a time, for the style actually chosen. It is not a
crawler and must not be looped over the catalog — `styles.refero.design/robots.txt`
asks AI agents not to bulk-crawl, and Refero's own MCP is the sanctioned route for
volume access.

## Optional: Refero's official plugin

Deeper research (150k+ real app screens, 6k+ user flows) needs a Refero Pro account:

```
/plugin marketplace add referodesign/refero_skill
/plugin install refero@refero
```

MCP endpoint: `https://api.refero.design/mcp`. This skill works without it.
