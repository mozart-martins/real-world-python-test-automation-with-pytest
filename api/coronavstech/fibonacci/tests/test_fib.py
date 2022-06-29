from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
import pytest
from typing import Callable
from fixtures import time_tracker
from django.urls import reverse

fibonacci_url = reverse('fib-seq')


@pytest.mark.parametrize("fib_func", [fibonacci_cached, fibonacci_lru_cached, fibonacci_naive])
@pytest.mark.parametrize("n, expected", [(0,0),(1,1),(2,1),(3,2),(4,3),(5,5),(6,8),(20,6765)])
def test_naive(time_tracker, fib_func: Callable[[int], int], n: int, expected: int) -> None:
    assert fib_func(n) == expected
    
# eh apenas uma marca... nao eh necessari
@pytest.mark.api
def test_no_n_parameter_should_return_response(client) -> None:
    response = client.get(fibonacci_url)
    assert response.status_code == 200
    assert response.json() == "Hello there, no number was passed"

# eh apenas uma marca... nao eh necessari
@pytest.mark.api
def test_post_method_with_fib_endpoint_should_fail(client) -> None:
    response = client.post(fibonacci_url, data={"n": 4})
    assert response.status_code == 405
    assert response.json()["detail"] == 'Method "POST" not allowed.'

# eh apenas uma marca... nao eh necessari
@pytest.mark.api
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_stress_fibonacci_endpoint(client, n: int, expected: int) -> None:
    response = client.get(
        fibonacci_url,
        data={"n": n}
    )
    assert response.status_code == 200
    assert response.json()["result"] == expected