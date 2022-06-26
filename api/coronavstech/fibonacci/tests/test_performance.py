from fibonacci.naive import fibonacci_naive
import pytest


#pytest -m performance
@pytest.mark.performance
def test_performance():
    fibonacci_naive(10)