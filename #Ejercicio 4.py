# Ejercicio 4

list_boxes = [{"name": "little box", "price": 2000, "quantity": 12}]


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


def add_boxes(name: str = "", price: float = 0, quantity: int = 0) -> list:
    quantity_boxes: int = mistakes_numbers_int(
        "Enter the number of boxes you want to enter:\n")

    for i in range(quantity_boxes):
        name: str = mistakes(f"Enter the name of the box {i+1}:\n")
        price: float = mistakes_numbers_float(f"Enter the price {i+1}:\n")
        quantity: int = mistakes_numbers_int(f"Enter the quantity {i+1}:\n")
        list_boxes.append(
            {"name": name, "price": price, "quantity": quantity})
    return list_boxes


def update_boxes(name: str = "", update_quantity: int = 0, update_price: float = 0):
    while True:
        choose: str = mistakes_numbers_int(
            "Do you want to update (Enter *1* for quantity and Enter *2* Price or Enter *3* for exit):\n", 1)
        if choose == 1:
            name = mistakes("Enter the name box:\n")
            update_quantity: int = mistakes_numbers_int(
                "Enter the new quantity:\n", 1)
        elif choose == 2:
            name = mistakes("Enter the name box:\n")
            update_price: float = mistakes_numbers_float(
                "Enter the new price:\n")
        elif choose == 3:
            break
        else:
            print("Invalid: Choose 1 or 2 or 3")

        for i in list_boxes:
            if i["name"] == name:
                if choose == 1:
                    i["quantity"] = update_quantity
                    print("Product update successfully:", i)
                    break
                elif choose == 2:
                    i["price"] = update_price
                    print("Product update succesfully:", i)
                    break
        else:
            print("Box not found")


def stock():
    name_box: str = mistakes("Enter the name box:\n")
    requested: str = mistakes_numbers_int("Enter box quantity resquested:\n")
    for boxes in list_boxes:
        if boxes["name"] == name_box:
            if boxes["quantity"] >= requested:
                print("Quantity in stock")
                break
            else:
                print("there is not enough quantity")
                break
    else:
        print("Box not found")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
                    \tENTER THE OPTION
                    1.Add boox
                    2.update box
                    3.Box in stock
                    4.Exit

                    """)
            if opc == 1:
                add_boxes()
            elif opc == 2:
                update_boxes()
            elif opc == 3:
                stock()
            elif opc == 4:
                break

        except ValueError:
            print("Error: enter again")
        except Exception as error:
            print(error)


main()
