import json #for save list, update later
from task import Task
from datetime import datetime

class TaskManager:

    def __init__(self):
        self.tasks = []

    def _get_task_id_from_user(self):
        try:
            task_id = int(input("Enter the ID of the task: "))
            return task_id
        except ValueError:
            print("Invalid input")
            return None

    def _get_task_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def _get_task_input(self):
        title = input("Enter a title of task: ")
        description = input("Enter a description: ")
        if not title or not description:
            print("Add the full info")
            return None,None
        return title,description

    def get_tasks_list(self):
        if not self.tasks:
            print("no tasks available")
        else:
            for task in self.tasks:
                print(
                    f"| ID: {task.id:2} | Title: {task.title: <10} | Description: {task.description: <30} | Created at: {task.created_at: <40} | Completed: {task.is_completed} |")
                print("------------------------------------------------------------------------------------------------------")

    def add_task(self):
        title,description = self._get_task_input()
        created_at = datetime.now()
        new_task = Task(title,description, created_at)
        self.tasks.append(new_task)
        print(f"Task '{new_task.title}' added successfully at {new_task.created_at}")

    def delete_task(self):
        try:
            task_id = self._get_task_id_from_user()
            task = self._get_task_id(task_id)
            if task:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} removed")
            else:
                print("Task not found")
        except ValueError:
            print("Invalid input")

    def update_task(self):
        task_id = self._get_task_id_from_user()
        task = self._get_task_id(task_id)
        if task:
            title, description = self._get_task_input()
            task.title = title
            task.description = description
            print(f"Task updated: {task.id} - {task.title} - {task.description}")
        else:
            print("Task not found")

    def mark_task_as_done(self):
        try:
            task_id = self._get_task_id_from_user()
            for task in self.tasks:
                if task.id == task_id:
                    task.mark_as_done()
                    print(f"Task with ID {task_id} marked as done")
                    return
            print("Task not found")
        except ValueError:
            print("Invalid input")



