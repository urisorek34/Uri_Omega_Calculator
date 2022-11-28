"""
Auther: Uri Sorek
Date:
Description: configuration file for the calculator.
"""

BINARY_OPERATORS_LIST = ["-", "+", "*", "/", "^", "&", "$", "@"]
UNARY_OPERATORS_LIST_LEFT = ["~", "#"]
UNARY_OPERATORS_LIST_RIGHT = ["!"]
PRIORITY_DICT = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "!": 6, "~": 6,"#": 6}
