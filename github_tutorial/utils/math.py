"""Standard math function utilities."""

def add_2_numbers(no_0, no_1):
    """Add 2 numbers together.

    This function adds 2 numbers together. 

    Parameters
    ----------
    no_0: int or float
        The first integer or float that will be added. 
    no_1: int or float
        The second integer or float that will be added.
    
    Returns
    -------
    sum_no_0_and_no_1: int or float
        The sum of no_0 and no_1.
    """
    if not isinstance(no_0, (int, float)):
        raise TypeError(
            f"ERROR: In the 'add_2_numbers' function, the {'no_0'} is a {type(no_0)} and not a int or float."
            )
    
    if not isinstance(no_1, (int, float)):
        raise TypeError(
            f"ERROR: In the 'add_2_numbers' function, the {'no_1'} is a {type(no_1)} and not a int or float."
            )
    
    sum_of_no_0_and_no_1 = no_0 + no_1

    return sum_of_no_0_and_no_1

def multiple_of_2_numbers(no_0, no_1):
    """Multiplies 2 numbers together.

    This function multiplies 2 numbers together. 

    Parameters
    ----------
    no_0: int or float
        The first integer or float that will be multiplied. 
    no_1: int or float
        The second integer or float that will be  multiplied.
    
    Returns
    -------
    sum_no_0_and_no_1: int or float
        The sum of no_0 and no_1.
    """
    if not isinstance(no_0, (int, float)):
        raise TypeError(
            f"ERROR: In the 'multiple_of_2_numbers' function, the {'no_0'} is a {type(no_0)} and not a int or float"
            )
    
    if not isinstance(no_1, (int, float)):
        raise TypeError(
            f"ERROR: In the 'multiple_of_2_numbers' function, the {'no_1'} is a {type(no_1)} and not a int or float"
            )
    
    multiple_of_no_0_and_no_1 = no_0 * no_1

    return multiple_of_no_0_and_no_1