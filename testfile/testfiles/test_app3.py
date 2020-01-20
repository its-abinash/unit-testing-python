import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/userfile/')

import app3
import pytest

x = app3.demo_class()

@pytest.mark.parametrize('num, result',
    [
        (0, False),
        (17, True),
        (5, True),
        (12, False),
        (2, True),
        (11, True),
        (1, False),
        (10, False),
        (30, False),
        (31, True),
        (32, False),
        (33, False),
        (34, False),
        (35, False)
    ]
)

def test_isPrime(num, result):
    assert x.isPrime(num) == result