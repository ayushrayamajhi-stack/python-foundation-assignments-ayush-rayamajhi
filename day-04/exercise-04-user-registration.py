"""
Exercise: Custom Exception for User Registration
Student: Ayush Rayamajhi
Day: 4
"""


class InvalidAgeError(Exception):
    pass


def register_user(name, age):
    if age < 0 or age > 120:
        raise InvalidAgeError(
            f"Age {age} is not valid for user '{name}'"
        )

    return {
        "name": name,
        "age": age
    }


def try_register(name, age):
    try:
        result = register_user(name, age)

    except InvalidAgeError as error:
        print(f"Registration failed: {error}")

    except ValueError as error:
        print(f"Invalid input: {error}")

    else:
        print(f"Registered: {result}")


# Tests
try_register("Asha", 21)
try_register("Bibek", -5)
try_register("Chandra", 200)