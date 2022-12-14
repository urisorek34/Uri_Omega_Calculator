"""
Auther: Uri Sorek
Description: this module contains the user communication.
"""
from calculator import calculate
from exceptions import SyntaxEquationError, MathEquationError
from signs import *

WELCOME_MESSAGE = "Welcome to the Uri's Omega advanced calculator!\n\n" \
                  "this calculator has few extra rules:\n" \
                  "- This calculator gets an equation and returns it's result." \
                  "- In this calculator unary '-' is in first priority (is part of the number).\n" \
                  "- The only brackets allowed are '()'.\n" \
                  "- For the menu press 'm' or 'M'.\n" \
                  "- For the exit press 'e' or 'E'.\n\n" \
                  "github link: https://github.com/urisorek34/Uri_Omega_Calculator \n"

EXIT_MESSAGE = "Thank you for using uri's Omega calculator!\n"

OPERATOR_EXPLANATION_DICT = {
    PLUS_OPERATOR: "plus operator:\n- Priority 1\n- Binary operator\n- operator add two numbers (first_number + "
                   "second_number)",
    MINUS_OPERATOR: "minus operator:\n- Priority 1\n- Binary operator\n- operator sub two numbers (first_number - "
                    "second_number)",
    MULTIPLY_OPERATOR: "multiply operator\n- Priority 2\n- Binary operator\n- operator multiply two numbers ("
                       "first_number * second_number)",
    DIVIDE_OPERATOR: "divide operator:\n- Priority 2\n- Binary operator\n- operator divide two numbers (first_number / "
                     "second_number)\n- raise MathEquationError --> ZeroDivisionCalculatorError",
    POWER_OPERATOR: "power operator:\n- Priority 3\n-Binary operator\n- operator power two numbers (first_number ^ "
                    "second_number)\n- raise MathEquationError --> ComplexNumberError",
    MODULO_OPERATOR: "modulo operator:\n- Priority 4\n-Binary operator\n- operator do modulo on two numbers ("
                     "first_number % second_number)\n- raise MathEquationError --> ZeroDivisionCalculatorError",
    MAX_OPERATOR: "max operator:\n- Priority 5\n- Binary operator\n- operator return max value between two numbers ("
                  "first_number $ second_number)",
    MIN_OPERATOR: "min operator:\n- Priority 5\n- Binary operator\n- operator return min value between two numbers ("
                  "first_number & second_number)",
    AVG_OPERATOR: "average operator:\n- Priority 5\n- Binary operator\n- operator return average of two numbers ("
                  "first_number @ second_number)",
    FACTORIAL_OPERATOR: "factorial operator:\n- Priority 6\n- Right unary operator\n- operator return the factorial "
                        "of a number ( number!)\n- raise MathEquationError --> FactorialError --> FloatFactorialError,"
                        "NegativeFactorialError",
    TILDA_OPERATOR: "tilda operator:\n- Priority 6\n- Left unary operator\n- operator changes the sign of a number ("
                    "~number = -number)\n- raise SyntaxEquationError --> TildaError",
    ADD_DIGIT_OPERATOR: "add digits operator:\n- Priority 6\n- Right unary operator\n- operator return the sum of the "
                        "digits of a number (123# = 1+2+3 = 6)\n- raise MathEquationError --> NegativeAddDigitsError"}


def menu_message() -> str:
    """
    the function returns the menu message.
    :return: the menu message.
    """
    message = "The menu:\nthe allowed operators and their priority (the higher priority is calculated first):\n"
    for operator, explanation in OPERATOR_EXPLANATION_DICT.items():
        message += "-" * 60 + f"\n{operator} --> {explanation}\n\n"
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
        print("\nEOFError --> assuming the user wants to exit")
        print(EXIT_MESSAGE)
        exit(1)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt --> assuming the user wants to exit")
        print(EXIT_MESSAGE)
        exit(1)
    except OSError:
        print("\nOSError --> assuming the user wants to exit")
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


def communicate_with_user() -> None:
    """
    the function communicates with the user.
    :return: None.
    """
    print(WELCOME_MESSAGE)
    print(menu_message())
    while True:
        input_string = get_input_string()
        if input_string.lower() == "e":
            print(EXIT_MESSAGE)
            break
        elif input_string.lower() == "m":
            print(menu_message())
        else:
            if not input_string:
                print("The input you entered is not valid, please try again.\n\n")
            else:
                print(get_result_with_exception_handling(input_string))
                print("You are welcome to enter another equation!\n")
