import pytest
from capitalize import capital_case, square


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    assert capital_case('trent') == 'Trent'
    assert capital_case('Hello') == 'hello'


@pytest.mark.parametrize("data, expected", [(5, 25),(2, 4), (9, 81), (-3, 9)])
def test_square_case(data, expected):
    actual = square(data)
    assert actual == expected