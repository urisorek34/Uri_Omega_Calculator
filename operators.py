"""
Auther: Uri Sorek
Date:

Description: this module contains the operators classes (with calculation and validation check for each operator).
"""


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


