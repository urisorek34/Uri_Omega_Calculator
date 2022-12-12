"""
Auther: Uri Sorek
Date:

Description: this module contains the pytest testing for the "Omega Calculator" program.
"""
import pytest
from user_communication import get_result_with_exception_handling


def test_syntax_error():
    """
    This method tests the main function.
    :return: None.
    """
    testing_list = ["3*^2", ")7*3", "3*3(", "3*3)", "3*3+4-5#2"]
    for test in testing_list:
        print(test)
        assert "Syntax Error!\n" in get_result_with_exception_handling(test)


test_syntax_error()
