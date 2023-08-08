import numpy as np
import pytest
from github_tutorial.tests.base_test import BaseTest
#from github_tutorial.utils.math import (add_2_numbers, multiple_of_2_numbers)
from github_tutorial.main_functions.main_functions  import (MathFunctionClass,  _add_1_to_value)

class TestMainFunction(BaseTest):
    def test__add_1_to_value_int(self):
        val_0 = 1

        value = _add_1_to_value(val_0)

        assert value == 2
        assert isinstance(value, (int, float))

    def test__add_1_to_value_float(self):
        val_0 = 2.5

        value =  _add_1_to_value(val_0)

        assert np.isclose(value, 3.5)
        assert isinstance(value, (int, float))

    def test__add_1_to_value_val_0_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the '_add_1_to_value' function, the initial_value is a {type('initial_value')} "
            f"and not a int or float",
        ):
            val_0 = '1.5'

            value = _add_1_to_value(val_0)
    
    def test__add_1_to_value_val_0_equal_99_99(self):
        val_0 = 99.999

        value =  _add_1_to_value(val_0)

        assert np.isclose(value, 100.999)
        assert isinstance(value, (int, float))

    def test__add_1_to_value_val_0_equal_negative_99999_99(self):
        val_0 = -99999.99

        value =  _add_1_to_value(val_0)

        assert np.isclose(value, -99998.99)
        assert isinstance(value, (int, float))

    def test__add_1_to_value_val_0_value_greater_equal_100(self):
        with pytest.warns(
            UserWarning,
            match=f"WARNING: In the '_add_1_to_value' function, the {'initial_value'} >= 100 "
            f"\(initial_value = {101}\). Are you sure you want to use a large number?",
        ):
            val_0 = 101

            value = _add_1_to_value(val_0)

    def test__add_1_to_value_val_0_value_greater_equal_100000(self):
        with pytest.warns(
            UserWarning,
            match=f"WARNING: In the '_add_1_to_value' function, the {'initial_value'} >= 100 "
            f"\(initial_value = {100000}\). Are you sure you want to use a large number?",
        ):
            val_0 = 100000

            value = _add_1_to_value(val_0)

    def test_MathFunctionClass(self):
        val_0 = 1
        val_1 = 2

        math_variable = MathFunctionClass(val_0, val_1)

        assert np.isclose(math_variable.added_numbers, 3)
        assert isinstance(math_variable.added_numbers, (int, float))
        assert np.isclose(math_variable.multiplied_numbers, 2)
        assert isinstance(math_variable.multiplied_numbers, (int, float))
        assert np.isclose(math_variable.add_1_to_both_numbers_and_multiply(), 6)
        assert isinstance(math_variable.add_1_to_both_numbers_and_multiply(), (int, float))
    
    def test_MathFunctionClass_val_0_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'MathFunctionClass' class, the value_0 is a {type('value_0')} "
            f"and not a int or float",
        ):
            val_0 = '1.5'
            val_1 = 2.0

            math_variable = MathFunctionClass(val_0, val_1)

    def test_MathFunctionClass_val_1_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'MathFunctionClass' class, the value_1 is a {type('value_1')} "
            f"and not a int or float",
        ):
            val_0 = 1.5
            val_1 = '2.0'

            math_variable = MathFunctionClass(val_0, val_1)