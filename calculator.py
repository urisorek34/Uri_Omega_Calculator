"""
Auther: Uri Sorek
Date:

Description: this module contains the calculator class.
"""
from calculate_operators_by_formula import calculate_formula
from config import UNARY_OPERATORS_LIST_LEFT,UNARY_OPERATORS_LIST_RIGHT
from check_formula_operators import check_operator_validation


def calculate_postfix(postfix_list: list) -> float:
    """
    This method calculates the postfix list.
    :param: postfix_list: the postfix list.
    :return: the result of the calculation.
    """
    stack = []
    for item in postfix_list:
        if type(item) is float:
            # if the item is a number, push it to the stack.
            stack.append(item)
        else:
            # if the item is an operator.
            if item in UNARY_OPERATORS_LIST_LEFT:
                # if the operator is unary operator from the left.
                num = stack.pop()
                stack.append(calculate_formula([item, num]))
            elif item in UNARY_OPERATORS_LIST_RIGHT:
                # if the operator is unary operator from the right.
                num = stack.pop()
                stack.append(calculate_formula([num, item]))
            else:
                # if the item is a binary operator.
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calculate_formula([num1, item, num2]))
    return stack.pop()
