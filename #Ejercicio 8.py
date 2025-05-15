# Ejercicio 8

list_expenses = []


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


def register_expenses(category: str = "", expense: float = 0) -> list:
    quantity_expenses = mistakes_numbers_int(
        "Enter the number of expenses to register:\n")
    for i in range(quantity_expenses):
        category = mistakes(f"Enter the expense category {i+1}:\n")
        amount = mistakes_numbers_float(
            f"Enter the amount of the expense {i+1}:\n")
        expense = {"category": category, "amount": amount}
        list_expenses.append(expense)
    return list_expenses


def total_expenses():
    total = sum(expense["amount"] for expense in list_expenses)
    print(f"\nTotal expenses: ${total:.2f}")


def percentage_category():
    if not list_expenses:
        print("No expenses registered.")
        return

    total = sum(expense["amount"] for expense in list_expenses)
    category_totals = {}

    for expense in list_expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(
            category, 0) + expense["amount"]

    print("\nPercentage of expenses by category:")
    for category, amount in category_totals.items():
        percentage = (amount / total) * 100
        print(f"{category}: {percentage}% (${amount})")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tEnter the option
            1.Register expenses
            2.Total expenses
            3.Percentage by category
            4.Exit
            """)
            if opc == 1:
                register_expenses()
            elif opc == 2:
                total_expenses()
            elif opc == 3:
                percentage_category()
            elif opc == 4:
                break
        except ValueError:
            print("Error: enter again")
        except Exception as error:
            print(error)


main()
