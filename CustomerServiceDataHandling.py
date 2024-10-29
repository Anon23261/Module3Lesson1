# Dictionary to store service tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status

# Function to display all tickets or filter by status
def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details['Customer']} - {details['Issue']} - {details['Status']}")

# Testing the functions
# Open a new ticket
open_ticket("Ticket003", "Charlie", "Network issue")

# Update the status of an existing ticket
update_ticket_status("Ticket001", "closed")

# Display all tickets
print("All tickets:")
display_tickets()

# Display only open tickets
print("\nOpen tickets:")
display_tickets("open")

# Display only closed tickets
print("\nClosed tickets:")
display_tickets("closed")