# Ejercicio 9

list_pets = []


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
                print("Error: Only numbers major to 0 allowed")
        except ValueError:
            print("Error: Only numerics value")
        except Exception as error:
            print(f" Sorry, an unexpected error ocurred  {error}")


def register_pets(name: str = "", quantity_pets: int = 0, age: int = 0) -> list:
    quantity_pets = mistakes_numbers_int(
        "Enter how many pets you want to register:\n")
    for i in range(quantity_pets):
        name = mistakes(f"Enter the name of the pet {i+1}:\n")
        species = mistakes("Enter the species of the pet:\n")
        age = mistakes_numbers_int("Enter the age of the pet (in years):\n")
        pet = {"name": name, "species": species, "age": age}
        list_pets.append(pet)
    return list_pets


def search_species(species: str = ""):
    species = mistakes("Enter the species to search:\n")
    print(f"\nPets of species: {species}")
    for pet in list_pets:
        if pet["species"].lower().replace(" ", "") == species:
            print(f"Name: {pet["name"]} * Age: {pet["age"]}")
            break
    else:
        print("No pets found for this species")


def filter_age(min_age: int = 0):
    min_age = mistakes_numbers_int("Enter the minimum age to filter:\n")
    print(f"\nPets with age >= {min_age} years:")
    found = False
    for pet in list_pets:
        if pet["age"] >= min_age:
            print(
                f"Name: {pet["name"]} * Species: {pet["species"]} * Age: {pet["age"]} years")
            found = True
    if not found:
        print("No pets found with that age or older")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tSelect an option:
            1.Register pets
            2.Search by species
            3.Filter by minimum age
            4.Exit
            """)
            if opc == 1:
                register_pets()
            elif opc == 2:
                search_species()
            elif opc == 3:
                filter_age()
            elif opc == 4:
                break
        except ValueError:
            print("Error: Enter again")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


main()
