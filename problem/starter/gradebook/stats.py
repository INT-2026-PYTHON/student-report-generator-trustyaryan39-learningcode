"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    average_scores = {}
    for record in records:
        name = record["name"]
        score = record["score"]
        if name in average_scores:
            average_scores[name].append(score)
        else:
            average_scores[name] = [score]

    # Calculate averages for each student
    for name in average_scores:
        average_scores[name] = round(sum(average_scores[name]) / len(average_scores[name]), 2)

    return average_scores


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    subjects = set()
    for record in records:
        subjects.add(record["subject"])
    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    average_scores = average_per_student(records)
    max_average = max(average_scores.values())
    for name, average in average_scores.items():
        if average == max_average:
            return name, average_scores[name]
    return None, 0.0


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    average_scores = average_per_student(records)
    passing = [name for name, average in average_scores.items() if average >= threshold]
    return sorted(passing)
