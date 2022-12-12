"""
Auther: Uri Sorek
Date:

Description: The main file of the "Omega calculator", this file is the file that gets the input from the user
and calculates it with the calculator object.
"""
from  input_string_optimization import *
from calculator import *
lst = convert_string_from_infix_to_postfix("1+2+(3$4)+5---6+7+8!")
print(lst)
print(calculate_postfix(lst))