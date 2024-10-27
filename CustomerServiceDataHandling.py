service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    #task: Open a new service ticket
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

def update_ticket_status(ticket_id, status):
    #task: Update the status of an existing ticket
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status

def display_tickets(status=None):
    #task: Display all tickets or filter by status
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details['Customer']} - {details['Issue']} - {details['Status']}")
