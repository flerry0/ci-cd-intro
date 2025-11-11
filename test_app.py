import pytest
from app import add, subtract, multiply, divide


def test_add():
    assert add(5, 5) == 10    # Sollte richtig sein
