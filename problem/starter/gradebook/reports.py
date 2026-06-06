"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    print("=== Gradebook Report ===")
    print(f"Total records: {len(records)}")
    print(f"Subjects offered: {', '.join(sorted(subjects_offered(records)))}")
    print()
    print("Averages:")
    for name, average in sorted(average_per_student(records).items()):
        print(f"  {name}: {average}")
    print()
    top_name, top_average = top_scorer(records)
    print(f"Top scorer: {top_name} ({top_average})")
    print("Passing students (>= 60.0): ",end="")
    for name in passing_students(records):
        print(f"{name}, ", end="")
    print()
