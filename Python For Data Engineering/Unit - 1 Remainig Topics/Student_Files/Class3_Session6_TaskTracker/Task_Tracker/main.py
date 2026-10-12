"""Task Tracker CLI - starter project.

Run with:  python main.py
Test with: python tests.py
"""


def add_task(tasks, title):
    """Add a new task and return the updated list."""
    tasks.append({"title": title, "done": False})
    return tasks


def show_tasks(tasks):
    """Print every task."""
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks):
        print(number, task["title"])


def complete_task(tasks, number):
    # TODO: mark the task as done (task numbers start at 1)
    pass


def remove_task(tasks, number):
    # TODO: remove the task (task numbers start at 1)
    pass


def main():
    tasks = []
    while True:
        print("\n1) Add  2) Show  3) Complete  4) Remove  5) Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(tasks, input("Task title: "))
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks, int(input("Task number: ")))
        elif choice == "4":
            remove_task(tasks, int(input("Task number: ")))
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
