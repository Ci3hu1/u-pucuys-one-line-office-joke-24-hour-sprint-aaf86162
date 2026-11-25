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
- SUBMITTED 24 Nov 2026 ~13:26 WIB on Joni's "Setuju semua": entry commit 3ecda213aa7c3f908b0c48718ff62e0f6b51303f (HEAD, notes commit on top of entry 33fd062), main, pushed, ls-remote verified. Bundle ~/workspace/tools/makefun/bundles/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.tar.gz, sha256 d57b4787f6de4536dfbd624e872c0a627f653994c76cb8997b9bbb98fa5774a7 (155,794 B; builder session 74d993f7, 1 usage row). Kit check ok=true, failed=[]. Submission 01a20c3b-808d-70ce-96d4-1e4e20be8394, stage submitted (grading queue behind at submit). Blind 3 rounds, counts from round 1 (cutoff 24 Nov 13:51:04 UTC / 20:51 WIB). Claim code saved only to ~/.config/makefun/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162-submission.json (0600).

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

## v2 (25 Nov 2026 ~10:20 WIB, on Joni's "Buat v2 ketiganya")
- R2 result: #1324/2931, 55.56% — best of the batch; v1's specific-scene structure (meeting → email → follow-up) is what worked. No judge reasons (blind rounds).
- v2 line (90 chars, Python len): "Dave from accounting replied-all to 214 people to say 'Please remove me from this thread'."
- ONE specific detail: Dave from accounting + 214 people — a proper noun and a number, a concrete scene no other entry has.
- Changes: JOKE swapped; added validate() (1-200 chars, not blank, one line, no control chars, at least one letter/digit) + read-back self-check + ENTRY_OUTPUT env; 3 new tests (8/8 pass).
- Entry commit 276d04709f4ebd7223846777f17b875400287ad7, main, pushed, ls-remote verified.
- Bundle ~/workspace/tools/makefun/bundles/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162-v2.tar.gz (253,899 B; sessions 74d993f7 + fix session 3c575f98, 1 usage row — the v1 builder's; fix session's row attaches on re-bundle before submit).
- Kit check ok=true, failed=[] (fresh kit level 42; reproduces 203/219 = 92.6%, revised pass (3 messages), in_window pass, priced pass). NOT submitted — awaiting Joni's 'Setuju' on this exact v2.
