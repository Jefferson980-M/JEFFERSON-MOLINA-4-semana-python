# Ejercicio 3

menu_restaurant = [{"name": "sopa", "price": 2000, "quantity": 12}]


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


def add_dishes(name: str = "", price: float = 0, quantity: int = 0) -> list:
    quantity_dishes: int = mistakes_numbers_int(
        "Enter the number of dishes you want to enter:\n")

    for i in range(quantity_dishes):
        name: str = mistakes(f"Enter the name of the dish {i+1}:\n")
        price: float = mistakes_numbers_float(f"Enter the price {i+1}:\n")
        quantity: int = mistakes_numbers_int(f"Enter the quantity {i+1}:\n")
        menu_restaurant.append(
            {"name": name, "price": price, "quantity": quantity})
    return menu_restaurant


def update_dish(name: str = "", update_quantity: int = 0, update_price: float = 0):
    while True:
        choose: str = mistakes_numbers_int(
            "Do you want to update (Enter *1* for quantity and Enter *2* Price or Enter *3* for exit):\n", 1)
        if choose == 1:
            name = mistakes("Enter the name dish:\n")
            update_quantity: int = mistakes_numbers_int(
                "Enter the new quantity:\n", 1)
        elif choose == 2:
            name = mistakes("Enter the name dish:\n")
            update_price: float = mistakes_numbers_float(
                "Enter the new price:\n")
        elif choose == 3:
            break
        else:
            print("Invalid: Choose 1 or 2 or 3")

        for i in menu_restaurant:
            if i["name"] == name:
                if choose == 1:
                    i["quantity"] = update_quantity
                    print("dish update successfully:", i)
                    break
                elif choose == 2:
                    i["price"] = update_price
                    print("dish update succesfully:", i)
                    break
        else:
            print("dish not found")


def total_dishes(suma: int = 0) -> int:
    suma: int = sum(dish["quantity"]
                    for dish in menu_restaurant if "quantity" in dish)
    print(f"Total dishes {suma}")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tENTER THE OPTION
            1.Add dish
            2.Update dish
            3.Total dishes
            4.Exit
            """)
            if opc == 1:
                add_dishes()
            elif opc == 2:
                update_dish()
            elif opc == 3:
                total_dishes()
            elif opc == 4:
                break
        except ValueError:
            print("Error: Enter again")
        except Exception as error:
            print(error)


main()
