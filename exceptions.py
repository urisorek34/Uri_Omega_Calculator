"""
Auther: Uri Sorek
Date:

Description: this module contains the exceptions for the calculator.
"""


class SyntaxEquationError(Exception):
    """
    This class represents the syntax equation error.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Syntax Error!"


class MathEquationError(Exception):
    """
    This class represents the math equation error.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Math Error!"
