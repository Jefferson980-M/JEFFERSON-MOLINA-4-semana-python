# Ejercicio 2

list_students = {}
grades_n = []


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
                    if 5 >= mistakes_integers > 0:
                        return mistakes_integers
                    else:
                        print(
                            "Error: Only numbers major to 0 allowed and and less than or equal to five")
            else:
                print("Error: Only integers numbers allowed")
        except ValueError:
            print("Error: Only integer numbers")


def mistakes_numbers_float(numbers: float, default=1) -> float:
    while True:
        try:
            mistakes_numerics = input(numbers).strip()
            mistakes_numerics = float(mistakes_numerics)
            if default == 1:
                if mistakes_numerics > 0:
                    return mistakes_numerics
                else:
                    print("Error: Only numbers major to 0 allowed")
        except ValueError:
            print("Error: Only value numbers")
        except Exception as error:
            print(f" Sorry, an unexpected error ocurred {error}")


def add_student(quantity: int = 0, name_student: str = "", grades: float = 0) -> list:

    quantity: int = mistakes_numbers_int(
        "How many grades do you want to enter?\n")
    name_student: str = mistakes("Enter the name student:\n")
    for i in range(quantity):
        grades: float = mistakes_numbers_float(f"Enter the grades {i+1}:\n")
        grades_n.append(grades)
    list_students["name"] = name_student
    list_students["grades"] = grades_n


def average(average_total: float = 0):

    average_total = sum(grades_n)/len(grades_n)
    print(f"Average: {average_total}")


def main():
    add_student()
    print(list_students)
    average()


main()
