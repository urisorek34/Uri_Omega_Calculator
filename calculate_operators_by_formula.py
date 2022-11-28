"""
Auther: Uri Sorek
Date:
Description: this module contains the operators' calculations.
"""


from check_formula_operators import check_operator_validation
from math import factorial, pow


def calculate_minus_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 - num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '-'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The minus operator is not valid.")  # TODO: add the right error.
    return formula_list[0] - formula_list[2]


def calculte_plus_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 + num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '+'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The plus operator is not valid.")  # TODO: add the right error.
    return formula_list[0] + formula_list[2]


def calculate_multiply_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 * num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '*'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The multiply operator is not valid.")  # TODO: add the right error.
    return formula_list[0] * formula_list[2]


def calculate_divide_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 / num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '/'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The divide operator is not valid.")  # TODO: add the right error.
    return formula_list[0] / formula_list[2]


def calculate_power_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 ^ num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '^'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The power operator is not valid.")  # TODO: add the right error.
    return pow(formula_list[0], formula_list[2])


def calculate_modulo_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1 % num2) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '%'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The modulo operator is not valid.")  # TODO: add the right error.
    return formula_list[0] % formula_list[2]


def calculate_factorial_formula(formula_list: list) -> float:
    """
    This method calculates the formula (num1!) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '!'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The factorial operator is not valid.")  # TODO: add the right error.
    return factorial(formula_list[0])


def calculate_negative_formula(formula_list: list) -> float:
    """
    This method calculates the formula (-num1) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '~'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The negative operator is not valid.")  # TODO: add the right error.
    return -formula_list[1]


def calculate_max_formula(formula_list: list) -> float:
    """
    This method calculates the formula (max(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '$'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The max operator is not valid.")  # TODO: add the right error.
    return max(formula_list[1], formula_list[3])


def calculate_min_formula(formula_list: list) -> float:
    """
    This method calculates the formula (min(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '&'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The min operator is not valid.")  # TODO: add the right error.
    return min(formula_list[1], formula_list[3])


def calculate_average_formula(formula_list: list) -> float:
    """
    This method calculates the formula (average(num1, num2)) if the formula is valid.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    operator = '@'
    if not check_operator_validation(operator, formula_list):
        raise ValueError("The average operator is not valid.")  # TODO: add the right error.
    return (formula_list[1] + formula_list[3]) / 2

