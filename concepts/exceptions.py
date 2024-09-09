# ValueError:

def convert_to_int(string_value):
    return int(string_value)

# This will raise a ValueError because "abc" is not a valid number
try:
    convert_to_int("abc")
except ValueError as e:
    print(f"A ValueError occurred: {e}")
    

# IndexError:

def access_element_at_index(my_list, index):
    return my_list[index]

# This will raise an IndexError because the list only has 3 elements
my_list = [10, 20, 30]

try:
    access_element_at_index(my_list, 5)
except IndexError as e:
    print(f"An IndexError occurred: {e}")
    

#NameError:
  
def print_variable():
    print(undeclared_variable)  # This variable is not defined

try:
    print_variable()
except NameError as e:
    print(f"A NameError occurred: {e}")

#TypeError:

def concatenate_strings(a, b):
    return a + b

try:
    concatenate_strings("Hello", 123)  # Trying to concatenate a string and an integer
except TypeError as e:
    print(f"A TypeError occurred: {e}")


# ModuleNotFoundError

def import_module():
    import non_existent_module  # This module doesn't exist

try:
    import_module()
except ModuleNotFoundError as e:
    print(f"A ModuleNotFoundError occurred: {e}")
    
# ZeroDivisionError

def divide_numbers(a, b):
    return a / b

try:
    divide_numbers(10, 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"A ZeroDivisionError occurred: {e}")
    
    
# OverflowError:

import math

def calculate_large_exp(value):
    return math.exp(value)

try:
    calculate_large_exp(1000)  # This will raise an OverflowError due to an extremely large result
except OverflowError as e:
    print(f"An OverflowError occurred: {e}")


# KeyError:

def access_dictionary_value(my_dict, key):
    return my_dict[key]

my_dict = {"name": "Jiliar", "age": 30}

try:
    access_dictionary_value(my_dict, "address")  # This key doesn't exist in the dictionary
except KeyError as e:
    print(f"A KeyError occurred: {e}")



