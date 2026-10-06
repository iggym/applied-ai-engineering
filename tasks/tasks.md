# Tasks — Improving the Repo and Site

These tasks come from an audit of `index.html`, `metadata.json`, `README.md`, and the 12 files in `articles/` (2026-10-06).
Priority: **P0** means the site is broken or wrong now. **P1** gives high value. **P2** is polish.
Each task has an acceptance check.

---

## P0 — Data integrity and broken content

- [ ] **Fix the duplicate `vendor-rhetoric-vs-practitioner-reality` entries in `metadata.json`.**
  Two entries (ids `0001556` and `0042`) share a slug and both point to `articles/vendor-rhetoric-vs-practitioner-reality.html`. As a result, the hub lists one article twice and never links `articles/vendor-rhetoric-vs-practitioner-reality-0.html` ("The Demo-to-Production Chasm"). Give that file a real slug, for example `demo-to-production-chasm.html`, and point entry `0042` at it, or merge or drop it if it is a near-duplicate.
  *Check:* every `path` in `metadata.json` is unique, and every file in `articles/` is listed exactly once.
- [ ] **Remove the duplicated hook.** `throwing-bodies-at-silicon` reuses the hook of `scaling-laws-vs-operating-laws` word for word ("The industry keeps borrowing model-scaling intuition…"). Write a hook specific to that article. Also decide whether the two pieces should be merged, because they argue the same thesis.
- [ ] **Fix `the-4096-token-illusion.html`.** Its `<title>` is "Article Shell Runner", and its content is rendered from a JSON payload with client-side `${data.title}` templates. Without JS, the page is empty and cannot be indexed. Render the prose into static HTML and set a real title.
  *Check:* with JS turned off, the page shows the full article text, and the title matches metadata.
- [ ] **Check the dates.** `what-postmortems-bury` (2025-04-24) and `taming-kills-the-wolf` (2025-03-11) are dated more than a year earlier than the rest of the docket. Their ids (`0072`, `0017`) are also out of order. Confirm the real publish dates.
- [ ] **Add the missing "back to hub" links.** `the-failure-taxonomy-industrial-complex.html`, `the-4096-token-illusion.html`, and both `vendor-rhetoric-*` pages have no link back to `../`. Readers who arrive from a shared link are stranded.

## P1 — Consistency and schema

