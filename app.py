
from storage import load_tickets, save_tickets

PRIORITIES = ["Low", "Medium", "High"]
STATUSES = ["Open", "In Progress", "Closed"]


def create_ticket():
    tickets = load_tickets()

    title = input("Enter ticket title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    description = input("Enter description: ").strip()

    print("Priorities: Low, Medium, High")
    priority = input("Enter priority: ").strip().title()

    if priority not in PRIORITIES:
        print("Invalid priority. Ticket not created.")
        return

    ticket_id = max(
        (ticket["id"] for ticket in tickets), default=0
    ) + 1

    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(ticket)
    save_tickets(tickets)
    print(f"Ticket #{ticket_id} created successfully!")


def view_tickets(tickets=None):
    if tickets is None:
        tickets = load_tickets()

    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print("-" * 40)
        print(f"ID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")


def search_tickets():
    keyword = input("Enter a title or description keyword: ").strip().lower()
    tickets = load_tickets()

    results = [
        ticket for ticket in tickets
        if keyword and (
            keyword in ticket["title"].lower()
            or keyword in ticket["description"].lower()
        )
    ]

    view_tickets(results)


def edit_ticket():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID to edit: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    ticket = next(
        (item for item in tickets if item["id"] == ticket_id), None
    )

    if ticket is None:
        print("Ticket not found.")
        return

    title = input(f"New title [{ticket['title']}]: ").strip()
    description = input("New description (press Enter to keep current): ").strip()

    if title:
        ticket["title"] = title
    if description:
        ticket["description"] = description

    priority = input(
        f"New priority [{ticket['priority']}] (Low/Medium/High): "
    ).strip().title()

    if priority:
        if priority not in PRIORITIES:
            print("Invalid priority. Changes not saved.")
            return
        ticket["priority"] = priority

    save_tickets(tickets)
    print("Ticket updated successfully!")


def update_status():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    ticket = next(
        (item for item in tickets if item["id"] == ticket_id), None
    )

    if ticket is None:
        print("Ticket not found.")
        return

    print("Statuses: Open, In Progress, Closed")
    status = input("Enter new status: ").strip().title()

    if status not in STATUSES:
        print("Invalid status.")
        return

    ticket["status"] = status
    save_tickets(tickets)
    print("Ticket status updated successfully!")


def main():
    while True:
        print("\n=== Customer Support Ticket System ===")
        print("1. Create ticket")
        print("2. View all tickets")
        print("3. Search tickets")
        print("4. Edit ticket")
        print("5. Update ticket status")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            search_tickets()
        elif choice == "4":
            edit_ticket()
        elif choice == "5":
            update_status()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()

