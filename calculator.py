"""
Auther: Uri Sorek
Description: this module contains the finale calculation of the equation.
"""
from calculate_operators_by_formula import calculate_formula
from signs import SIGN_MINUS
from config import UNARY_OPERATORS_LIST_LEFT, UNARY_OPERATORS_LIST_RIGHT
from input_string_optimization import convert_string_from_infix_to_postfix
from exceptions import MissingOperandError, MissingOperatorError


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
            if not stack:
                # if the stack is empty, raise appropriate exception.
                raise MissingOperandError(item + " is missing operand.")
            # if the item is an operator.
            if item in UNARY_OPERATORS_LIST_LEFT or item == SIGN_MINUS:
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
    if len(stack) > 1:
        raise MissingOperatorError(f"Missing operator in the equation.")
    if stack[0] == -0.0:
        return -1 * stack.pop()
    return stack.pop()


def calculate(equation: str) -> float:
    """
    This method calculates the equation.
    :param: equation: the equation.
    :return: the result of the calculation.
    """
    postfix_list = convert_string_from_infix_to_postfix(equation)
    try:
        return calculate_postfix(postfix_list)
    except IndexError:
        raise MissingOperandError(f"Missing operand in {equation}.")
