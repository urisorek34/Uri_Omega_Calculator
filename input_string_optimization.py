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


def convert_numbers_to_float(number_string: str) -> float:
    """
    the function converts numbers to float.
    :param: number_string:
    :return:
    """
    pass


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


def reduce_minuses(equation: str) -> str:
    """
    return equation with reduced minuses (unary minus).
    :param equation: the given equation string
    :return: the new string with reduced minuses.
    """
    pass


def convert_string_to_formula_list(equation: str) -> list:
    """
    This method converts the equation string to a list of the formula.
    :param: equation: the equation.
    :return: the formula list.
    """
    pass
