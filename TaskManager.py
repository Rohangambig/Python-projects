#  Task manager app
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return

        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Not Done"
            print(f"{idx}. {task.description} - {status}")

    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = True
            print("Task marked as done.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            index = int(input("Enter task index to mark as done: "))
            task_manager.mark_done(index)
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            task_manager.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
