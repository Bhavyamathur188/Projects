import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

tasks = load_tasks()

while True:
    print("\n1. View Tasks  2. Add Task  3. Remove Task  4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid input!")
