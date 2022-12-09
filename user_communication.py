"""
Auther: Uri Sorek
Date:

Description: this module contains the user communication.
"""
from config import PRIORITY_DICT
from calculator import calculate
from exceptions import SyntaxEquationError, MathEquationError

WELCOME_MESSAGE = "Welcome to the uri's Omega advanced calculator!\n " \
                  "This calculator gets an equation and returns it's result." \
                  "In this calculator unary '-' is in first priority (is part of the number).\n" \
                  "The only brackets allowed are '()'.\n" \
                  "For the menu press 'm' or 'M'.\n" \
                  "For the exit press 'e' or 'E'.\n" \
                  "github link: https://github.com/urisorek34/Uri_Omega_Calculator \n"

EXIT_MESSAGE = "Thank you for using uri's Omega calculator!\n"


def menu_message() -> str:
    """
    the function returns the menu message.
    :return: the menu message.
    """
    message = "The menu:\nthe allowed operators and their priority (the higher priority is calculated first):\n"
    for operator, priority in PRIORITY_DICT.items():
        message += f"{operator} --> {priority}\n"
    return message


def get_input_string() -> str:
    """
    the function gets the input string from the user.
    :return: the input string.
    """
    input_string = ""
    try:
        input_string = input("Please enter the equation you want to calculate (press 'm' for menu and 'e' to exit):\n")
    except EOFError:
        print("EOFError --> assuming the user wants to exit")
        print(EXIT_MESSAGE)
        exit(1)

    return input_string


def get_result_with_exception_handling(input_string: str) -> str:
    """
    the function gets the result of the equation and handles the exceptions.
    :param input_string: the input string.
    :return: the result of the equation.
    """
    try:
        result = calculate(input_string)
        return f"the result of the equation is: {result}"
    except SyntaxEquationError as syntax_error:
        return str(syntax_error)
    except MathEquationError as math_error:
        return str(math_error)
    finally:
        print("You are welcome to try again!\n\n")


def communicate_with_user() -> None:
    """
    the function communicates with the user.
    :return: None.
    """
    print(WELCOME_MESSAGE)
    while True:
        input_string = get_input_string()
        if input_string.lower() == "e":
            print(EXIT_MESSAGE)
            break
        elif input_string.lower() == "m":
            print(menu_message())
        else:
            print(get_result_with_exception_handling(input_string))
