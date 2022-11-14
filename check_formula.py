"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""
from operators import Plus, Minus, Multiply, Divide, Power, Modulo, Factorial, Negative, Max, Min, Average


class CheckFormula(object):
    """
    This class is the class that checks the formula given from the input string from the user.
    """
    PRIORITY_DICT = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "#": 5, "!": 6, "~": 6}
    OPERATORS_DICT = {"+": Plus(), "-": Minus(), "*": Multiply(), "/": Divide(), "^": Power(), "%": Modulo(),
                      "$": Max(), "&": Min(), "@": Average(), "!": Factorial(), "~": Negative()}

    def __init__(self, formula_from_user):
        self.formula_from_user = formula_from_user

    def get_operators_dict(self):
        """
        This method returns the operators dictionary.
        :return: OPERATORS_DICT.
        """
        return self.OPERATORS_DICT

    def get_rid_of_minuses(self):
        """
        This method gets rid of the unnecessary minuses (before a number) and convert it to the positive/negative number.
        :return: the formula without minuses.
        """
        return
        # TODO: get rid of the unnecessary minuses (before a number) and convert it to the positive/negative number.

    def get_rid_of_spaces(self):
        """
        This method gets rid of the spaces (between operators and numbers) in the formula.
        :return: the formula without spaces.
        """
        # TODO: get rid of the spaces (between operators and numbers) in the formula.

    def convert_input_to_right_format(self):
        """
        This method converts the input string to the right format (for the calculator).
        :return: the formula in the right format.
        """
        return
        # TODO: convert the input string to the right format (for the calculator).
