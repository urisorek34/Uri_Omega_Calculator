"""
Auther: Uri Sorek
Date:

Description: this module contains the pytest testing for the "Omega Calculator" program.
"""
import pytest
from user_communication import get_result_with_exception_handling


def test_syntax_error():
    """
    This method tests syntax errors.
    :return: None.
    """
    testing_list = ["3*^2", ")7*3", "3*3(", "3*3)", "3*3+4-5#2"]
    for test in testing_list:
        print(test)
        assert "Syntax Error!\n" in get_result_with_exception_handling(test)


def test_non_sense():
    """
    This method tests nonsense input.
    :return: None.
    """
    assert "Syntax Error!\n" in get_result_with_exception_handling("dfsdfafdsg3241-=-sdfg")


def test_empty_input():
    """
    This method tests empty input.
    :return: None.
    """
    assert "Syntax Error!\n" in get_result_with_exception_handling("")


def test_white_spaces_input():
    """
    This method tests white spaces input.
    :return: None.
    """
    assert "Syntax Error!\n" in get_result_with_exception_handling("  \t\n\r ")


def test_simple_equations():
    """
    This method tests simple equations.
    :return: None.
    """
    testing_dict = {"3+4": 7, "3-4": -1, "3*4": 12, "3/4": 0.75, "3^4": 81, "3%4": 3, "7$8": 8, "7&8": 7,
                    "10!": 3628800, "-8@4": -2, "-123#": -6, "~-5": 5}
    for test, result in testing_dict.items():
        print(test)
        assert get_result_with_exception_handling(test) == f"the result of the equation is: {float(result)}"