- [ ] **Normalize `metadata.json` to one schema.** Four entries have no `id`, `slug`, `format`, or `research_window`. Ids use mixed formats (`0001`, `0047`, `0001556`, `00014755`). Re-number them as a 3-digit docket sequence in publish order. Make `research_window` use the same format everywhere (some entries wrap dates in `[...]`). Pretty-print the file consistently (2-space indent).
- [ ] **Make the slugs match the filenames.** `failure-taxonomy-industrial-complex` lives at `the-failure-taxonomy-industrial-complex.html`. Either rename the file or fix the slug. If you rename, leave a redirect stub at the old URL.
- [ ] **Clarify the two "failure taxonomy" pieces.** `failure-taxonomy-is-not-a-strategy` and `the-failure-taxonomy-industrial-complex` are both pinned and overlap heavily. Pin only one as the "Lead Brief" and cross-link the two.
- [ ] **Add a JSON Schema and a validator.** Add `docs/metadata.schema.json` and a small, dependency-free script (Python or Node) that checks the schema, unique id, slug, and path, that each path exists, that no hook is duplicated, and that each file's `<title>` matches the metadata title.
- [ ] **Add GitHub Actions CI** (`.github/workflows/validate.yml`) that runs the validator and a link checker (for example, `lychee`) on every PR.
- [ ] **Rewrite `README.md` to match the site.** The README describes a "harness / software factory" hub with code pillars. The site is actually an essay docket for engineering leaders ("Past the taxonomy. Into the argument."). Also:
  - fix the broken clone command (``git clone [https://...](https://...)`` inside a code block),
  - remove the fake "System Status: Production Ready" badge,
  - add an article index, or a link to the hub,
  - document the authoring workflow (`docs/master-prompt-v1.md` → `articles/` → `metadata.json`).
- [ ] **Add `CONTRIBUTING.md`** with the article checklist (taken from §8 of the master prompt), naming rules, and the metadata schema.
- [ ] **Unify the article design system.** Articles use about 8 different palettes and font stacks (Literata, DM Serif, Playfair, Instrument Serif, Inter/Lora, and system fonts) on both light and dark backgrounds. Move to the house theme (Fraunces / Source Serif 4 / IBM Plex Mono, brass/rust accents) shared with `index.html`. Consider a shared `assets/article.css`, and keep per-article interactive CSS inline.
- [ ] **Add per-article SEO and social meta.** Only 1 of 12 articles has a `meta description`, and none has Open Graph or Twitter tags or a canonical link. Add them to every article and to `index.html`.

## P1 — Hub (`index.html`)

- [ ] **Escape metadata before writing it with `innerHTML`.** Titles, hooks, and tags are inserted unescaped. A stray `<` or `&` in metadata breaks the layout. Use `textContent` or an `escapeHTML()` helper.
- [ ] **Render the article list without JS.** Today the feed is empty if JS fails or `fetch` is blocked (for example, when opened via `file://`). Generate a static `<noscript>` list or pre-render the list with the validator script.
- [ ] **Add tag filtering and search.** With 12+ briefs and more than 30 distinct tags, readers need to filter. Add a tag chip filter (state in the URL hash) and a client-side text search over title and hook.
- [ ] **Consolidate tags.** Merge near-synonyms (`ai-engineering` / `applied-ai` / `engineering`, `rag` / `rag-architecture`, `ai-ops` / `mlops`) into a controlled vocabulary of about 12 tags documented in the schema.
- [ ] **Show the docket number consistently.** Cards fall back to the list index when `id` is missing, so the numbers shift whenever pinning changes.

## P2 — Discoverability and polish

- [ ] Add an `feed.xml` RSS/Atom feed and a `sitemap.xml`, both generated from `metadata.json` by the validator or build script.
- [ ] Add a `favicon.svg` (the brass "stamp" mark), an `og-image.png` default, and per-article social images.
- [ ] Add a `404.html` in the house style that links back to the hub.
- [ ] Add "Next / previous brief" and "Related briefs" (by shared tags) to the footer of each article.
- [ ] Add a light-mode toggle to the hub (respect `prefers-color-scheme`), matching the house-light tokens in the master prompt.
- [ ] Run Lighthouse and axe on each page. Fix contrast, missing labels on interactive controls, and heading-order issues. Make every slider and scrubber usable from the keyboard.
- [ ] Self-host fonts or add `font-display: swap` and preconnects consistently (some articles have no preconnect).
- [ ] Link the sister repos (`production-ai-patterns`, `agentic-engineering`, …) from the hub footer, since the site positions itself as their synthesis.
- [ ] Add an "About / Author" section so that hiring and consulting evaluators (the stated audience) know whose argument they are reading.

## Content pipeline

- [ ] Use `docs/master-prompt-v1.md` for all new briefs. Keep a `docs/prompt-changelog.md`, and bump to v2 after the next 3 briefs, based on what reviewers had to fix.
- [ ] Back-fill a "Sources" section with dated links in the older briefs that lack one (`reference-nobody-finishes`, `failure-taxonomy-is-not-a-strategy`, `the-failure-taxonomy-industrial-complex`), and check every quoted statistic.
- [ ] Add a "The strongest counterargument" block to the briefs that are missing one (`scaling-laws-vs-operating-laws`, `the-4096-token-illusion`, `the-failure-taxonomy-industrial-complex`, both `vendor-rhetoric-*`), so that the hub's promise ("a position, a counterargument, and a verdict") holds for every piece.
- [ ] Keep an editorial backlog (`tasks/backlog.md`) of candidate theses, each tagged by source repo and angle.
