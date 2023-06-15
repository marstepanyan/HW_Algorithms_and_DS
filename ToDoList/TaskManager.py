from Task import Task
import datetime


class TaskManager:
    def __init__(self):
        self.tasks = []

    def valid_index(self, idx):
        if idx not in range(1, len(self.tasks) + 1):
            print("Invalid task index.")
            return

    def add_task(self):
        task_description = input("Enter task name: ")
        deadline = input("Enter deadline (YYYY-MM-DD HH:MM): ")
        task = Task(task_description, datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M"))
        self.tasks.append(task)
        print("Task added successfully.")
        print()

    def edit_task(self):
        task_index = int(input("Enter task number to modify: "))
        self.valid_index(task_index)
        task = self.tasks[task_index - 1]
        new_description = input("Enter new task name: ")
        task.set_description(new_description)
        print("Task modified successfully.")
        print()

    def delete_task(self):
        task_index = int(input("Enter task number to delete: "))
        self.valid_index(task_index)
        del self.tasks[task_index - 1]
        print("Task deleted successfully.")
        print()

    def mark_as_completed(self):
        task_index = int(input("Enter task number to mark as completed: "))
        self.valid_index(task_index)
        task = self.tasks[task_index - 1]
        task.set_status(True)
        print("Task marked as completed.")
        print()

    def show_tasks(self):
        print("Tasks:")
        completed_count = 0
        current_time = datetime.datetime.now()
        for i, task in enumerate(self.tasks, 1):
            status = "[Completed]" if task.get_status() else "[Not Completed]"
            deadline = task.get_deadline()
            if task.get_status():
                completed_count += 1
                print(f"{i}. {task.get_description()} {status}")
            elif deadline - current_time < datetime.timedelta(hours=1):
                print(f"{i}. {task.get_description()} {status} (Deadline approaching within 1 hour)")
            elif deadline - current_time < datetime.timedelta(days=1):
                print(f"{i}. {task.get_description()} {status} (Deadline approaching within 1 day)")
            else:
                print(f"{i}. {task.get_description()} {status}")
        print()
        print(f"Completed tasks: {completed_count}")
        print(f"Uncompleted tasks: {len(self.tasks) - completed_count}")
        print()

    def task_manager(self):
        while True:
            print("1. Add task")
            print("2. Edit task")
            print("3. Delete task")
            print("4. Mark task as completed")
            print("5. Show tasks")
            print("6. Exit")
            print()

            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.edit_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_as_completed()
            elif choice == "5":
                self.show_tasks()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
