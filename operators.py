"""
Auther: Uri Sorek
Date:

Description: this module contains the operators classes (with calculation and validation check for each operator).
"""
from math import pow


class Operator(object):
    """
    This class is the base class of the different operators in the calculator.
    """

    def __init__(self):
        self.operator = None

    def check_format_operator_validation(self, formula_list):
        """
        This method checks the format of the operator in the formula.
        :param: formula_list: the formula list.
        :return: True if the format is valid, False otherwise.
        """
        operands_is_type_valid = isinstance(formula_list[0], float) and isinstance(formula_list[2], float)
        return len(formula_list) == 3 and operands_is_type_valid and formula_list[1] == self.operator

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (method to override).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        pass


class Plus(Operator):
    """
    This class is the plus operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "+"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 + num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return formula_list[0] + formula_list[2]


class Minus(Operator):
    """
    This class is the minus operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "-"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 - num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return formula_list[0] - formula_list[2]


class Multiply(Operator):
    """
    This class is the multiply operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "*"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 * num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return formula_list[0] * formula_list[2]


class Divide(Operator):
    """
    This class is the divide operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "/"

    def check_format_operator_validation(self, formula_list):
        """
        This method checks the format of the operator in the formula.
        :param: formula_list: the formula list.
        :return: True if the format is valid, False otherwise.
        """
        operands_is_type_valid = isinstance(formula_list[0], float) and isinstance(formula_list[2], float)
        return len(formula_list) == 3 and operands_is_type_valid and formula_list[1] == self.operator and formula_list[
            2] != 0

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 / num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return formula_list[0] / formula_list[2]


class Power(Operator):
    """
    This class is the power operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "^"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 ** num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return pow(formula_list[0], formula_list[2])


class Modulo(Operator):
    """
    This class is the modulo operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "%"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1 % num2).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return formula_list[0] % formula_list[2]


class Max(Operator):
    """
    This class is the max operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "$"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (max(num1, num2)).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return max(formula_list[0], formula_list[2])


class Min(Operator):
    """
    This class is the min operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "&"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (min(num1, num2)).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return min(formula_list[0], formula_list[2])


class Average(Operator):
    """
    This class is the average operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "@"

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (average(num1, num2)).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return (formula_list[0] + formula_list[2]) / 2


class Negative(Operator):
    """
    This class is the negative operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "~"

    def check_format_operator_validation(self, formula_list):
        """
        This method checks the format of the operator in the formula (overrides the method of Operator class).
        :param: formula_list: the formula list.
        :return: True if the format is valid, False otherwise.
        """
        return len(formula_list) == 2 and isinstance(formula_list[1], float)

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (-num1).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        return -formula_list[1]


class Factorial(Operator):
    """
    This class is the factorial operator class.
    """

    def __init__(self):
        super().__init__()
        self.operator = "!"

    def check_format_operator_validation(self, formula_list):
        """
        This method checks the format of the operator in the formula (overrides the method of Operator class).
        :param: formula_list: the formula list.
        :return: True if the format is valid, False otherwise.
        """
        check_if_num_is_natural = float(formula_list[0]) % 1 == 0 and float(formula_list[0]) >= 0
        return len(formula_list) == 2 and isinstance(formula_list[0], float) and check_if_num_is_natural

    def calculate_formula(self, formula_list):
        """
        This method calculates the formula (num1!).
        :param: formula_list: the formula list.
        :return: the result of the calculation.
        """
        factorial_result = 1
        for index in range(1, int(formula_list[0]) + 1):
            factorial_result *= index
        return factorial_result
