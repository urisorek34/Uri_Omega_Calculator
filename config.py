"""
Auther: Uri Sorek
Date:
Description: configuration file for the calculator.
"""
from signs import *

BINARY_OPERATORS_LIST = [MINUS_OPERATOR, PLUS_OPERATOR, MULTIPLY_OPERATOR, DIVIDE_OPERATOR, POWER_OPERATOR,
                         MODULO_OPERATOR, MIN_OPERATOR, MAX_OPERATOR, AVG_OPERATOR]
UNARY_OPERATORS_LIST_LEFT = [TILDA_OPERATOR]
UNARY_OPERATORS_LIST_RIGHT = [FACTORIAL_OPERATOR, ADD_DIGIT_OPERATOR]
PRIORITY_DICT = {PLUS_OPERATOR: 1, MINUS_OPERATOR: 1, MULTIPLY_OPERATOR: 2, DIVIDE_OPERATOR: 2, POWER_OPERATOR: 3,
                 MODULO_OPERATOR: 4, MAX_OPERATOR: 5, MIN_OPERATOR: 5, AVG_OPERATOR: 5, FACTORIAL_OPERATOR: 6,
                 TILDA_OPERATOR: 6, ADD_DIGIT_OPERATOR: 6}
