from app import ToDoList

class ToDoApp:
    def __init__(self):
        self.todo = ToDoList()

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Add task")
            print("2. Show tasks")
            print("3. Mark task as completed")
            print("4. Delete task")
            print("5. Exit")

            choice = input("> ")

            if choice == "1":
                self.handle_add()
            elif choice == "2":
                self.handle_list()
            elif choice == "3":
                self.handle_complete()
            elif choice == "4":
                self.handle_delete()
            elif choice == "5":
                print("Goodbye, task-slayer.")
                break
            else:
                print("Invalid choice.")

    def handle_add(self):
        desc = input("Task description: ")
        self.todo.add_task(desc)
        print(f"Added: {desc}")

    def handle_list(self):
        tasks = self.todo.list_tasks()
        if not tasks:
            print("No tasks.")
            return

        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "[✔]" if task.completed else "[ ]"
            print(f"{i}. {status} {task.description}")

    def handle_complete(self):
        self.handle_list()
        index = int(input("Number to complete: ")) - 1
        task = self.todo.complete_task(index)
        if task:
            print(f"Completed: {task.description}")
        else:
            print("Invalid index.")

    def handle_delete(self):
        self.handle_list()
        index = int(input("Number to delete: ")) - 1
        removed = self.todo.delete_task(index)
        if removed:
            print(f"Deleted: {removed.description}")
        else:
            print("Invalid index.")


if __name__ == "__main__":
    ToDoApp().run()