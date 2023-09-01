import numpy as np
import pytest
from python_github_tutorial.tests.base_test import BaseTest
from python_github_tutorial.utils.math import (add_2_numbers, multiple_of_2_numbers)


class TestMath(BaseTest):
    def test_add_2_numbers_ints(self):
        val_0 = 1
        val_1 = 2

        value = add_2_numbers(val_0, val_1)

        assert value == 3
        assert isinstance(value, (int, float))
    
    def test_add_2_numbers_floats(self):
        val_0 = 1.5
        val_1 = 2.0

        value = add_2_numbers(val_0, val_1)

        assert np.isclose(value, 3.5)
        assert isinstance(value, (int, float))

    def test_add_2_numbers_val_0_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'add_2_numbers' function, the no_0 is a {type('no_0')} "
            f"and not a int or float",
        ):
            val_0 = '1.5'
            val_1 = 2.0

            value = add_2_numbers(val_0, val_1)

    def test_add_2_numbers_val_1_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'add_2_numbers' function, the no_1 is a {type('no_1')} "
            f"and not a int or float",
        ):
            val_0 = 1.5
            val_1 = '2.0'

            value = add_2_numbers(val_0, val_1)

    def test_multiple_of_2_numbers_ints(self):
        val_0 = 1
        val_1 = 2

        value = multiple_of_2_numbers(val_0, val_1)

        assert value == 2
        assert isinstance(value, (int, float))
    
    def test_multiple_of_2_numbers_floats(self):
        val_0 = 1.5
        val_1 = 2.0

        value = multiple_of_2_numbers(val_0, val_1)

        assert np.isclose(value, 3.0)
        assert isinstance(value, (int, float))

    def test_multiple_of_2_numbers_val_0_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'multiple_of_2_numbers' function, the no_0 is a {type('no_0')} "
            f"and not a int or float",
        ):
            val_0 = '1.5'
            val_1 = 2.0

            value = multiple_of_2_numbers(val_0, val_1)

    def test_multiple_of_2_numbers_val_1_str(self):
        with pytest.raises(
            TypeError,
            match=f"ERROR: In the 'multiple_of_2_numbers' function, the no_1 is a {type('no_1')} "
            f"and not a int or float",
        ):
            val_0 = 1.5
            val_1 = '2.0'

            value = multiple_of_2_numbers(val_0, val_1)