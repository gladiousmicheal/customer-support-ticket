import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tickets.json"


def load_tickets():
    """Load saved tickets from the JSON file."""
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tickets(tickets):
    """Save tickets to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)
