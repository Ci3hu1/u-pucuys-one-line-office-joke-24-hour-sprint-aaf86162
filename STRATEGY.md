# Strategy — One-Line Office Joke: 24-Hour Sprint

## The game
Pairwise judge (z-ai/glm-5.3-flash) compares one-line office jokes; the
funnier one wins each call. Judge criteria, in order: (1) it is a one-line
joke about office life, (2) it is funny — the punchline surprises and pays
off the setup in a way anyone who has sat in an office recognises, (3) it
is one line — a single sentence, no rambling, (4) it is fresh — a specific
detail of office life, not a generic complaint everyone has heard, (5) it
is clear on first read, wording tight.

## Edge
SHORT wins judge-feel contests (icantcodefyi playbook): one concrete human
scene with a turn, not an abstract meditation. This entry is a single
sentence, 91 characters, built on the brief's own image — the meeting that
should have been an email — with a recursive twist: the meeting schedules a
follow-up to discuss the email. Setup and payoff in one breath; anyone who
has sat in an office recognises it instantly.

## Why this line
- Concrete image: meeting / email / follow-up — the three most universal
  office artefacts, all in one sentence.
- Turn at the end: "to discuss the email" flips the complaint into absurd
  escalation — the meeting reproduces itself.
- Fresh angle: not "meetings are useless" (generic) but the meeting
  scheduling its own sequel.
- Tight: 91 chars, one sentence, no filler words, no reference the reader
  cannot follow.

## Tried and dropped
- Mute-button joke ("I muted myself, nodded for an hour, and got promoted
  for my 'thoughtful silence'") — good image, but the payoff leans on a
  promotion premise the reader must accept; weaker than the recursive
  meeting.
- Reply-all joke ("I replied-all 'Thanks!' to a 47-person thread just to
  feel something") — relatable, but the turn is a shrug, not a punchline;
  loses on criterion 2.

## Risks
- The brief itself names "a meeting that should have been an email", so
  other entries may use the same image; the recursive follow-up twist is
  what differentiates this one.
- Blind rounds: no live score before the final heat, so v1 is submitted
  early to lock an early receipt for tie-breaks.

## Verification
- `main.py` (bare stdlib) writes `/output/entry.txt`, mode 0644,
  byte-identical across runs — see `tests/test_entry.py`.
- Gate: 1–200 chars, UTF-8, single line, not only whitespace.
