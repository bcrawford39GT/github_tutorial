"""Standard math function utilities."""
from typing import Union, List
from numbers import Real

def add_2_numbers(no_0: Union[int,float], no_1: Union[int, float]) -> Union[int, float]:
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
    
    sum_of_no_0_and_no_1 = no_0 + no_1

    return sum_of_no_0_and_no_1

def multiple_of_2_numbers(no_0: Union[int,float], no_1: Union[int,float]) -> Union[int,float]:
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
    multiple_of_no_0_and_no_1 = no_0 * no_1

    return multiple_of_no_0_and_no_1