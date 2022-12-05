"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""

from config import PRIORITY_DICT, BRACKETS_LIST
from equation_validation import check_equation_validation


def convert_priority_dict_to_same_priority_list() -> list:
    """
    convert the priority dictionary to a lists of the same priority.
    :return: the tuples list.
    """
    dict_list_same_priority = {}
    # sort the priority dict
    for operator, priority in PRIORITY_DICT.items():
        if priority not in dict_list_same_priority.keys():
            dict_list_same_priority[priority] = [operator]
        else:
            dict_list_same_priority[priority].append(operator)
    # reverse the operators that are sorted by priority
    priority_list_reversed = list(dict_list_same_priority.values())
    priority_list_reversed.reverse()
    return priority_list_reversed


def convert_number_to_float(number_string: str) -> float:
    """
    the function converts a string number to float.
    :param: number_string: the string that suppose to be a number.
    :return: the number converted to float.
    """

    if number_string.count(".") > 1:
        raise ValueError("missing operator")  # TODO: right exception (missing operator exception)
    try:
        number_string = number_string.replace("u", "-")
        return float(number_string)
    except ValueError:
        raise ValueError("missing operator")  # TODO: right exception (missing operator exception)


def replace_minus_with_unary_minus(equation: str) -> str:
    """
    replace the minus with unary minus.
    :param equation: the equation string.
    :return: the equation string with unary minus.
    """
    equation_list = list(equation)
    if "-" in equation_list:
        minus_index = equation_list.index("-")
        while minus_index != -1:
            if minus_index == 0:
                # if the first char is a minus, replace it with unary minus
                equation_list[minus_index] = "u"
            elif equation_list[minus_index - 1] in PRIORITY_DICT.keys() or equation_list[minus_index - 1] == "(" or \
                    equation_list[minus_index - 1] == "u":
                # if the minus is after an operator, replace it with unary minus
                equation_list[minus_index] = "u"
            minus_index = equation.find("-", minus_index + 1)
    return "".join(equation_list)


def reduce_minuses(equation: str) -> str:
    """
    return equation with reduced unary minuses (unary minus).
    :param equation: the given equation string
    :return: the new string with reduced minuses.
    """
    equation_replaced_unary_minus = replace_minus_with_unary_minus(equation)
    minus_index = equation_replaced_unary_minus.find("u")
    while minus_index != -1:
        count_minuses = 1
        # count the minuses
        while equation_replaced_unary_minus[minus_index + 1] == "u":
            equation_replaced_unary_minus = equation_replaced_unary_minus.replace("u", "", 1)
            count_minuses += 1
        # if the number of minuses is even then the number is positive and the unary minus is redundant
        if count_minuses % 2 == 0:
            equation_replaced_unary_minus = equation_replaced_unary_minus.replace("u", "", 1)
        minus_index = equation_replaced_unary_minus.find("u", minus_index + 1)
    return equation_replaced_unary_minus


def convert_equation_to_numbers_and_operators(equation: str) -> list:
    """
    This method converts the equation list to a list of numbers and operators.
    :param: equation: the equation list.
    :return: the formula list in postfix format.
    """
    equation = reduce_minuses(equation)
    equation_lst = []
    index = 0
    while index != len(equation):
        number = ""
        if equation[index] in PRIORITY_DICT.keys() or equation[index] == "(" or equation[index] == ")":
            equation_lst.append(equation[index])
            index += 1
        else:
            while index != len(equation) and equation[index] not in PRIORITY_DICT.keys() and equation[index] != "(" and \
                    equation[index] != ")":
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
        elif element == "(":
            stack.append(element)
        elif element == ")":
            while stack[-1] != "(":
                # pop the stack until the first "("
                postfix_equation.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and PRIORITY_DICT[element] <= PRIORITY_DICT[stack[-1]]:
                # pop the stack until the first "(" or until the operator in the stack has lower priority
                postfix_equation.append(stack.pop())
            stack.append(element)
    while stack:
        # pop the stack until it is empty and add the operators to the postfix equation
        postfix_equation.append(stack.pop())
    return postfix_equation
