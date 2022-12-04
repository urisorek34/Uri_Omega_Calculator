"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""

from config import PRIORITY_DICT
from equation_validation import check_equation_validation


def convert_priority_dict_to_same_priority_list() -> list:
    """
    convert the priority dictionary to a lists of the same priority.
    :return: the tuples list.
    """
    dict_list_same_priority = {}
    # sort the priority dict
    sorted_priority_dict = dict(sorted(PRIORITY_DICT.keys()))
    for operator, priority in sorted_priority_dict:
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
        return float(number_string)
    except ValueError:
        raise ValueError("missing operator")  # TODO: right exception (missing operator exception)


def pack_formula_to_list_right_unary(operator: str, operand: str) -> list:
    """
    pack right unary formula to list
    :param operator: the operator
    :param operand: the operand
    :return: the packed list.
    """
    pass


def pack_formula_to_list_brackets(operator: str, operand: str) -> list:
    """
    pack brackets to list.
    :param operator: the operator
    :param operand: the operand
    :return: the packed list.
    """
    pass


def pack_formula_to_list_left_unary(operator: str, operand: str) -> list:
    """
    pack left unary formula to list
    :param operator: the operator
    :param operand: the operand
    :return: the packed list.
    """
    pass


def pack_formula_to_list_binary(operand_one: str, operator: str, operand_two: str) -> list:
    """
    pack binary formula to list
    :param operand_one: the first operand
    :param operator: the operator
    :param operand_two: the second operand
    :return:
    """
    pass


def replace_minus_with_unary_minus(equation: str) -> str:
    """
    replace the minus with unary minus.
    :param equation: the equation string.
    :return: the equation string with unary minus.
    """
    first_minus_index = equation.find("-")
    while first_minus_index != -1:
        if first_minus_index == 0:
            # if the first char is a minus, replace it with unary minus
            equation = equation.replace("-", "u-", 1)
        elif equation[first_minus_index - 1] in PRIORITY_DICT.keys():
            # if the minus is after an operator, replace it with unary minus
            equation = equation.replace("-", "u-", 1)
        first_minus_index = equation.find("-", first_minus_index + 1)
    return equation


def reduce_minuses(equation: str) -> str:
    """
    return equation with reduced minuses (unary minus).
    :param equation: the given equation string
    :return: the new string with reduced minuses.
    """


def convert_string_to_formula_list(equation: str) -> list:
    """
    This method converts the equation string to a list of the formula.
    :param: equation: the equation.
    :return: the formula list.
    """
    pass
