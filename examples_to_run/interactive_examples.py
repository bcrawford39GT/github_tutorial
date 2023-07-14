
# to make each cell add '# %%' to the above section 
# %%
from github_tutorial.main_functions.main_functions  import math_function_class 

# %%
# enter the two (2) values to use
entered_value_0 = 100
entered_value_1 = 2

# %%
# set the math_function_class
math_variable = math_function_class(entered_value_0, entered_value_1)

# %%
# print the math_variable (i.e., math_function_class) and list its type
print(f"\n")
print(f"math_variable = {math_variable}")
print(f"type(math_variable) = {type(math_variable)}\n")

# %%
# print the math_variable attribute added_number and list its type
print(f"math_variable.added_numbers = {math_variable.added_numbers}")
print(f"type(math_variable.added_numbers) = {type(math_variable.added_numbers)}\n")

# %%
# print the math_variable attribute multiplied_numbers and list its type
print(
    f"math_variable.multiplied_numbers = "
    f"{math_variable.multiplied_numbers}"
    )
print(
    f"type(math_variable.multiplied_numbers) = " 
    f"{type(math_variable.multiplied_numbers)}\n"
    )

# %%
# print the math_variable running a function within the class (add_1_to_both_numbers_and_multiply()) and list its type
print(
    f"math_variable.add_1_to_both_numbers_and_multiply() = "
    f"{math_variable.add_1_to_both_numbers_and_multiply()}"
    )
print(
    f"type(math_variableadd_1_to_both_numbers_and_multiply()) = "
    f"{type(math_variable.add_1_to_both_numbers_and_multiply())}\n")
# %%
