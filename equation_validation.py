"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""


def check_equation_validation(equation: str) -> bool:
    """
    This method checks the validation of the equation given from the user.
    :param: equation: the equation.
    :return: True if the equation is valid, False otherwise.
    """
    pass


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
