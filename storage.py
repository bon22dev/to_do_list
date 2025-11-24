import json
import os
from models import Task

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save(self, tasks):
        data = [task.to_dict() for task in tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]