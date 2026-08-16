# Handover: Nalex Visualization — Final Polishing Pass

**To:** Antigravity agent (Sonnet 4.6, thinking)
**From:** prior session (Claude, Cowork mode)
**Date:** 2026-08-09
**Task:** final polishing of the Nalex visualization artifact set. Read this whole document before touching any file — §1 and §2 are not optional context, they change what "polishing" is allowed to mean here.

---

## 0. Read first: this is not a normal design task

This project analyses private message logs between two real people (Naomi and Alex) who are not present to consent to how they're characterised. The project rules exist to prevent the analysis from drifting into coaching, blame, or fabricated data, and they bind *you*, not just the prior session. Violating them is the one failure mode that can't be fixed by a later polishing pass, because it would mean the artifact said something about a real person that isn't supported by evidence.

Read `CLAUDE.md` (global, private instructions) and `index.md` (project map) in full before doing anything else. The short version, repeated in four places in this repo in near-identical wording:

> Analysis only. No coaching, no message drafting, no advice, no prescriptions for real-world action. Every claim is either Evidence (measured, reproduces from `events.jsonl`) or Interpretation (inference, explicitly labelled, never presented as fact). No diagnosis, no pathologising, no fixed personality labels. Roles are situational, not identities.

If a polishing task would add a script for what someone should say, a fixed role label (e.g. "the avoidant one"), a completion/gamification mechanic, or any figure not traceable to a source file — don't do it, and say so instead of doing a softened version of it.

---

## 1. Unresolved conflict you need to surface, not resolve

There are **two independent, non-integrated specifications for what "the canonical Nalex render" is**, and they were never reconciled:

**Track A — the flashcards artifact.**
`visualisations/nalex_patterns_flashcards.html`. A 23-card, 5-section, fully interactive document (filters, sticky bar, glossary tooltips, focus mode, sparklines) covering the whole evidence base. Built and iteratively verified across several sessions; currently the file this repo's own status notes call canonical (see `visualisations/visualization_input_manifest.txt` and recent session validation).

**Track B — the 3C spec.**
`visualisations/nalex_viz_canonical_render_spec.md`, backed by `visualisations/nalex_viz_ideation.md`, `research_prompt_modes/viz_schema_template.md`, `research_prompt_modes/visualization_pipeline.md`, and `research_prompt_modes/analysis_outputs/nalex_viz_schema.json`. This document specifies a *different* artifact — one static card-based render (variant "3C," a single claim about initiation/closure) built through a mandatory flatten-then-render pipeline, and it is explicit that the first canonical render **must not** have interactivity, hover states, tooltips, or filters (§1.4). It does not mention the flashcards file at all. It supersedes nothing, by its own §1.1 — it was written as if the flashcards file didn't exist.

**These directly conflict.** Track B's exclusion list is close to a description of what makes the flashcards file distinctive. Neither document acknowledges the other.

**Do not silently pick one.** Do not delete, rewrite, or fold one into the other as part of "polishing." Produce a short written note (a few sentences is enough) naming the conflict for the project owner, and ask which track is authoritative before doing anything that assumes an answer. If forced to proceed without an answer, treat Track A (flashcards) as the polishing target, since it's the one the repo's own recent commits and manifest treat as current — but flag that this is a default, not a resolution.

---

## 2. Environment hazards — read before running any command

**No Git.** The project owner's explicit, current instruction is: *"Do not use Git, commits, staging, branches, locks, or repository status commands. This is a local project without Git. Treat the filesystem as the source of truth."* This is a deliberate policy change made after repeated failures, not a suggestion. Do not run `git status`, `git add`, `git commit`, or anything else in the git namespace. Verify your work with direct file reads, `shasum`, `wc`, `grep`, `stat` — not git.

