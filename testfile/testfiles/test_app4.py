import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/userfile/')

import app4
import pytest

x = app4.demo_class()

@pytest.mark.parametrize('num1, num2, result',
    [
        (10, 15, 5),
        (35, 10, 5),
        (31, 2, 1),
        (10, 4, 2),
        (5, 5, 5)
    ]
)

def test_GCD(num1, num2, result):
    assert x.GCD(num1, num2) == result