"""
Auther: Uri Sorek
Date:
Description: this module contains the operators' validation check for checking validation before calculating.
"""


def check_defult_format_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the operator in the formula.
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    operands_is_type_valid = isinstance(formula_list[0], float) and isinstance(formula_list[2], float)
    return len(formula_list) == 3 and operands_is_type_valid and formula_list[1] == operator


def check_plus_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the plus operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "+"
    return check_defult_format_operator_validation(operator, formula_list)


def check_minus_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the minus operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "-"
    return check_defult_format_operator_validation(operator, formula_list)


def check_multiply_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the multiply operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "*"
    return check_defult_format_operator_validation(operator, formula_list)


def check_divide_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the divide operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "/"
    return check_defult_format_operator_validation(operator, formula_list) and formula_list[2] != 0


def check_power_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the power operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "^"
    return check_defult_format_operator_validation(operator, formula_list)


def check_modulo_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the modulo operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "%"
    return check_defult_format_operator_validation(operator, formula_list) and formula_list[2] != 0


def check_factorial_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the factorial operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "!"
    return len(formula_list) == 2 and isinstance(formula_list[0], float) and formula_list[1] == operator


def check_max_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the max operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "$"
    return check_defult_format_operator_validation(operator, formula_list)


def check_min_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the min operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "#"
    return check_defult_format_operator_validation(operator, formula_list)


def check_average_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the avarege operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "@"
    return check_defult_format_operator_validation(operator, formula_list)


def check_negative_operator_validation(formula_list: list) -> bool:
    """
    This method checks the format of the negate operator in the formula.
    :param: formula_list: the formula list.
    :return: True if the format is valid, False otherwise.
    """
    operator = "~"
    return len(formula_list) == 2 and isinstance(formula_list[0], float) and formula_list[1] == operator


def check_operator_validation(operator: str, formula_list: list) -> bool:
    """
    This method checks the format of the operator in the formula.
    :param: formula_list: the formula list.
    :param: operator: the operator that is given to the function.
    :return: True if the format is valid, False otherwise.
    """
    operators_validation_dict = {"+": check_plus_operator_validation, "-": check_minus_operator_validation,
                                 "*": check_multiply_operator_validation, "/": check_divide_operator_validation,
                                 "^": check_power_operator_validation, "%": check_modulo_operator_validation,
                                 "!": check_factorial_operator_validation, "~": check_negative_operator_validation,
                                 "$": check_max_operator_validation, "#": check_min_operator_validation,
                                 "@": check_average_operator_validation}
    return operators_validation_dict[operator](formula_list)
