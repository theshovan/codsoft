"""Create a To-Do-List using python
Add some features-
1.Add task,
2.View task,
3.Update task,
4.Delete task,
5.Mark task as done,
6.Exit.
"""


import json

# File to store tasks
task_file = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task."""
    task = input("Enter task description: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "[✓]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def update_task():
    """Update an existing task."""
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter new description: ")
            tasks[task_num]["task"] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    """Delete a task."""
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_done():
    """Mark a task as completed."""
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the To-Do List application."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
