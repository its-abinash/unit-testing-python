import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/userfile/')

import app1
import pytest

x = app1.demo_class()

@pytest.mark.parametrize('arr, n, result',
    [
        ([1, 1, 1, 1, 0, 0, 0], 7, 4),
        ([1, 1, 1, 0, 0, 0, 0], 7, 3),
        ([1, 0, 0, 0], 4, 1)
    ]
)

def test_countOnes(arr, n, result):
    assert x.countOnes(arr, n) == result