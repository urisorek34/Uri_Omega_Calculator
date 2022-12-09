"""
Auther: Uri Sorek
Date:

Description: this module contains the user communication.
"""
from config import PRIORITY_DICT

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


