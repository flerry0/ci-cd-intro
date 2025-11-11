import pytest
from app import *


def test_add():
    assert add(2, 3) == 5
