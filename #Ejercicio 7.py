# Ejercicio 7

list_tasks = []


def mistakes(strings: str = "") -> str:
    while True:
        try:
            mistakes_strings = input(strings).lower().replace(" ", "")
            if mistakes_strings.isalpha():
                return mistakes_strings
            else:
                print("Error: Only alphabetic characters allowed")
        except TypeError:
            print("Error")


def mistakes_numbers_int(numbers: int = 0, default: int = 1):
    while True:
        try:
            mistakes_integers = input(numbers)
            if mistakes_integers.isdigit():
                mistakes_integers = int(mistakes_integers)
                if default == 1:
                    if mistakes_integers > 0:
                        return mistakes_integers
                    else:
                        print("Error: Only numbers major to 0 allowed")
            else:
                print("Error: Only integers numbers allowed")
        except ValueError:
            print("Error: Only integer numbers")


def mistakes_numbers_float(numbers: float) -> float:
    while True:
        try:
            mistakes_numerics = input(numbers).strip()
            mistakes_numerics = float(mistakes_numerics)
            if mistakes_numerics > 0:
                return mistakes_numerics
            else:
                print("Error: Only numbers greater than 0")
        except ValueError:
            print("Error: Only numerics value")
        except Exception as error:
            print(f" Sorry, an unexpected error ocurred  {error}")


def add_tasks(descriotion: str = "", priority: str = "") -> list:
    quantity_tasks = mistakes_numbers_int(
        "Enter the number of tasks you want to add:\n")
    for i in range(quantity_tasks):
        description = mistakes(f"Enter the task description {i+1}:\n")
        print("Priority options:high, medium, low")
        priority = mistakes(f"Enter the task priority {i+1}:\n")
        task = {"description": description,
                "priority": priority, "state": "pending"}
        list_tasks.append(task)
    return list_tasks


def completed_task():
    description = mistakes("Enter the description of the task to complete:\n")
    for task in list_tasks:
        if task["description"] == description:
            task["state"] = "completed"
            print("Task completed.")
            break
    else:
        print("Task not found.")


def filter_priority():
    priority = mistakes("Enter the priority to filter (high, medium, low):\n")
    print(f"\nTasks with priority '{priority}':")
    for task in list_tasks:
        if task["priority"] == priority:
            print(
                f"Description: {task["description"]} * State: {task["state"]}")


def filter_state():
    state = mistakes("Enter the state to filter (pending, completed):\n")
    print(f"\nTasks with state '{state}':")
    for task in list_tasks:
        if task["state"] == state:
            print(
                f"Description: {task["description"]} - Priority: {task["priority"]}")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tEnter the option
            1.Add tasks
            2.Task completed
            3.Filter by priority
            4.Filter by status
            5.Exit
            """)
            if opc == 1:
                add_tasks()
            elif opc == 2:
                completed_task()
            elif opc == 3:
                filter_priority()
            elif opc == 4:
                filter_state()
            elif opc == 5:
                break
        except ValueError:
            print("Error: enter again")
        except Exception as error:
            print(error)


main()
