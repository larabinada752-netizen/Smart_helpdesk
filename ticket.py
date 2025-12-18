class Ticket:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "OPEN"

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Status: {self.status}"
        )
