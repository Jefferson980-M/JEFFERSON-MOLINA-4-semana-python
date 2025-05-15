# Ejercicio 6

list_courses = []


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
                print(
                    "Error: Only numbers less than or equal to 5 and greater than 0")
        except ValueError:
            print("Error: Only numerics value")
        except Exception as error:
            print(f" Sorry, an unexpected error ocurred  {error}")


def register_courses(title: str = "", quantity_courses: int = 0) -> list:
    quantity_courses = mistakes_numbers_int(
        "Enter the number of courses you want to register:\n")
    for i in range(quantity_courses):
        title = mistakes(f"Enter the title of course {i+1}:\n")
        duration = mistakes_numbers_float("Enter the duration (in hours):\n")
        enrolled = mistakes_numbers_int(
            "Enter the number of enrolled students:\n")
        course = {"title": title, "duration": duration, "enrolled": enrolled}
        list_courses.append(course)
    return list_courses


def update_courses(title: str = "", update_enrolled: int = 0, update_duration: float = 0):
    while True:
        choose: str = mistakes_numbers_int(
            "Do you want to update (Enter *1* for enrolled students and Enter *2* duration or Enter *3* for exit):\n", 1)
        if choose == 1:
            title = mistakes("Enter the name course:\n")
            update_enrolled: int = mistakes_numbers_int(
                "Enter the new enrolled students:\n", 1)
        elif choose == 2:
            title = mistakes("Enter the name course:\n")
            update_duration: float = mistakes_numbers_float(
                "Enter the new duration:\n")
        elif choose == 3:
            break
        else:
            print("Invalid: Choose 1 or 2 or 3")

        for i in list_courses:
            if i["title"] == title:
                if choose == 1:
                    i["enrolled"] = update_enrolled
                    print("Course update successfully:", i)
                    break
                elif choose == 2:
                    i["duration"] = update_duration
                    print("Course update succesfully:", i)
                    break
        else:
            print("Course not found")


def filter_duration(min_duration: int = 0):
    min_duration = mistakes_numbers_float(
        "Enter the minimum duration in hours:\n")
    print(f"\nCourses with duration >= {min_duration} hours:")
    for course in list_courses:
        if course["duration"] >= min_duration:
            print(
                f"Course: {course['title']} * Duration: {course['duration']}h * Enrolled: {course['enrolled']}")


def main():
    while True:
        try:
            opc = mistakes_numbers_int("""
            \tEnter the option
            1.Register course
            2.Update courses 
            3.Filter duration  
            4.Exit                       
            """)
            if opc == 1:
                register_courses()
            elif opc == 2:
                update_courses()
            elif opc == 3:
                filter_duration()
            elif opc == 4:
                break
        except ValueError:
            print("Error: enter again")
        except Exception as error:
            print(error)


main()
