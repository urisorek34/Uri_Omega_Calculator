"""
Auther: Uri Sorek
Date:
Description: this module contains the nontrivial math tools for calculating.
"""

from math import pow
from exceptions import FloatFactorialError, NegativeFactorialError, ComplexNumberError, NegativeAddDigitsError, \
    ZeroDivisionCalculatorError


def factorial(num: float) -> float:
    """
    This method calculates the factorial of a number.
    :param num: the number.
    :return: the factorial of the number.
    """
    if num < 0:
        raise NegativeFactorialError(str(num) + " is negative number.")
    if num % 1 != 0:
        raise FloatFactorialError(str(num) + " is float number.")
    if num == 0:
        return 1
    return num * factorial(num - 1)


def checked_divide(num1: float, num2: float) -> float:
    """
    This method calculates the division of a number checked if he is zero.
    :param num1: the number.
    :param num2: the divisor.
    :return: the result of the division.
    """
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionCalculatorError(f"{num1}/{num2} is zero division.")


def checked_pow(num1: float, num2: float) -> float:
    """
    This method calculates the power of a number checked if he is complex.
    :param num1: the number.
    :param num2: the power.
    :return: the power of the number.
    """
    try:
        return pow(num1, num2)
    except ValueError:
        raise ComplexNumberError(f"{num1}^{num2} is complex number.")


def calculate_add_digits_checked(number: float) -> float:
    """
    This method calculates the formula if the number not negative.
    raise appropriate exception if the formula is not valid.
    :param: formula_list: the formula list.
    :return: the result of the calculation.
    """
    number_string = str(number).replace(".", "")
    if number_string[0] == "-":
        raise NegativeAddDigitsError(f"{number} is negative number.")
    return float(sum([int(digit) for digit in number_string]))
