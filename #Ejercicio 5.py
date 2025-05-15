# Ejercicio 5
list_movies = []


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
            if 5 >= mistakes_numerics > 0:
                return mistakes_numerics
            else:
                print(
                    "Error: Only numbers less than or equal to 5 and greater than 0")
        except ValueError:
            print("Error: Only numerics value")
        except Exception as error:
            print(f" Sorry, an unexpected error ocurred  {error}")


def add_movies(name: str = "", quantity_movies: int = 0) -> list:
    quantity_movies: int = mistakes_numbers_int(
        "Enter the number of movies you want to enter:\n")
    for i in range(quantity_movies):
        name: str = mistakes(f"Enter the name of the movie {i+1}:\n")
        qualifications_n = []

        for j in range(5):
            qualifications: float = mistakes_numbers_float(
                f"Enter five qualifications {j+1}:\n")
            qualifications_n.append(qualifications)
        movie = {"name": name, "qualifications": qualifications_n}
        list_movies.append(movie)
    return list_movies


def average(qualifications: float = 0) -> float:
    for movie in list_movies:
        qualifications = movie["qualifications"]
        average1 = sum(qualifications)/len(qualifications)
        print("MOVIES\n")
        print(f"movie: {movie["name"]} average: {average1}")


def main():
    add_movies()
    average()


main()
