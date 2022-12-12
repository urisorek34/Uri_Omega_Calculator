"""
Auther: Uri Sorek
Date:
Description: this module contains the nontrivial math tools for calculating.
"""

from math import pow
from exceptions import FloatFactorialError, NegativeFactorialError,ComplexNumberError


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


def checked_pow(num1: float, num2: float) -> float:
    """
    This method calculates the power of a number.
    :param num1: the number.
    :param num2: the power.
    :return: the power of the number.
    """
    try:
        return pow(num1, num2)
    except ValueError:
        raise ComplexNumberError(f"{num1}^{num2} is complex number.")
