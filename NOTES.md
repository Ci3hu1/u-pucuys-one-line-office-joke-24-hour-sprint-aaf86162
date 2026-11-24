# Build notes — One-Line Office Joke: 24-Hour Sprint

- Slug: `u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162`
- Prize: $2 total, top 8 ($0.64 / $0.45 / $0.31 / $0.22 / $0.15 / $0.11 / $0.07 / $0.05)
- Closes: 25 Nov 2026 12:50 WIB (05:50 UTC); results 16 Dec 2026
- Harness: program/v1 — program writes one text to `/output/entry.txt`
- Gate: UTF-8, 1–200 chars, not only whitespace; single line
- Judge: pairwise, z-ai/glm-5.3-flash; blind rounds (no live rank/score
  until results); next round 2026-11-24T13:51:04Z
- Field at triage: 0 submissions (empty table)
- Kit: fresh download, level 40 (`u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162-kit.tar.gz`)
- Entry: FREE, no prerequisites

## Candidates (all single sentences, under 200 chars)

1. "The meeting that should have been an email just scheduled a follow-up
   to discuss the email." — 91 chars — PICKED.
2. "I muted myself, nodded for an hour, and got promoted for my
   'thoughtful silence'." — 79 chars.
3. "I replied-all 'Thanks!' to a 47-person thread just to feel something."
   — 70 chars.

## Why #1
One concrete office scene (meeting → email → follow-up) with the twist at
the very end: the meeting reproduces itself. Single sentence, instantly
recognisable, tight wording, and the recursive angle is fresher than a
plain "meetings are useless" complaint. #2's payoff depends on accepting a
promotion premise; #3's turn is a shrug rather than a punchline.

## Build record
- v1 built 24 Nov 2026 ~13:0x WIB in a fresh session after opening
  (opened 2026-11-24T05:51:37Z).
- `main.py`: bare stdlib, writes `/output/entry.txt`, mode 0644.
- Tests: `python3 -m unittest discover -s tests -v` — 5 tests (see below).
- Kit check: `node cli/makefun.mjs check` from the fresh kit — see below.
- Repo: https://github.com/Ci3hu1/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162
- NOT bundled, NOT submitted — awaiting Joni's 'Setuju' on the exact entry.

## Test results
- `python3 -m unittest discover -s tests -v`: 5/5 OK (one line ≤200 chars,
  no trailing blank line, byte-identical reruns, mode 0644, stdlib only).
- Joke: 91 chars; file 92 bytes incl. trailing newline; sha256
  c045894989977c0647fec6fd311aba767bfa257995fda1d9c88ac162b004e96a (identical
  across 2 runs).

## Kit check result
- `node cli/makefun.mjs check` (fresh kit, level 40): 4 passed, 1 failed,
  14 skipped, 5 checked at submission.
- Passed: competition_open, snapshot, license_osi, entrypoint.
- Failed: transcripts_present only — expected pre-bundle; the bundle is
  made later by the top-level agent.
- At-submission checks (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) are verified at submit time; repo is
  public, created after opening, commit pushed.

## Live score / rank
- Blind rounds: no live score until results. (Fill after submit + rounds.)