**Why git was abandoned here, for your own situational awareness (not an invitation to fix it):** this repo lives on a FUSE mount bridged to the user's actual Mac (paths like `/Users/okgoogle13/Projects/Nalex`). It has 64,393 tracked files and ~50,000 loose git objects — well past git's auto-gc threshold — and every `git commit` triggers an index refresh that stats the whole tree over network-backed FUSE. In the prior session this reliably hung past every available timeout (up to ~178s), even with `gc.auto=0`. A low-level plumbing workaround (`write-tree` / `commit-tree` / `update-ref`, bypassing the index refresh) got partway before the owner asked to drop git entirely for this project. Don't attempt to fix the git performance problem as part of a polishing task — it's out of scope and the owner has already redirected around it.

**The workspace folder has delete/rename protection.** Files under `/Users/okgoogle13/Projects/Nalex` cannot be deleted or renamed by normal filesystem calls — this is enforced by the host environment, not a permissions bug. If you need to remove or rename something, you'll need the equivalent of this session's `allow_cowork_file_delete` gate, which prompts the real user for approval. Don't work around a delete failure with a copy-then-leave-the-original-behind pattern; ask for the gate instead.

**Full-tree scans hang.** Never run a recursive operation (glob, find, git, grep) rooted at the repo root without excluding `.tmp.driveupload/` (a ~46,000-file Google Drive upload cache) — it's the single biggest cause of timeouts in this repo. It's listed in `.gitignore` but that only matters for git, which you're not using; for shell commands, exclude it explicitly (`find . -path ./.tmp.driveupload -prune -o ...`, or scope every command to a specific subdirectory instead of the root).

**Corpus files are read-only in spirit even though not in permissions.** `events.jsonl` and everything derived from it (`aftermath_stats.json`, `baseline_comparison_audit.json`, `gap_stats_out.json`, `conflict_questions.txt`, `phase_profile.json`) must not be touched by a visual polishing pass. If a number on screen looks wrong, the fix is in the rendering file, never in the source data, and if the source data itself looks wrong, that's an escalation, not a same-session edit.

---

## 3. Current file inventory (`visualisations/`)

