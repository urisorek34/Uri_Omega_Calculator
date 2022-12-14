"""
Auther: Uri Sorek
Description: this module contains the math calculations that can cause a MathEquationError.
"""

from math import pow
from signs import *
from exceptions import FloatFactorialError, NegativeFactorialError, ComplexNumberError, NegativeAddDigitsError, \
    ZeroDivisionCalculatorError, OverMaxValueError


def factorial(num: float) -> float:
    """
    This method calculates the factorial of a number.
    :param: num: the number.
    :return: the factorial of the number.
    :raise: FloatFactorialError if the number is float.
    :raise: NegativeFactorialError if the number is negative.
    :raise: OverMaxValueError if the result is over max value.
    """
    if num < 0:
        raise NegativeFactorialError(str(num) + " is negative number.")
    if num % 1 != 0:
        raise FloatFactorialError(str(num) + " is float number.")
    if num == 0:
        return 1
    result = num * factorial(num - 1)
    if result == float('inf'):
        raise OverMaxValueError("equation is over max value.")
    return result


def checked_divide(number: float, divisor: float) -> float:
    """
    This method calculates the division of a number checked if he is zero.
    :param: number: the number.
    :param: divisor: the divisor.
    :return: the result of the division.
    :raise: ZeroDivisionCalculatorError if the divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionCalculatorError(f"{number}/{divisor} is zero division.")
    return number / divisor


def checked_pow(base: float, exponent: float) -> float:
    """
    This method calculates the power of a number checked if he is complex.
    :param: base: the base.
    :param: exponent: the exponent of the base.
    :return: the power of the base by the exponent.
    :raise: ComplexNumberError if the result is a complex number.
    :raise: OverMaxValueError if the result is over max value.
    """
    if base < 0 and exponent % 1 != 0:
        raise ComplexNumberError(f"{base}^{exponent} is complex number.")
    result = pow(base, exponent)
    if result == float('inf'):
        raise OverMaxValueError(f"{base}^{exponent} is over max value.")
    return result


def calculate_add_digits_checked(number: float) -> float:
    """
    This method calculates the sum of the digits of the number if it's not negative.
    :param: number: the number.
    :return: the result of the calculation.
    :raise: NegativeAddDigitsError if the number is negative.
    """
    number_string = str(number)
    if number_string[0] == MINUS_OPERATOR:
        raise NegativeAddDigitsError(f"{number} is negative number.")
    return float(sum([int(digit) for digit in number_string if digit.isdigit()]))


def checked_modulo(number: float, divisor: float) -> float:
    """
    This method calculates the modulo of a number checked if he is zero.
    :param: number: the number.
    :param: divisor : the divisor.
    :return: the result of the modulo.
    :raise: ZeroDivisionCalculatorError if the divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionCalculatorError(f"{number}%{divisor} is zero division.")
    return number % divisor
