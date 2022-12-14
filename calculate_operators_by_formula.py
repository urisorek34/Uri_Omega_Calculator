"""
Auther: Uri Sorek
Date:
Description: this module contains the operators' calculations.
"""

from signs import *
from check_formula_operators import check_operator_validation
from math_tools import *
from config import UNARY_OPERATORS_LIST_LEFT
from exceptions import OverMaxValueError


def calculate_minus_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 - num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return formula_list[0] - formula_list[2]


def calculate_plus_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 + num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return formula_list[0] + formula_list[2]


def calculate_multiply_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 * num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return formula_list[0] * formula_list[2]


def calculate_divide_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 / num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return checked_divide(formula_list[0], formula_list[2])


def calculate_power_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 ^ num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return checked_pow(formula_list[0], formula_list[2])


def calculate_modulo_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 % num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return checked_modulo(formula_list[0], formula_list[2])


def calculate_factorial_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1!) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return factorial(formula_list[0])


def calculate_negative_formula(formula_list: list) -> float:
    """
    This method calculates the formula (-num1) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return -formula_list[1]


def calculate_max_formula(formula_list: list) -> float:
    """
    This method calculates the formula (max(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return max(formula_list[0], formula_list[2])


def calculate_min_formula(formula_list: list) -> float:
    """
    This method calculates the formula (min(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return min(formula_list[0], formula_list[2])


def calculate_average_formula(formula_list: list) -> float:
    """
    This method calculates the formula (average(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return (formula_list[0] + formula_list[2]) / 2


def calculate_add_digits_formula(formula_list: list) -> float:
    """
    This method calculates the formula (add_digits(num1)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return calculate_add_digits_checked(formula_list[0])


def calculate_formula(formula: list) -> float:
    """
    This method calculates the formula according to the operator.
    :param: formula: the formula list.
    :return: the result of the calculation.
    """
    operators_calculations = {PLUS_OPERATOR: calculate_plus_formula, MINUS_OPERATOR: calculate_minus_formula,
                              MULTIPLY_OPERATOR: calculate_multiply_formula, DIVIDE_OPERATOR: calculate_divide_formula,
                              POWER_OPERATOR: calculate_power_formula, MODULO_OPERATOR: calculate_modulo_formula,
                              FACTORIAL_OPERATOR: calculate_factorial_formula,
                              TILDA_OPERATOR: calculate_negative_formula,
                              MAX_OPERATOR: calculate_max_formula, MIN_OPERATOR: calculate_min_formula,
                              AVG_OPERATOR: calculate_average_formula, ADD_DIGIT_OPERATOR: calculate_add_digits_formula,
                              SIGN_MINUS: calculate_negative_formula}
    try:
        if (formula[0] in UNARY_OPERATORS_LIST_LEFT or formula[0] == SIGN_MINUS) and check_operator_validation(
                formula[0],
                formula):
            return operators_calculations[formula[0]](formula)
        elif check_operator_validation(formula[1], formula):
            return operators_calculations[formula[1]](formula)
    except (OverflowError, RecursionError):
        formula = [str(x) for x in formula]
        raise OverMaxValueError(f"The result of {''.join(formula)} is too big!")
