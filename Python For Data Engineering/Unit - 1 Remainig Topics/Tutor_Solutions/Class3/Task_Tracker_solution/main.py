"""Task Tracker CLI - model solution.

Run with:  python main.py
Test with: python tests.py
"""


def _to_index(tasks, number):
    """Convert a 1-based task number to a list index or raise ValueError."""
    if not isinstance(number, int) or not 1 <= number <= len(tasks):
        raise ValueError("Task number out of range.")
    return number - 1


def add_task(tasks, title):
    """Add a new task and return the updated list."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    tasks.append({"title": title, "done": False})
    return tasks


def show_tasks(tasks):
    """Print every task with its number and status."""
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{number}. [{status}] {task['title']}")


def complete_task(tasks, number):
    """Mark a task as done."""
    tasks[_to_index(tasks, number)]["done"] = True
    return tasks


def remove_task(tasks, number):
    """Remove a task."""
    del tasks[_to_index(tasks, number)]
    return tasks


def ask_number():
    """Return an integer typed by the user, or None if invalid."""
    try:
        return int(input("Task number: "))
    except ValueError:
        print("Please enter a whole number.")
        return None


def main():
    tasks = []
    while True:
        print("\n1) Add  2) Show  3) Complete  4) Remove  5) Quit")
        choice = input("Choose: ")
        try:
            if choice == "1":
                add_task(tasks, input("Task title: "))
            elif choice == "2":
                show_tasks(tasks)
            elif choice in ("3", "4"):
                number = ask_number()
                if number is not None:
                    action = complete_task if choice == "3" else remove_task
                    action(tasks, number)
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Unknown option.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
