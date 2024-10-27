# Module3Lesson1
Python Programming Challenges
This repository contains solutions to two Python programming challenges designed to demonstrate data handling and functionality in customer service systems and display message formatting.

1. Customer Service Ticket Tracker
Overview
The Customer Service Ticket Tracker is a Python program designed to track customer service tickets. Each ticket contains details such as a unique ID, customer name, issue description, and status (open or closed). This program provides a straightforward way to manage and update customer tickets, allowing you to track and modify ticket statuses as needed.

Features
Open a New Ticket: Allows users to create a new customer service ticket with a unique ID, customer name, issue description, and an initial status of "open."
Update Ticket Status: Allows users to change the status of an existing ticket to either "open" or "closed."
Display Tickets: Displays all tickets or filters by status (open/closed).
Example Ticket Structure
python
Copy code
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
Functions
open_ticket(ticket_id, customer, issue): Opens a new ticket.
update_ticket_status(ticket_id, status): Updates the status of an existing ticket.
display_tickets(status=None): Displays all tickets or filters by status if specified.
Usage
To use the functions, call each function with the relevant parameters:

Use open_ticket to add a new ticket.
Use update_ticket_status to modify the status of an existing ticket.
Use display_tickets to view all tickets or only open/closed tickets by passing the status as a parameter.
2. Like Display Text Generator
Overview
The Like Display Text Generator is a function that generates display text similar to social media “like” counters. Given a list of names of people who like an item, this function returns a grammatically correct string describing who liked the item.

Features
Dynamic Output Based on List Length:
No likes: Displays "no one likes this".
One like: Displays "<name> likes this".
Two likes: Displays "<name1> and <name2> like this".
Three likes: Displays "<name1>, <name2> and <name3> like this".
Four or more likes: Displays "<name1>, <name2> and X others like this" (where X is the remaining count).
Functions
likes(names): Returns the appropriate display text based on the list of names.
Usage
Simply call likes(names) with an array of names as input, and the function will return a properly formatted message.

Installation and Setup
These projects do not require any additional libraries and can be run in any Python environment. Just copy the code files and execute them in a Python interpreter or editor.

License
These projects are provided for educational purposes only.

