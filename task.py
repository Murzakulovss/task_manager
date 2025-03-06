from datetime import datetime
class Task:
    id_counter = 1
    def __init__(self, title, description, created_at,  is_completed = False):
        self.id = Task.id_counter
        Task.id_counter+=1
        self.title = title
        self.description = description
        self.created_at = created_at
        self.is_completed = is_completed

    def mark_as_done(self):
        self.is_completed = True
        print(f"Task {self.title} marked as done")

