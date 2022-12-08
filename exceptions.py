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
        return "Syntax Error!\n"


class MathEquationError(Exception):
    """
    This class represents the math equation error.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Math Error!\n"


class MissingOperatorError(SyntaxEquationError):
    """
    This class represents the missing operator error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " missing operator: " + self.message


class MissingBracketError(SyntaxEquationError):
    """
    This class represents the missing bracket error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " missing bracket: " + self.message


class MissingOperandError(SyntaxEquationError):
    """
    This class represents the missing operand error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " missing operand: " + self.message
