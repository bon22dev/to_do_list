from models import Task
from storage import Storage

class ToDoList:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.storage.save(self.tasks)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.storage.save(self.tasks)
            return removed
        return None

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.storage.save(self.tasks)
            return self.tasks[index]
        return None

    def list_tasks(self):
        return self.tasks