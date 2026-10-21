import json
import app


def test_create_ticket(monkeypatch, tmp_path):
    ticket_file = tmp_path / "tickets.json"
    ticket_file.write_text("[]", encoding="utf-8")

    monkeypatch.setattr(
        app,
        "load_tickets",
        lambda: json.loads(ticket_file.read_text(encoding="utf-8"))
    )

    def save(tickets):
        ticket_file.write_text(json.dumps(tickets), encoding="utf-8")

    monkeypatch.setattr(app, "save_tickets", save)

    answers = iter(["Order delayed", "Not received", "High"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    app.create_ticket()

    tickets = json.loads(ticket_file.read_text(encoding="utf-8"))

    assert len(tickets) == 1
    assert tickets[0]["title"] == "Order delayed"
    assert tickets[0]["priority"] == "High"
    assert tickets[0]["status"] == "Open"


def test_reject_invalid_priority(monkeypatch, tmp_path, capsys):
    ticket_file = tmp_path / "tickets.json"
    ticket_file.write_text("[]", encoding="utf-8")

    monkeypatch.setattr(
        app,
        "load_tickets",
        lambda: json.loads(ticket_file.read_text(encoding="utf-8"))
    )

    def save(tickets):
        ticket_file.write_text(json.dumps(tickets), encoding="utf-8")

    monkeypatch.setattr(app, "save_tickets", save)

    answers = iter(["Order delayed", "Not received", "Urgent"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    app.create_ticket()

    tickets = json.loads(ticket_file.read_text(encoding="utf-8"))

    assert tickets == []
    assert "Invalid priority" in capsys.readouterr().out
