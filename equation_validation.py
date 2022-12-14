"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""
from signs import OPENER_BRACKET, CLOSER_BRACKET
from exceptions import MissingBracketError


def check_equation_validation(equation: str) -> bool:
    """
    This method checks the validation of the equation given from the user.
    :param: equation: the equation.
    :return: True if the equation is valid, False otherwise.
    """
    if not check_brackets_validation(equation):
        raise MissingBracketError(equation)
    return True


def check_brackets_validation(equation: str) -> bool:
    """
    This method checks the validation of the brackets in the equation.
    :param: equation: the equation.
    :return: True if the brackets are valid, False otherwise.
    """
    brackets_stck = []
    # for each bracket in the equation
    for char in equation:
        # if the char is an opener, add it to the stack
        if char == OPENER_BRACKET:
            brackets_stck.append(OPENER_BRACKET)
        elif char == CLOSER_BRACKET:
            # if the char is a closer, check if the stack is empty
            if len(brackets_stck) == 0:
                return False
            else:
                brackets_stck.pop()

    return len(brackets_stck) == 0
