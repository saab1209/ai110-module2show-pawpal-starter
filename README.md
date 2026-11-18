# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```
=== Today's Schedule for Salma ===
1. [08:00] Bella - Morning Walk (Walk | High | Daily) [Pending]
2. [08:15] Milo - Breakfast & Thyroid Pill (Medication | High | Daily) [Pending]
3. [18:00] Bella - Evening Kibble (Feeding | Medium | Daily) [Pending]
4. [19:30] Milo - Play & Brush Session (Enrichment | Low | Once) [Pending]

Detected Time Conflicts: 1
  - Overlap: 'Morning Walk' (08:00) overlaps with 'Breakfast & Thyroid Pill' (08:15)


## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
python -m pytest --cov
```

Sample test output:

```text
============================== test session starts ==============================
collected 6 items

tests/test_pawpal.py ......                                               [100%]

============================== 6 passed in 0.03s ===============================
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()`, `Scheduler.get_daily_schedule()` | Parses 24-hour `"HH:MM"` times into minutes since midnight for chronological ordering, or sorts by `High` → `Medium` → `Low` priority. |
| Filtering | `Scheduler.filter_tasks()` | Filters household tasks dynamically by `pet_name` and completion status (`all`, `pending`, or `completed`). |
| Conflict handling | `Scheduler.detect_conflicts()` | Checks `[start, start + duration_minutes)` intervals across all pets and returns warning pairs without crashing the app. |
| Recurring tasks | `Task.mark_complete()`, `Scheduler.complete_task()` | Uses `datetime.timedelta` (`+1 day` for `Daily`, `+7 days` for `Weekly`) to auto-schedule the next pending task upon completion. |

## 📸 Demo Walkthrough

1. **Launch the App & View Household State:** Start the interface with `streamlit run app.py`. `st.session_state` initializes an `Owner` profile (*Salmaa*) with two pre-loaded pets (*Bella* the Dog and *Milo* the Cat) so data persists across every click.
2. **Register a New Pet (Sidebar):** Enter a pet's name, species, and age in the **Add a New Pet** form and click **Register Pet** to add it to `owner.pets` and view live pending task counts.
3. **Schedule a Care Routine:** Select a pet in **Schedule a Pet Care Task**, enter a task title, category (`Feeding`, `Walk`, `Medication`, `Appointment`, `Enrichment`), 24-hour time, duration, priority, and recurrence frequency, then click **Add Care Task**.
4. **Review Conflict Warnings & Filter Schedule:** Any overlapping tasks (such as *Bella's Morning Walk* at `08:00` for 30m and *Milo's Thyroid Medication* at `08:15` for 15m) automatically trigger an `st.warning` banner. Use the dropdown controls to sort by time or priority and filter by pet or status.
5. **Complete Routines & Trigger Recurrence:** Click **Complete** next to any pending task to mark it done; if the task is `Daily` or `Weekly`, PawPal+ immediately queues the next scheduled occurrence and shows a confirmation toast.

### Sample CLI Output (`python main.py`)
```text
=== Today's Schedule for Salmaa ===
1. [08:00] Bella - Morning Walk (Walk | High | Daily) [Pending]
2. [08:15] Milo - Thyroid Medication (Medication | High | Daily) [Pending]
3. [18:00] Bella - Evening Kibble (Feeding | Medium | Daily) [Pending]
4. [19:30] Milo - Play & Brush Session (Enrichment | Low | Once) [Pending]

Detected Time Conflicts: 1
  - Overlap: 'Morning Walk' (08:00) overlaps with 'Thyroid Medication' (08:15)
```
