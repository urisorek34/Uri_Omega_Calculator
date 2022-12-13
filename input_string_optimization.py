"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""

from config import PRIORITY_DICT, OPENER_BRACKET, CLOSER_BRACKET, SIGN_MINUS, UNARY_OPERATORS_LIST_RIGHT
from equation_validation import check_equation_validation
from exceptions import MissingOperatorError, TildaError, InvalidOperatorError


def convert_number_to_float(number_string: str) -> float:
    """
    the function converts a string number to float.
    :param: number_string: the string that suppose to be a number.
    :return: the number converted to float.
    """

    if number_string.count(".") > 1:
        raise MissingOperatorError(number_string)
    try:
        return float(number_string)
    except ValueError:
        raise InvalidOperatorError(number_string)


def replace_minus_with_unary_minus(equation: str) -> str:
    """
    replace the minus with unary minus.
    :param equation: the equation string.
    :return: the equation string with unary minus.
    """
    equation_list = list(equation)
    if SIGN_MINUS in equation_list:
        raise InvalidOperatorError(SIGN_MINUS)
    if "-" in equation_list:
        minus_index = equation_list.index("-")
        while minus_index != -1:
            if minus_index == 0:
                # if the first char is a minus, replace it with unary minus
                equation_list[minus_index] = SIGN_MINUS
            elif equation_list[minus_index - 1] in PRIORITY_DICT.keys() or equation_list[
                minus_index - 1] == OPENER_BRACKET or \
                    equation_list[minus_index - 1] == SIGN_MINUS:
                # if the minus is after an operator, replace it with unary minus
                equation_list[minus_index] = SIGN_MINUS
            minus_index = equation.find("-", minus_index + 1)
    return "".join(equation_list)


def reduce_minuses(equation: str) -> str:
    """
    return equation with reduced minuses which near a number and replace it with "+" operator or one "-" operator.
    :param equation: the given equation string
    :return: the new string with reduced minuses.
    """
    equation_list = list(equation)
    if "-" in equation_list:
        minus_index = equation_list.index("-")
        while minus_index != -1:
            if minus_index != 0 and (equation[minus_index - 1] == CLOSER_BRACKET or equation_list[
                minus_index - 1] in UNARY_OPERATORS_LIST_RIGHT or equation_list[minus_index - 1] == "." or
                                     equation_list[minus_index - 1].isdigit()):
                equation = covert_number_of_minuses_to_operator(equation, minus_index)
                equation_list = list(equation)
            minus_index = equation.find("-", minus_index + 1)
    return equation


def covert_number_of_minuses_to_operator(equation: str, starting_index: int) -> str:
    """
    function that convert number of minuses to operator "+" or "-".
    :param equation: the equation string.
    :param starting_index: the starting index of the minuses.
    :return: the new equation string with the minuses converted to operator.
    """
    counter = -1
    index = starting_index
    while index < len(equation) and equation[index] == "-":
        counter += 1
        index += 1
    if counter == 0:
        return equation
    elif counter % 2 == 1:
        equation = equation[:starting_index] + "-" + equation[index - 1:]
    else:
        equation = equation[:starting_index] + "+" + equation[index - 1:]
    return equation


def remove_spaces(equation: str) -> str:
    """
    This method removes the spaces from the equation.
    :param equation: the equation.
    :return: the equation without spaces.
    """
    return equation.replace(" ", "")


def check_tilda_validation(equation: str) -> None:
    """
    This method checks the validation of the tilda in the equation (~ has to be in the left to a number).
    :param: equation: the equation.
    :return: True if the tilda is valid, False otherwise.
    :raise: TildaError if the tilda is not valid.
    """
    equation_without_unary_minus = equation.replace(SIGN_MINUS, "")
    for index, element in enumerate(equation_without_unary_minus):
        if element == "~" and equation_without_unary_minus[index + 1] in PRIORITY_DICT.keys():
            raise TildaError(equation)


def check_unary_minus_priority(operator: str) -> bool:
    """
    This method checks if the operator is in higher or equal in priority than unary minus. "#" operator has higher priority an "~" has the same priority.
    :param operator: the operator.
    :return: positive if higher priority, 0 if the same priority, negative if lower priority.
    """
    if operator == "#":
        return True
    return False


def priority_check(operator1: str, operator2: str) -> bool:
    """
    This method checks if the priority of the first operator is higher than the second operator.
    :param operator1: the first operator.
    :param operator2: the second operator.
    :return: True if the first operator has higher priority, False otherwise.
    """
    if operator1 == SIGN_MINUS:
        return check_unary_minus_priority(operator2)
    elif operator2 == SIGN_MINUS:
        if "~" == operator1:
            return False
        return not check_unary_minus_priority(operator1)
    else:
        return PRIORITY_DICT[operator1] <= PRIORITY_DICT[operator2]


def convert_equation_to_numbers_and_operators(equation: str) -> list:
    """
    This method converts the equation list to a list of numbers and operators.
    :param: equation: the equation list.
    :return: the formula list in postfix format.
    """
    check_equation_validation(equation)
    equation = remove_spaces(equation)
    equation = reduce_minuses(equation)
    equation = replace_minus_with_unary_minus(equation)
    check_tilda_validation(equation)
    equation_lst = []
    index = 0
    while index != len(equation):
        number = ""
        if equation[index] in PRIORITY_DICT.keys() or equation[index] == OPENER_BRACKET or equation[
            index] == CLOSER_BRACKET or equation[index] == SIGN_MINUS:
            equation_lst.append(equation[index])
            index += 1
        else:
            while index != len(equation) and equation[index] not in PRIORITY_DICT.keys() and equation[
                index] != OPENER_BRACKET and \
                    equation[index] != CLOSER_BRACKET:
                number += equation[index]
                index += 1
            equation_lst.append(convert_number_to_float(number))
    return equation_lst


def convert_string_from_infix_to_postfix(equation: str) -> list:
    """
    This method converts the equation string from infix to a postfix of the formula.
    :param: equation: the equation list.
    :return: the formula list in postfix format.
    """
    postfix_equation = []
    stack = []
    converted_equation = convert_equation_to_numbers_and_operators(equation)
    for element in converted_equation:
        # if the element is a number, add it to the postfix equation
        if isinstance(element, float):
            postfix_equation.append(element)
        elif element == OPENER_BRACKET:
            stack.append(element)
        elif element == CLOSER_BRACKET:
            while stack[-1] != OPENER_BRACKET:
                # pop the stack until the first "("
                postfix_equation.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != OPENER_BRACKET and priority_check(element, stack[-1]):
                # pop the stack until the first "(" or until the operator in the stack has lower priority
                postfix_equation.append(stack.pop())
            stack.append(element)
    while stack:
        # pop the stack until it is empty and add the operators to the postfix equation
        postfix_equation.append(stack.pop())
    return postfix_equation
