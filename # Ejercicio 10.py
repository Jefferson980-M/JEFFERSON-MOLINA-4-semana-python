# Ejercicio 10

list_members = []


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


def register_members(name: str = "", quantity_members: int = 0, plan: str = "", payment_status: str = "") -> list:
    quantity_members = mistakes_numbers_int(
        "Enter how many members you want to register:\n")
    for i in range(quantity_members):
        name = mistakes(f"Enter the name of the member {i+1}:\n")
        plan = mistakes("Enter the membership plan (basic/premium):\n")
        payment_status = mistakes("Is the payment up to date? (yes/no):\n")
        member = {"name": name, "plan": plan, "payment": payment_status}
        list_members.append(member)
    return list_members


def update_plan(name: str = "", new_plan: str = ""):
    name = mistakes("Enter the name of the member to update:\n")
    for member in list_members:
        if member["name"] == name:
            new_plan = mistakes("Enter the new plan (basic/premium):\n")
            member["plan"] = new_plan
            print("Membership plan updated successfully:", member)
            break
    else:
        print("Member not found")


def list_late():
    print("\nMembers with overdue payments:")
    found = False
    for member in list_members:
        if member["payment"] == "no":
            print(f"Name: {member["name"]} * Plan: {member["plan"]}")
            found = True
    if not found:
        print("All members are up to date with payments")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tSelect an option:
            1.Register members
            2.Update membership plan
            3.Members with late payments
            4.Exit
            """)
            if opc == 1:
                register_members()
            elif opc == 2:
                update_plan()
            elif opc == 3:
                list_late()
            elif opc == 4:
                break
        except ValueError:
            print("Error: Enter again")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


main()
