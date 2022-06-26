from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
import pytest
from typing import Callable



@pytest.mark.parametrize("fib_func", [fibonacci_cached, fibonacci_lru_cached])
@pytest.mark.parametrize("n, expected", [(0,0),(1,1),(2,1),(3,2),(4,3),(5,5),(6,8),(20,6765)])
def test_naive(fib_func: Callable[[int], int], n: int, expected: int) -> None:
    assert fibonacci_naive(n) == expected
    