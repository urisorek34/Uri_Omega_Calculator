"""
Auther: Uri Sorek
Date:
Description: this module contains the operators' calculations.
"""

from check_formula_operators import check_operator_validation
from math_tools import factorial, pow
from config import UNARY_OPERATORS_LIST_LEFT


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

    return formula_list[0] / formula_list[2]


def calculate_power_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 ^ num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return pow(formula_list[0], formula_list[2])


def calculate_modulo_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 % num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return formula_list[0] % formula_list[2]


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
    return max(formula_list[1], formula_list[3])


def calculate_min_formula(formula_list: list) -> float:
    """
    This method calculates the formula (min(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return min(formula_list[1], formula_list[3])


def calculate_average_formula(formula_list: list) -> float:
    """
    This method calculates the formula (average(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    return (formula_list[1] + formula_list[3]) / 2


def calculate_add_digits_formula(formula_list: list) -> float:
    """
    This method calculates the formula (add_digits(num1)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    # TODO: specific calculation
    return sum([int(digit) for digit in str(formula_list[1])])


def calculate_formula(formula: list) -> float:
    """
    This method calculates the formula according to the operator.
    :param: formula: the formula list.
    :return: the result of the calculation.
    """
    operators_calculations = {"+": calculate_plus_formula, "-": calculate_minus_formula,
                              "*": calculate_multiply_formula, "/": calculate_divide_formula,
                              "^": calculate_power_formula, "%": calculate_modulo_formula,
                              "!": calculate_factorial_formula, "~": calculate_negative_formula,
                              "$": calculate_max_formula, "&": calculate_min_formula,
                              "@": calculate_average_formula, "#": calculate_add_digits_formula}
    if formula[0] in UNARY_OPERATORS_LIST_LEFT:
        if check_operator_validation(formula[0], formula):
            return operators_calculations[formula[0]](formula)
    elif check_operator_validation(formula[1], formula):
        return operators_calculations[formula[1]](formula)
    else:
        raise Exception("Invalid formula")  # TODO: change to specific exception
