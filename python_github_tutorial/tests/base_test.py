"""test functions for python_github_tutorial"""
import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()

    @pytest.fixture
    def get_10_plus_5(self):
       get_10_plus_5 = 10 + 5 