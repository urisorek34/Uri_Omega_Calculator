"""
Auther: Uri Sorek
Date:
Description: this module contains the operators' validation check for checking validation before calculating.
"""

import config


def format_binary_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the binary operator in form of a formula (operand operator operand).
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    operands_is_type_valid = isinstance(formula_list[0], float) and isinstance(formula_list[2], float)
    return len(formula_list) == 3 and operands_is_type_valid and formula_list[1] == operator


def format_left_unary_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the left unary operator in form of a formula (operator operand).
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    return len(formula_list) == 2 and isinstance(formula_list[0], float) and formula_list[1] == operator


def format_right_unary_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the right unary operator in form of a formula (operand operator).
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    return len(formula_list) == 2 and isinstance(formula_list[1], float) and formula_list[0] == operator


def check_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the operator in the formula.
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    if operator in config.BINARY_OPERATORS_LIST:
        return format_binary_operator_validation(operator, formula_list)
    elif operator in config.UNARY_OPERATORS_LIST_LEFT:
        return format_left_unary_operator_validation(operator, formula_list)
    elif operator in config.UNARY_OPERATORS_LIST_RIGHT:
        return format_right_unary_operator_validation(operator, formula_list)
    # raise NoSuchOperatorError() # TODO
