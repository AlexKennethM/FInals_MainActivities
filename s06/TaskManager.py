class TaskManager:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        self.top = -1

    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def add_task(self, title, description):
        task = {"Title": title, "Description": description, "completed": False}

        if not self.is_full():
            if title not in [t['Title'] for t in self.stack]:
                self.top += 1
                self.stack.append(task)
                return f"{title} added to task"
            else:
                return f"{title} already in stack"
        else:
            return f"Task is full, finish other tasks"

    def mark_completed(self, title):
        for task in self.stack:
            if task["Title"] == title:
                task["completed"] = True
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def display_elements(self):
        if self.is_empty():
            print("Task is empty")
        else:
            print("Task list: ")
            for task in self.stack:
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"- {task['Title']}: {task['Description']} [{status}]")

    def exit(self):
        exit()


def main():
    task_manager = TaskManager(5)

    while True:
        print("========== Task Manager ==========")
        print("Add task[1], Mark as Completed[2], Display Tasks[3], Exit[4]")

        user_input = (input("Choose action 1-4: "))

        if user_input == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            print(task_manager.add_task(title, description))
        elif user_input == "2":
            title = input("Enter task title to mark as completed: ")
            task_manager.mark_completed(title)
        elif user_input == "3":
            task_manager.display_elements()
        elif user_input == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()
