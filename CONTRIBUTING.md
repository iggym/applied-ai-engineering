# Contributing to Applied AI Engineering

This is the synthesis hub where patterns from production-ai-patterns, agentic-engineering, scaling-ai-systems, and sibling field-notes repos add up to a strategic argument.

## Article Guidelines

### Structure (Required)

Every brief follows a fixed pattern:
1. **Cold open**: A real incident or anecdote (dated, sourced)
2. **Thesis statement**: The claim in one sentence
3. **Three+ cases**: Evidence that the pattern shows up repeatedly
4. **Reframe**: What the pattern actually says (different from the obvious reading)
5. **Counterargument**: The strongest objection, stated fairly
6. **Four Moves**: Actionable recommendations with success signals
7. **Takeaways**: Three bullet points you carry

See `docs/master-prompt-v1.md` for the full template and its 8-point pre-submission checklist.

### Metadata Requirements

Use `docs/metadata.schema.json` as the source of truth. Every article must have:

- **id**: 3-digit unique identifier (001-999) assigned in publication order
- **slug**: URL-safe identifier (lowercase, hyphens only); must match filename without .html
- **title**: Article title as it appears in the <title> tag
- **hook**: One-sentence premise (50–100 chars); appears on hub cards
- **path**: `articles/filename.html`
- **date**: Publication date (YYYY-MM-DD)
- **status**: `published` (or `draft`, `archived`)
- **format**: `essay` (other formats: `guide`, `analysis`, `tutorial`)
- **tags**: Array of lowercase hyphenated tags; see Consolidated Vocabulary below
- **reading_time_minutes**: Integer; auto-computed as `max(1, round(word_count / 230))`
- **pinned**: Boolean; `true` only for leadership briefs
- **research_window**: Date range (YYYY-MM-DD to YYYY-MM-DD) covering sources

### Consolidated Tag Vocabulary

Use these tags consistently across articles:

**Core domain:**
- `agentic-systems` — Agents, multi-step reasoning, autonomous tools
- `architecture` — System design, blast radius, credential scoping
- `strategy` — Business decisions, vendor evaluation, team incentives
- `incident-analysis` — Postmortems, failure modes, real events
- `production` — Live systems, scaling, reliability

**Audience & style:**
- `evaluation` — Model benchmarks, leaderboards, measurement
- `human-in-the-loop` — Oversight, approval, judgment
- `governance` — Policy, risk, oversight
- `org-design` — Hiring, team structure, reporting

**Technical depth:**
- `vendor-critique` — Vendor claims vs. reality
- `platform-engineering` — Infrastructure, tooling

### Naming

**Slug and filename must match**, with hyphens:
- Slug: `your-chatbot-has-signing-authority`
- File: `articles/your-chatbot-has-signing-authority.html`

### Sources & Citations

- Every claim must cite a verified source
- Use `[[n]]` markers in body text; render as `<sup><a href="#fn-n">[n]</a></sup>`
- Footer contains numbered source list with author, title, date, URL
- Only primary sources (research papers, announcements, incident reports) or credible secondary sources (major news, established blogs)
- No fabricated references

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-slug="slug-from-filename">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Article Title — Applied AI Engineering</title>
  <meta name="description" content="Hook text (50-160 chars).">
  <!-- og:*, twitter:*, preconnect for fonts -->
</head>
<body>
  <nav class="aae-hub-link"><a href="../">← Applied AI Engineering</a></nav>
  <article>
    <h1>Article Title</h1>
    <!-- hero SVG here, optional -->
    <section><!-- body content --></section>
  </article>
  <footer><!-- sources --></footer>
</body>
</html>
```

**House theme:**
- Display: Fraunces
- Body: Source Serif 4
- Monospace: IBM Plex Mono
- Accent: Brass `#C08A3E`, Rust `#A6503E`

### Before You Submit

```bash
python3 scripts/validate-metadata.py
```

Check:
- [ ] Metadata valid (runs validator)
- [ ] All sources have dated links
- [ ] No template markers visible
- [ ] Slug matches filename
- [ ] `<title>` tag set
- [ ] Responsive at 360px and 1280px
- [ ] Dark mode readable

## Review Checklist

Before merging:
1. ✓ Cold open is real, dated, sourced
2. ✓ Thesis is falsifiable
3. ✓ Three+ distinct cases, same mechanism
4. ✓ Counterargument is strongest objection
5. ✓ Each move is actionable, signal measurable
6. ✓ Metadata consistent; no duplicates
7. ✓ All sources verified
8. ✓ No gendered pronouns for unnamed people (use they/them)

See `docs/master-prompt-v1.md` for full authoring framework.
