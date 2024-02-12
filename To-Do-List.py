class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):1
        if task not in self.tasks:
            self.tasks[task] = False
            print(f"Task '{task}' added successfully.")
        else:
            print(f"Task '{task}' already exists.")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            print(f"Task '{task}' updated successfully.")
        else:
            print(f"Task '{task}' does not exist.")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted successfully.")
        else:
            print(f"Task '{task}' does not exist.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for task, status in self.tasks.items():
                print(f"[{'X' if status else ' '}] {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to update: ")
            status = input("Enter status (True/False): ").capitalize() == 'True'
            todo_list.update_task(task, status)
        elif choice == '3':
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
