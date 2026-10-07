# Applied AI Engineering

> **Past the taxonomy. Into the argument.**

A synthesis hub for engineering leaders: essays on production AI systems, incident analysis, and the hard architectural realities that vendors won't tell you.

**[Read the hub →](https://iggym.github.io/applied-ai-engineering/)**

---

## What This Is

A curated collection of *briefs*—long-form essays (5–11 min read) for engineering leaders and hiring/consulting evaluators. Each brief:
- Starts with a real, dated incident
- Makes a falsifiable claim
- Provides three+ cases showing the pattern repeats
- Offers a reframe (what it actually means)
- Addresses the strongest counterargument
- Ends with four actionable moves

**Audience**: Engineering leaders making decisions about AI systems, vendors, and teams.

## The Hub

The site synthesizes patterns from field-notes repos covering production AI patterns, agents, scaling, operations, and architecture.

18 articles. No ads. No nav bloat. Pure argument.

## Article Index

| ID | Title | Read | Date |
|----|-------|------|------|
| 001 | [The Failure Taxonomy Industrial Complex](articles/the-failure-taxonomy-industrial-complex.html) | 9 min | 2026-08-06 |
| 002 | [Why Your AI Failure Taxonomy Isn't a Strategy](articles/failure-taxonomy-is-not-a-strategy.html) | 11 min | 2026-07-14 |
| 003 | [Your Chatbot Has Signing Authority](articles/your-chatbot-has-signing-authority.html) | 7 min | 2026-10-07 |
| 004 | [The Pipeline Illusion](articles/vendor-rhetoric-vs-practitioner-reality.html) | 8 min | 2026-05-15 |
| 005 | [The 4096-Token Illusion](articles/the-4096-token-illusion.html) | 7 min | 2026-05-15 |
| 006 | [The Demo-to-Production Chasm](articles/demo-to-production-chasm.html) | 8 min | 2026-05-15 |
| 007 | [The Architecture Reference Nobody Finishes](articles/reference-nobody-finishes.html) | 6 min | 2026-06-10 |
| 008 | [Scaling Laws Are Not Operating Laws](articles/scaling-laws-vs-operating-laws.html) | 10 min | 2026-06-22 |
| 009 | [Read-Heavy, Write-Cautious](articles/read-heavy-write-cautious.html) | 9 min | 2026-07-28 |
| 010 | [Throwing Bodies at Silicon](articles/throwing-bodies-at-silicon.html) | 4 min | 2026-08-10 |
| 011 | [The Leaderboard Is a Press Release](articles/the-leaderboard-is-a-press-release.html) | 6 min | 2026-10-07 |
| 012 | [The Channel Is the Vulnerability](articles/the-channel-is-the-vulnerability.html) | 6 min | 2026-10-07 |
| 013 | [Instructions Are Suggestions. Credentials Are Policy.](articles/instructions-are-suggestions-credentials-are-policy.html) | 6 min | 2026-10-07 |
| 014 | [The Token Price Is Falling. Your Bill Isn't.](articles/the-token-price-is-falling-your-bill-isnt.html) | 6 min | 2026-10-07 |
| 015 | [Approval Is Not Oversight](articles/approval-is-not-oversight.html) | 6 min | 2026-10-07 |
| 016 | [Renting Your Own Moat](articles/renting-your-own-moat.html) | 8 min | 2026-04-14 |
| 017 | [Taming Kills the Wolf](articles/taming-kills-the-wolf.html) | 8 min | 2025-03-11 |
| 018 | [What Postmortems Bury](articles/what-postmortems-bury.html) | 7 min | 2025-04-24 |

## Running Locally

```bash
git clone https://github.com/iggym/applied-ai-engineering.git
cd applied-ai-engineering
python3 -m http.server 8000
# Open http://localhost:8000
```

No build step, dependencies, or compilation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, checklist, and the full authoring framework in `docs/master-prompt-v1.md`.

Validate before submitting:
```bash
python3 scripts/validate-metadata.py
```

## Validation & CI

- GitHub Actions runs on every PR
- Validates metadata schema and consistency
- Link checker (lychee) on all articles

## License

Creative Commons. See LICENSE for details.
