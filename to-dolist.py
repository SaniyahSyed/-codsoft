class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.title} - {task.description} - {task.status}")

    def update_task_status(self, task_index, new_status):
        self.tasks[task_index - 1].status = new_status

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to update status: "))
            new_status = input("Enter the new status (e.g., Complete/Incomplete): ")
            todo_list.update_task_status(task_index, new_status)
            print("Task status updated successfully!")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