| File | Status | Notes |
|---|---|---|
| `nalex_patterns_flashcards.html` | **Canonical (Track A), pending §1 resolution** | 23 cards, 5 sections, verified against source data across multiple sessions. Every figure traces to `phase_profile.json`; every quote traces verbatim to `conflict_questions.txt` / `CURRENT_STATE_CLEAN.md`. Currently correct: Alex Baseline = 927 words (not 928 — that figure belongs only to Naomi's Aftermath longest single turn, which appears 3 times and must stay 928). |
| `nalex_playbook_dark_m3.html` | **Explicitly out of mode — do not touch its content** | Marked with a banner, title prefix, and meta tag identifying it as an exploratory coaching prototype, not evidence. Contains prescriptive language ("Moving Forward," scripted phrases) that must never be merged into the canonical artifact. Leave the labelling and the content as-is; if it needs polishing at all, only the out-of-mode banner styling qualifies, never the prescriptive text underneath it. |
| `visualization_input_manifest.txt` | Current | SHA-256 of the 5 files `viz_schema_template.md` treats as pipeline inputs. Regenerate only if you edit one of those 5 named files; do not add the flashcards file or any render to this manifest — it is an *input* manifest, not an output list. |
| `nalex_mobile_infographic_render.html` | **Excluded from canonical set — leave excluded** | Contains fixed role labels ("Exhaustive Processor," "Cost Controller"), moralising language ("weaponized," "accountability failures"), and a direct prescription ("Initiate Two-Lane Repair"). Its pronoun-count figures also aren't in the manifest's input set. Do not reference, link, or merge this file into the canonical artifact during polishing. |
| `nalex_mobile_v1_playful.html`, `_v2_polished.html`, `_v3_dramatic.html` | **Not reviewed this handover — triage before touching** | Not audited in the sessions this handover summarises. Read each before assuming it's safe to use as a polishing reference; they may carry the same Track-B assumptions or off-mode language as the files above. |
| `nalex_viz_ideation.md`, `nalex_viz_canonical_render_spec.md`, `nalex_mobile_infographic_schema.json` | Track B documents | See §1. Do not execute this pipeline as part of "final polishing" without the conflict in §1 being resolved by the project owner. |
| `.gitignore` (repo root) | Current | Excludes `.tmp.driveupload/` and `.DS_Store`. Not relevant to your work if you're following §2 (no git), but leave it in place. |

---

## 4. What "final polishing" means, scoped to Track A only

Assuming §1 resolves in favour of the flashcards file (or you're told to proceed with it as the default per §1's guidance), the outstanding items are:

1. **Mobile viewport verification.** Never actually rendered — no browser tooling was available in the prior session. Check at minimum a 412×915 portrait viewport (a common Android/Pixel size): sticky control bar height and wrapping, tap target sizes on the phase/lens chips, sparkline legibility, tension-card side-by-side layout (it has a documented fallback to stacked at 640px — confirm it actually triggers and reads well).
2. **`prefers-reduced-motion` verification.** The CSS has a reduced-motion block that disables transitions/animations and hover-lift. Confirm it actually suppresses everything it should (card open/close, hover lift, chip state changes) rather than just the ones explicitly listed.
3. **Light/dark and contrast check.** The file uses a single warm light palette by design (no dark mode was built) — confirm this was intentional before adding one; don't silently introduce a dark mode as "polish" without checking whether that was ever asked for.
4. **Accessibility pass.** `aria-expanded` / `aria-pressed` are used throughout; verify they're both present and correctly wired to visual state after any markup changes. Glossary tooltips use `tabindex` and `focusin`/`focusout` for keyboard access — verify tab order is sane, especially inside the sticky bar with its three chip groups.
5. **Visual QA via screenshot**, if you have browser/screenshot tooling available (the prior session did not). This is the single biggest gap in the current verification: every check so far has been structural (grep, hash, DOM parse) — nothing has been visually confirmed to render correctly.

## 5. What is explicitly *not* in scope for this pass

Carried forward from an earlier design-review round in this project and still binding:

- **No shuffle.** Card order is load-bearing — findings are sequenced before the caveats that qualify them.
- **No completion/progress mechanics** (cards-flipped counters, etc.) on a document analysing a relationship breakdown.
- **No reflection prompts** ("How would you have read this message?") — that's facilitation, which the project rules exclude.
- **No data-driven visual sizing that implies fault** (e.g., avatar size scaled to word count) — this was rejected earlier as encoding blame through design rather than text.
- **No merging of Track B's flatten-then-render pipeline, its interactivity ban, or `nalex_playbook_dark_m3.html`'s prescriptive language** into the canonical artifact, per §1 and §3 above.

## 6. Verification standard to hold yourself to

Every prior session on this project has been caught making at least one factual error before catching it in verification (a rounded quote, a stale figure, a wrong file assumed not to exist). Don't skip the equivalent step here:

- Any number you touch: re-derive it from `phase_profile.json` or `CURRENT_STATE_CLEAN.md` directly, don't trust a cached figure from this handover or from the file you're editing.
- Any quote you touch: confirm it's verbatim against `conflict_questions.txt` or `CURRENT_STATE_CLEAN.md`, including profanity — several early drafts in this project's history softened quotes by dropping expletives, which was flagged as a real problem (sanitising a real person's words in a document they may read is its own kind of distortion).
- Before finishing: re-run the structural checks the file already has a track record of passing — Evidence/Interpretation block counts equal 23 each, quote count 31, zero external network requests, single `<html>/<body>/<script>/<style>` blocks, no prescriptive language leaked in from the playbook file.

## 7. Report back

When you're done, report: what you resolved on the §1 conflict (or that you flagged it and stopped), which of the §4 polish items you completed, what you found in the untriaged `_v1`/`_v2`/`_v3` mobile files, and the exact verification commands you ran with their output — not just "verified," the actual evidence.
