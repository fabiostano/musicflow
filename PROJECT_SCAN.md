# MusicFlow – Project Scan Notes

_Last updated: 2026-03-17 (UTC)_

## 1) What this project is

This is an **oTree-based behavioral study** project focused on the effect of **background music vs. control (no music)** on **flow and related outcomes** during knowledge-work-like tasks.

Core idea in code:
- Participant chooses a playlist in `Intro`
- Treatment order is randomized (`music` / `control`)
- Participants complete task rounds under both conditions
- Questionnaires capture flow, mind-wandering, workload, boredom, etc.

---

## 2) High-level architecture

### Runtime / framework
- Python + oTree (`otree==5.10.4`)
- Entry point: `manage.py`
- Main config: `settings.py`
- Deployment hint: `Procfile`

### Main app modules (oTree apps)
- `Intro` – demographics/state + playlist choice
- `EEG_Setup` – eyes-open/eyes-closed resting segments (music + non-music)
- `Research` – reading/notes task with scientific papers
- `Transcription` – transcription task using image snippets
- `N_back` – email-subject memory/response style task
- `Matching` – record matching/data-checking style task
- `Outro` – trait questionnaires + open questions
- `Music_Discovery` – separate music preference flow (currently not in most default session configs)

### Shared assets
- `_static/music/` – playlist audio + covers
- `_static/papers/` – PDFs for research task
- `_static/snippets/` – many image snippets for transcription-like tasks
- `_static/*.csv` – synthetic data pools for tasks (names, ids, job titles, etc.)
- `_templates/global/` – shared task/questionnaire template components

---

## 3) Session configs (important)

Defined in `settings.py` under `SESSION_CONFIGS`.

Key configs:
- `full_research_first`: `Intro -> EEG_Setup -> Research -> Transcription -> Outro`
- `full_transcription_first`: `Intro -> EEG_Setup -> Transcription -> Research -> Outro`
- Plus focused/pretest configs (`nback`, `matching`, `pretest`, etc.)

Observed behavior:
- Several task apps run with `NUM_ROUNDS = 2` to capture within-subject condition changes
- Treatment order is randomized and reused across rounds

---

## 4) How treatment assignment currently works

- `Intro/MusicSelection.before_next_page` sets:
  - `participant.playlist`
  - `participant.treat_order` as shuffled `['music', 'control']`

- Task apps (e.g., `Transcription`, `N_back`, `Matching`, `Research`) read:
  - round 1 → `treat_order[0]`
  - round 2 → `treat_order[1]`

This gives a clean within-subject crossover design.

---

## 5) Questionnaires / constructs currently represented

Across apps, many fields already implemented for:
- **Flow state** (SFSS variants)
- **Skill-demand balance**
- **Mind wandering (state/trait)**
- **Mental workload (NASA-TLX style single item)**
- **Boredom** (in N_back / Matching)
- **Affect / arousal / fatigue controls**
- **Music-at-work beliefs and behavior** (Outro, extensive)

Question ordering is often randomized in `get_form_fields` for reduced order effects.

---

## 6) Quick quality/risk notes from first scan

1. **Credentials in repo**
   - `settings.py` currently contains explicit `ADMIN_PASSWORD` and `SECRET_KEY` placeholders/values.
   - Should be moved to environment vars before production use.

2. **Potential off-by-one / indexing fragility in `Music_Discovery`**
   - Different pages use `playlist[round_number]` vs `playlist[round_number-1]` patterns.
   - Might be intentional due to page sequencing, but worth validating with a small pilot run.

3. **Data hygiene in static snippets**
   - `_static/snippets/` includes many duplicate-looking files (`copy` naming patterns).
   - Could inflate random pools and reduce control over stimulus balance.

4. **Typos/inconsistent wording in labels**
   - Several questionnaire labels have minor typos (`someting`, `ususal`, etc.).
   - Not functionally blocking, but relevant for participant-facing quality.

---

## 7) Suggested immediate next steps

1. **Run a full dry pass of `full_research_first` and `full_transcription_first`**
   - Verify treatment order, playlist handoff, timer behavior, and form persistence.

2. **Define analysis-ready export map**
   - Decide which fields are primary endpoints vs controls for first analyses.
   - Create a compact codebook (`field -> construct -> scale direction`).

3. **Add a short `README.md` focused on experiment operation**
   - Local run commands
   - Session config usage
   - Data export workflow
   - Environment variable requirements

4. **Harden config for production**
   - Remove inline secrets
   - Confirm `DEBUG=False`, auth level, and deployment settings.

---

## 8) Collaboration note

I’m now set up to work directly in this repo for:
- feature changes
- experiment logic updates
- bugfixes
- clean commits and pushes

When we start implementing, we should pick one of these first:
- **A)** methodology-focused cleanup (questionnaire structure/scales)
- **B)** runtime reliability pass (timers, treatment handoff, data fields)
- **C)** analysis pipeline prep (codebook + export scripts)
