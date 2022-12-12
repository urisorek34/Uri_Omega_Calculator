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