# Ejercicio 1
library = [{"name": "sombra", "author": "julio", "pages": 500}]


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


def add_book(title: str = "", author: str = "", pages: int = 0) -> list:
    title: str = mistakes("Enter the name book:\n")
    author: str = mistakes("Enter the author:\n")
    pages: int = mistakes_numbers_int("Enter the pages:\n")

    library.append({"name": title, "author": author, "pages": pages})
    return library


def find_book(search: str = "") -> str:
    search: str = mistakes("Enter the name book to search:\n")
    for i in library:
        if i["name"] == search:
            print("Book found", i)
            break
    else:
        print("Book not found")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
                \tENTER THE OPTION
                1.Add book
                2.Find book
                3.Books available
                4.Exit

                """)
            if opc == 1:
                add_book()
            elif opc == 2:
                find_book()
            elif opc == 3:
                print("Books available")
                for book in library:
                    print(
                        f"\nName: {book["name"]}\nAuthor: {book["author"]}\nPages: {book["pages"]}")
            elif opc == 4:
                break

        except ValueError:
            print("Error: enter again")
        except Exception as error:
            print(error)


main()
