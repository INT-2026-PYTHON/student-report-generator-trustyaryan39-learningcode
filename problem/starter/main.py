"""Entry point — run with `python3 main.py` from the starter/ directory."""

from gradebook import RECORDS, format_report


if __name__ == "__main__":
    format_report(RECORDS)
