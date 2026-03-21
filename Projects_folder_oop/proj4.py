class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{status} {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print("Task added!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print("Task completed!")
        else:
            print("Invalid task number.")


# -------- CLI Interface --------
manager = TaskManager()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter task: ")
        manager.add_task(title)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        manager.show_tasks()
        num = int(input("Enter task number: ")) - 1
        manager.complete_task(num)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")