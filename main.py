from user import User
from ticket import Ticket

users = []
tickets = []

def show_menu():
    print("\n=== SMART HELPDESK SYSTEM ===")
    print("1. Create User")
    print("2. Create Ticket")
    print("3. View Tickets")
    print("4. Exit")

def create_user():
    username = input("Enter username: ")
    role = input("Enter role (user / support): ")
    user = User(username, role)
    users.append(user)
    print("User created successfully.")

def create_ticket():
    title = input("Ticket title: ")
    description = input("Ticket description: ")
    priority = input("Priority (Low / Medium / High): ")
    ticket = Ticket(title, description, priority)
    tickets.append(ticket)
    print("Ticket created successfully.")

def view_tickets():
    if not tickets:
        print("No tickets found.")
        return

    for i, ticket in enumerate(tickets, start=1):
        print(f"\nTicket #{i}")
        print(ticket)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            create_ticket()
        elif choice == "3":
            view_tickets()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
