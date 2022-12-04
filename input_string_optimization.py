"""
Auther: Uri Sorek
Date:

Description: this module contains formula validation check for the input string (what to calculate).
"""

from config import PRIORITY_DICT
from equation_validation import check_equation_validation


def convert_priority_dict_to_same_priority_list() -> list:
    """
    convert the priority dictionary to a lists of the same priority.
    :return: the tuples list.
    """
    dict_list_same_priority = {}
    # sort the priority dict
    sorted_priority_dict = dict(sorted(PRIORITY_DICT.keys()))
    for operator, priority in sorted_priority_dict:
        if priority not in dict_list_same_priority.keys():
            dict_list_same_priority[priority] = [operator]
        else:
            dict_list_same_priority[priority].append(operator)
    # reverse the operators that are sorted by priority
    priority_list_reversed = list(dict_list_same_priority.values())
    priority_list_reversed.reverse()
    return priority_list_reversed


def convert_number_to_float(number_string: str) -> float:
    """
    the function converts a string number to float.
    :param: number_string: the string that suppose to be a number.
    :return: the number converted to float.
    """

    if number_string.count(".") > 1:
        raise ValueError("missing operator")  # TODO: right exception (missing operator exception)
    try:
        number_string = number_string.replace("u", "-")
        return float(number_string)
    except ValueError:
        raise ValueError("missing operator")  # TODO: right exception (missing operator exception)


def pack_formula_to_list_right_unary(operator: str, operand: str) -> list:
    """
    pack right unary formula to list
    :param operator: the operator
    :param operand: the operand
    :return: the packed list.
    """
    pass


def pack_formula_to_list_brackets(equation: str, lst: list) -> list:
    """
    pack brackets to list using recursion.
    :param lst: the list to pack to.
    :param equation: the equation string.
    :return: list of lists with brackets inside.
    """
    # if there are no more brackets
    if equation.count("(") == 0:
        return [equation.replace(")", "")]
    # get the string until the left bracket
    equation_until_left_bracket = equation[:equation.index("(")]
    # get the string from the left bracket
    equation_after_left_bracket = equation[equation.index("(") + 1:]
    # append to the list the string until the left bracket
    lst.append(equation_until_left_bracket)
    # append to the list a call to the function with the string after the left bracket
    lst.append(pack_formula_to_list_brackets(equation_after_left_bracket, []))
    # if the first char is a left bracket
    if lst[0] == "":
        lst.pop(0)
    return lst


def pack_formula_to_list_left_unary(operator: str, operand: str) -> list:
    """
    pack left unary formula to list
    :param operator: the operator
    :param operand: the operand
    :return: the packed list.
    """
    pass


def pack_formula_to_list_binary(operand_one: str, operator: str, operand_two: str) -> list:
    """
    pack binary formula to list
    :param operand_one: the first operand
    :param operator: the operator
    :param operand_two: the second operand
    :return:
    """
    pass


def replace_minus_with_unary_minus(equation: str) -> str:
    """
    replace the minus with unary minus.
    :param equation: the equation string.
    :return: the equation string with unary minus.
    """
    equation_list = list(equation)
    minus_index = equation_list.index("-")
    while minus_index != -1:
        if minus_index == 0:
            # if the first char is a minus, replace it with unary minus
            equation_list[minus_index] = "u"
        elif equation_list[minus_index - 1] in PRIORITY_DICT.keys() or equation_list[minus_index - 1] == "(" or \
                equation_list[minus_index - 1] == "u":
            # if the minus is after an operator, replace it with unary minus
            equation_list[minus_index] = "u"
        minus_index = equation.find("-", minus_index + 1)
    return "".join(equation_list)


def reduce_minuses(equation: str) -> str:
    """
    return equation with reduced unary minuses (unary minus).
    :param equation: the given equation string
    :return: the new string with reduced minuses.
    """
    equation_replaced_unary_minus = replace_minus_with_unary_minus(equation)
    minus_index = equation_replaced_unary_minus.find("u")
    while minus_index != -1:
        count_minuses = 1
        # count the minuses
        while equation_replaced_unary_minus[minus_index + 1] == "u":
            equation_replaced_unary_minus = equation_replaced_unary_minus.replace("u", "", 1)
            count_minuses += 1
        # if the number of minuses is even then the number is positive and the unary minus is redundant
        if count_minuses % 2 == 0:
            equation_replaced_unary_minus = equation_replaced_unary_minus.replace("u", "", 1)
        minus_index = equation_replaced_unary_minus.find("u", minus_index + 1)
    return equation_replaced_unary_minus


def convert_string_to_formula_list(equation: str) -> list:
    """
    This method converts the equation string to a list of the formula.
    :param: equation: the equation.
    :return: the formula list.
    """
    pass
