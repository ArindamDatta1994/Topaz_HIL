def add_task():
    task = input("Enter your task: ")
    with open("to_do_list.txt", "a") as file:
        file.write(task + "\n")

    print("Task added successfully!")

def view_task():
    try:
        with open("to_do_list.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No task in the to-do list.")
                return
            
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task.strip()}")

            print()

    except FileNotFoundError:
        print("No to-do list found. Please add a task first.")

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()