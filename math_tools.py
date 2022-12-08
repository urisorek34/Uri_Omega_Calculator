"""
Auther: Uri Sorek
Date:
Description: this module contains the nontrivial math tools for calculating.
"""

from math import pow
from exceptions import FloatFactorialError, NegativeFactorialError


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
