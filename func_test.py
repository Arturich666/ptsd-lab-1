from functions import plus, minus, multiply, divide
import pytest


def test_plus():
    result = plus(3, 2)
    assert result == 5


def test_minus():
    result = minus(3, 2)
    assert result == 1


def test_multiply():
    result = multiply(3, 2)
    assert result == 6


def test_divide1():
    result = divide(9, 2)
    assert result == 4.5


def test_divide2():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


def test_divide3():
    result = divide(12, 2)
    assert result == 6
