class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(description)

    def list_tasks(self):
        return self.tasks


class ToDoApp:
    def __init__(self):
        self.todo = ToDoList()

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Add task")
            print("2. Show tasks")
            print("3. Exit")

            choice = input("> ")

            if choice == "1":
                self.handle_add()
            elif choice == "2":
                self.handle_list()
            elif choice == "3":
                print("Exiting the realm.")
                break
            else:
                print("Unrecognized command.")

    def handle_add(self):
        description = input("Task description: ")
        self.todo.add_task(description)
        print(f"Added: {description}")

    def handle_list(self):
        tasks = self.todo.list_tasks()
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")


if __name__ == "__main__":
    ToDoApp().run()
