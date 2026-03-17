# MusicFlow – Project Scan Notes

_Last updated: 2026-03-17 (UTC)_

## 1) Study scope (current target)

Current intended **full study run**:
- `Intro`
- `EEG_Setup`
- `Research`
- `Matching`
- `Outro`

Legacy/pretest apps (`Transcription`, `N_back`, etc.) still exist in repo but are **not part of current full-run priority**.

---

## 2) Runtime + architecture

### Stack
- Python + oTree (`otree==5.10.4`)
- Entry: `manage.py`
- Config: `settings.py`
- Deployment helper: `Procfile`

### App roles (high-level)
- `Intro`: demographics, state baseline, music playlist selection, treatment order assignment
- `EEG_Setup`: resting baseline blocks (eyes open/closed, with/without music)
- `Research`: paper reading + note-taking task
- `Matching`: data-checking / matching task
- `Outro`: trait and music-at-work questionnaires

### Shared resources
- `_static/music/`: background tracks
- `_static/papers/`: PDFs used by Research task
- `_static/*.csv`: synthetic task data pools
- `_templates/global/`: shared questionnaire/page templates

---

## 3) Session configs (updated)

In `settings.py`:
- `full_research_first`: `Intro -> EEG_Setup -> Research -> Matching -> Outro`
- `full_matching_first`: `Intro -> EEG_Setup -> Matching -> Research -> Outro`

This supports **task-order counterbalancing** at the session-config level.

---

## 4) Counterbalancing logic (updated)

### Treatment order assignment
In `Intro`, treatment order is now **alternating** (not random):
- odd `id_in_subsession` → `['music', 'control']`
- even `id_in_subsession` → `['control', 'music']`

This gives deterministic balancing within a session.

### Within-task crossover
`Research` and `Matching` remain `NUM_ROUNDS = 2`:
- round 1 uses `participant.treat_order[0]`
- round 2 uses `participant.treat_order[1]`

So each participant does each task once with music and once without.

---

## 5) Task timing + in-task ESM (updated)

### Task duration
- `Research` task duration: **15 min** per round
- `Matching` task duration: **15 min** per round

### ESM popup behavior
Implemented in task templates (JS/HTML level, no separate page):
- Popup appears at **5:00** and **10:00** during each task round
- Uses questionnaire-style table layout
- Captures 3 FKS items:
  - `fks6`: “I was totally absorbed in what I am doing.”
  - `fks8`: “I knew what I had to do each step of the way.”
  - `fks9`: “I felt that I have everything under control.”

### ESM storage fields
Added to both `Research.Player` and `Matching.Player`:
- `esm5_fks6`, `esm5_fks8`, `esm5_fks9`
- `esm10_fks6`, `esm10_fks8`, `esm10_fks9`

---

## 6) Post-task ESM burden checks (new)

Added 2 items to `TaskQuestionnaire` in both `Research` and `Matching`:
1. “The three questions that came as a check-in during the task were disrupting my focus.”
2. “It was easy for me to get back in focus after answering the three questions.”

These are rendered in their own **7-point Likert table**.

---

## 7) Likert-scale policy adjustments

### Project rule applied
All odd-point Likert scales were standardized to **7-point**.

### Exception retained
**SAM pleasure/arousal stay 5-point** (as explicitly requested).

### Template header alignment
Questionnaire templates were updated to match 7-point structure where needed (added missing `<th>` spacer columns so table headers align with 7 choices).

Files touched include task questionnaire templates and global questionnaire templates.

---

## 8) Git + collaboration setup notes

- Repo cloned to workspace and managed on branch `main`
- Remote switched from HTTPS to SSH for unattended push from VPS
  - now uses: `git@github.com:fabiostano/musicflow.git`
- SSH auth on VPS verified against GitHub account

Recent relevant commits pushed:
- `842e24a` – full-study flow + alternating treatment + 15-min tasks + first ESM implementation
- `da37b18` – ESM refinements + 7-point odd Likert standardization
- `36bea19` – SAM back to 5-point + Likert table-header alignment

---

## 9) Known caveats / follow-up checks

1. **Inline credentials in `settings.py`**
   - `ADMIN_PASSWORD` and `SECRET_KEY` are in code; should be moved to env vars for production.

2. **Legacy app consistency**
   - Repo still contains pretest/legacy modules; keep in mind when interpreting exports or maintaining templates.

3. **Template consistency audit**
   - After major scale-policy changes, run a visual pass in-browser over all active questionnaires to verify spacing and labels.

4. **Data dictionary needed**
   - Recommend adding a compact codebook for analysis:
     - construct mapping
     - scale direction
     - reverse-scored items
     - round/timepoint semantics (`esm5_*` vs `esm10_*`)

---

## 10) Suggested next practical step

Create `ANALYSIS_CODEBOOK.md` with:
- primary outcomes
- covariates/controls
- per-task/per-round variable list
- treatment coding conventions
- planned exclusion checks (attention checks, missing ESM, etc.)
