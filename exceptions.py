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


class FactorialError(MathEquationError):
    """
    This class represents the factorial error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " factorial error: "


class NegativeFactorialError(FactorialError):
    """
    This class represents the negative factorial error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " negative factorial is not allowed: " + self.message


class FloatFactorialError(FactorialError):
    """
    This class represents the float factorial error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + " float factorial is not allowed: " + self.message
