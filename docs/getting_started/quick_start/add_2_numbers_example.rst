add_2_numbers Function Example
==============================


Use the ``add_2_numbers`` function to add two (2) entered variables together. 
In general, you will add a detailed description for the example.

All the classes and functions should not be listed in the examples. 
Only the functions that the users will typically use should be listed here. 

Import and use the python_github_tutorial ``add_2_numbers`` function.

.. code:: ipython3

    from python_github_tutorial.utils.math  import add_2_numbers

    # Enter the two (2) input variables numbers.
    no_0 = 1
    no_1 = 5

    # Run the add_2_numbers function on the two (2) input variables numbers
    # and print the output value and it's Python type.
    calculated_value = add_2_numbers(no_0, no_1)
    print(f"calculated_value = {calculated_value}")
    print(f"type(calculated_value) = {type(calculated_value)}\n")