# Build a `gradebook` Package — Student Grade Analyzer

A single, end-to-end problem that walks you through building a small Python **package** made of multiple **modules** that import from each other. You will practice the fundamentals that show up in almost every real Python project — **without** any file I/O.

---

## What you'll learn

| Concept | Where it shows up in this problem |
| --- | --- |
| **Packages** (folder with `__init__.py`) | The `gradebook/` folder |
| **Modules** (`.py` files inside a package) | `data.py`, `stats.py`, `reports.py` |
| **Imports** (absolute + relative) | `main.py` and inside the package |
| **Data structures** | `list[dict]`, `dict[str, float]`, `set[str]`, `tuple[str, float]`, `dict[str, list[int]]` |
| **Comprehensions & aggregation** | `sum()`, `max()`, `sorted(..., key=...)` |
| **Type hints & docstrings** | Every function in the package |

---

## The scenario

You're given a list of student grade records already loaded into memory (see `gradebook/data.py`). Each record is a dictionary:

```python
{"name": "Alice", "subject": "Math", "score": 88}
```

Build a package called `gradebook` that turns this raw list into useful statistics and a readable report.

---

## Required project layout

```text
starter/
├── gradebook/
│   ├── __init__.py   # marks gradebook as a package + re-exports public API
│   ├── data.py       # already provided — the hardcoded RECORDS list
│   ├── stats.py      # YOU implement — pure functions over records
│   └── reports.py    # YOU implement — uses stats.py via a relative import
└── main.py           # entry point — run this
```

Run the program with:

```bash
cd starter
python3 main.py
```

---

## Module-by-module specification

### 1. `gradebook/data.py`  *(already provided — do not modify)*

```python
RECORDS: list[dict] = [
    {"name": "Alice",   "subject": "Math",    "score": 88},
    {"name": "Alice",   "subject": "Science", "score": 92},
    ...
]
```

### 2. `gradebook/stats.py`  *(YOU implement)*

```python
def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score (rounded to 2 decimals)."""

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects in the records."""

def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
```

### 3. `gradebook/reports.py`  *(YOU implement)*

```python
def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report using the functions in stats.py.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
```

This module **must** import from `stats.py` using a **relative import**:

```python
from .stats import average_per_student, subjects_offered, top_scorer, passing_students
```

### 4. `gradebook/__init__.py`  *(YOU implement)*

Re-export the public API so callers can write `from gradebook import RECORDS, format_report`:

```python
from .data import RECORDS
from .reports import format_report
```

### 5. `main.py`  *(already provided)*

```python
from gradebook import RECORDS, format_report

if __name__ == "__main__":
    print(format_report(RECORDS))
```

---

## Expected output

```text
=== Gradebook Report ===
Total records: 12
Subjects offered: English, Math, Science

Averages:
  Alice   : 86.33
  Bob     : 82.33
  Charlie : 91.33
  Diana   : 65.0

Top scorer: Charlie (91.33)
Passing students (>= 60.0): Alice, Bob, Charlie, Diana
```

> Exact whitespace/alignment can vary, but every labeled section must be present.

---

## Hints

- **Group scores per student:** build a `dict[str, list[int]]` first (use `dict.setdefault(name, []).append(score)`), then compute averages.
- **Unique subjects:** a set comprehension — `{r["subject"] for r in records}`.
- **Top scorer:** `max(averages.items(), key=lambda kv: kv[1])` returns the `(name, avg)` tuple with the largest average.
- **Sorting:** `sorted(names)` sorts alphabetically; `sorted(items, key=...)` sorts by a custom key.
- **Relative vs absolute import:**
  - *Inside* the package → `from .stats import ...` (the dot means "current package").
  - *Outside* the package → `from gradebook import ...`.
- **Why `__init__.py`?** It tells Python "this folder is a package." Without it, `import gradebook` fails.

---

## Suggested order to implement

1. Open the `starter/` folder.
2. Implement the four functions in `stats.py` and test them quickly:

   ```python
   from gradebook.data import RECORDS
   from gradebook.stats import average_per_student
   print(average_per_student(RECORDS))
   ```

3. Implement `reports.format_report` that calls into `stats.py` via a relative import.
4. Wire `__init__.py` to re-export `RECORDS` and `format_report`.
5. Run `python3 main.py` and compare to the expected output.

---

## Stretch goals (optional)

- Add a 5th function `lowest_subject(records) -> tuple[str, float]` — the subject with the lowest class average.
- Add a `gradebook/__main__.py` so you can run the package directly with `python3 -m gradebook`.
- Write `pytest`-style tests for each `stats.py` function.

---

## Files in this repo

| Path | Purpose |
| --- | --- |
| [problem/starter/](starter/) | Empty scaffolding — start here |
| [problem/solution/](solution/) | Reference implementation (peek only after trying) |
