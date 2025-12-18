# Smart Helpdesk

**Description:**  
Smart Helpdesk is a Command-Line Interface (CLI) Helpdesk system developed in Python.  
Users can create accounts, open tickets, and view their tickets.  
Support staff can view all tickets and update their status.  
All data is stored in a local SQLite database.

---

## Features

- User login with role-based access (`user` or `support`)
- Create tickets (for Users)
- View tickets (Users see only their own tickets; Support sees all tickets)
- Update ticket status (for Support)
- Data persistence using SQLite
- Easy-to-use Command Line Interface (CLI)

---

## Installation & Running

1. Clone the repository:

```bash
git clone <your_repository_url>
```

2. Navigate to the project folder:

```bash
cd Smart_helpdesk
```

3. Make sure Python 3 is installed. Run the program:

```bash
python main.py
```

4. Follow the on-screen menu:

- **Create User**: Register a new User or Support account  
- **Login**: Log in with an existing account  
- **Create Ticket**: Users can create a new ticket  
- **View Tickets**: Users see their tickets; Support sees all  
- **Update Ticket Status**: Support users can change the status of any ticket  
- **Exit**: Close the program

---

## Example Usage

### 1. Create User

```python
Enter username: Nada
Enter role (user/support): user
Enter password: 1234
User created successfully.
```

### 2. Login

```python
Username: Nada
Password: 1234
Login successful! Role: user
```

### 3. Create Ticket

```python
Ticket title: PC not working
Ticket description: The computer does not start
Priority (Low / Medium / High): High
Ticket created successfully.
```

### 4. View Tickets

```python
Ticket ID: 1
Title: PC not working
Description: The computer does not start
Priority: High
Status: OPEN
Created by: Nada
```

### 5. Update Ticket Status (Support only)

```python
Ticket ID: 1
Enter new status (Open / In Progress / Closed): In Progress
Ticket status updated successfully.
```

---


## Screenshots

### 1. terminal_create_ticket_1.png.png
![Create User](https://github.com/larabinada752-netizen/Smart_helpdesk/blob/c78fe63c403c89040218b4979cdc8ad9618e58dc/terminal_create_ticket_1.png.png)

### 2. terminal_create_ticket_2.png.png
![Create Ticket](https://github.com/larabinada752-netizen/Smart_helpdesk/blob/c78fe63c403c89040218b4979cdc8ad9618e58dc/terminal_create_ticket_2.png.png)


---

## Notes

- SQLite database (`helpdesk.db`) is generated automatically on the first run  
- `_pycache_` folder is created by Python automatically; no need to include it in GitHub  
- Keep folder names simple (English letters) to avoid path issues  

---

## Tech Stack

- Python 3  
- SQLite  
- Command Line Interface (CLI)

---

## Author

Nada Larabi

