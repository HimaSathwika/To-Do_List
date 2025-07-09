def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nTo-Do List:")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✓" if completed else "✗"
            print(f"{i}. [{status}] {task}")
        print()

def add_task(tasks):
    task = input("Enter the task name: ")
    tasks.append((task, False))
    print("Task added successfully!\n")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            task = tasks[num - 1][0]
            tasks[num - 1] = (task, True)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed[0]}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = []
    while True:
        print("To-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
