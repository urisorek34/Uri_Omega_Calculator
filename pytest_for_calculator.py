"""
Auther: Uri Sorek
Description: this module contains the pytest testing for the calculator.
"""
from user_communication import get_result_with_exception_handling


def test_syntax_error():
    """
    This method tests syntax errors.
    :return: None.
    """
    print("\nSyntax Error:")
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
    This method tests 15 simple equations.
    :return: None.
    """
    print("\nSimple equations:")
    testing_dict = {"3+4": 7, "3-4": -1, "3*4": 12, "3/4": 0.75, "3^4": 81, "3%4": 3, "7$8": 8, "7&8": 7,
                    "10!": 3628800, "-8@4": -2, "-123#": -6, "~-5": 5, "3%4-6": -3, "3-4&6": -1, "345*2-~6": 696, }
    for test, result in testing_dict.items():
        print(test + " = " + str(result))
        assert get_result_with_exception_handling(test) == f"the result of the equation is: {float(result)}"


def test_advanced_equations():
    """
    This method tests 20 advanced equations (also with unary minuses, brackets, and spaces).
    :return: None.
    """
    print("\nAdvanced equations:")
    testing_dict = {"-~(-3)*(-(( 3!)))*-1": -18, "(5%3)----(2 $3)&(2^ 3)": 5, "7^2+-(-3)!": 55,
                    "6%3*6-(-3@ 6)": -1.5,
                    "132#*(--2)+20+(-3+3)": 32, "~78   - --- -- - -8^2": -142, "(~-3!+ 2)@4-(75.435%5) #": -11,
                    "3^2*3-(----- - 3!@ 10)": 19,
                    "90%(3*   -3)*857565865/553653": 0, "--5845.854&6896.6- -~3*9": 5818.854,
                    " 45@(876%8&7.8) -  (3  *  3  ^  2)": -3.29999999999999,
                    "-- -~(5&-6)$-10*8/6/6/8/6": -0.027777777777777776,
                    "1234567#$1234.10#*2": 56, "(76&3$2@1 ^3)#&(983.53453325^3)": 8, "3!!@--3%(35433565*325)%3": 1.5,
                    "9^0.5*(   10@-30)$~83247532": -30,
                    "3+~5&(90-6)@43.546$4434": 4437, "56%3*2 - ~ ( 3 ^ 2  ) ": 13,
                    "67.5324$78*( 5&2080)----345436.5": 345826.5,
                    "102.000001#@-~  ---- --(3^2)!": 181442}

    for test, result in testing_dict.items():
        print(test + " = " + str(result))
        assert get_result_with_exception_handling(test) == f"the result of the equation is: {float(result)}"
