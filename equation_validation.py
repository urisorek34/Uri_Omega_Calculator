"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""
from config import OPENER_BRACKET, CLOSER_BRACKET


def check_equation_validation(equation: str) -> bool:
    """
    This method checks the validation of the equation given from the user.
    :param: equation: the equation.
    :return: True if the equation is valid, False otherwise.
    """
    # TODO: exceptions for missing operators and brackets
    if check_spaces_between_numbers(equation) or not check_brackets_validation(equation):
        return False
    return True


def check_spaces_between_numbers(equation: str) -> bool:
    """
    This method checks the spaces between the numbers in the equation.
    :param: equation: the equation.
    :return: True if there are spaces and False if not.
    """
    current_string_start = 1
    space_index = 0
    while space_index != -1:
        # check for each space if it between two numbers
        space_index = equation.find(" ", current_string_start)
        if equation[space_index - 1].isdigit() and equation[space_index + 1].isdigit():
            return True
        current_string_start = space_index + 1
    return False


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
