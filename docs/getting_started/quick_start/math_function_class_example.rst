MathFunctionClass Example
=========================

Use the ``MathFunctionClass`` class to do various mathematical operations on the 
entered variables. In general, you will add a detailed description for 
the example. 

All the classes and functions should not be listed in the examples. 
Only the functions that the users will typically use should be listed here. 

Import and use the python_github_tutorial ``MathFunctionClass`` class.  

.. code:: ipython3

    from python_github_tutorial.main_functions.main_functions  import MathFunctionClass 

    # enter the two (2) values to use
    entered_value_0 = 100
    entered_value_1 = 2

    # set the MathFunctionClass
    math_variable = MathFunctionClass(entered_value_0, entered_value_1)

    # print the math_variable (i.e., MathFunctionClass) and list its type
    print(f"\n")
    print(f"math_variable = {math_variable}")
    print(f"type(math_variable) = {type(math_variable)}\n")

    # print the math_variable attribute added_number and list its type
    print(f"math_variable.added_numbers = {math_variable.added_numbers}")
    print(f"type(math_variable.added_numbers) = {type(math_variable.added_numbers)}\n")

    # print the math_variable attribute multiplied_numbers and list its type
    print(
    f"math_variable.multiplied_numbers = "
    f"{math_variable.multiplied_numbers}"
    )
    print(
    f"type(math_variable.multiplied_numbers) = " 
    f"{type(math_variable.multiplied_numbers)}\n"
    )

    # print the math_variable running a function within the class (add_1_to_both_numbers_and_multiply()) and list its type
    print(
    f"math_variable.add_1_to_both_numbers_and_multiply() = "
    f"{math_variable.add_1_to_both_numbers_and_multiply()}"
    )
    print(
    f"type(math_variableadd_1_to_both_numbers_and_multiply()) = "
    f"{type(math_variable.add_1_to_both_numbers_and_multiply())}\n")