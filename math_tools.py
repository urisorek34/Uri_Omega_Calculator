"""
Auther: Uri Sorek
Date:
Description: this module contains the nontrivial math tools for calculating.
"""

from math import pow


def factorial(num: int) -> int:
    """
    This method calculates the factorial of a number.
    :param num: the number.
    :return: the factorial of the number.
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)