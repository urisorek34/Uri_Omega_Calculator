"""
Auther: Uri Sorek
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
        return super().__str__() + "missing operator: " + self.message


class MissingBracketError(SyntaxEquationError):
    """
    This class represents the missing bracket error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "missing bracket: " + self.message


class MissingOperandError(SyntaxEquationError):
    """
    This class represents the missing operand error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "missing operand: " + self.message


class FactorialError(MathEquationError):
    """
    This class represents the factorial error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "factorial error: "


class NegativeFactorialError(FactorialError):
    """
    This class represents the negative factorial error.
    inherits from FactorialError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "negative factorial is not allowed: " + self.message


class FloatFactorialError(FactorialError):
    """
    This class represents the float factorial error.
    inherits from FactorialError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "float factorial is not allowed: " + self.message


class ZeroDivisionCalculatorError(MathEquationError):
    """
    This class represents the zero division error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "zero division error: " + self.message


class InvalidOperatorError(SyntaxEquationError):
    """
    This class represents the invalid operator error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "invalid operator: " + self.message


class TildaError(SyntaxEquationError):
    """
    This class represents the tilda error.
    inherits from SyntaxEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "tilda ('~') error (a number has to come after a tilda): " + self.message


class ComplexNumberError(MathEquationError):
    """
    This class represents the complex number error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "calculator doesn't support complex numbers: " + self.message


class NegativeAddDigitsError(MathEquationError):
    """
    This class represents the negative add digits error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "negative add digits is not allowed: " + self.message


class OverMaxValueError(MathEquationError):
    """
    This class represents the over max value error.
    inherits from MathEquationError.
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__() + "over calculator max value error: " + self.message
