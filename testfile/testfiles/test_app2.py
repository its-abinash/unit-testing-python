import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/userfile/')

import app2
import pytest

x = app2.demo_class()

@pytest.mark.parametrize('str1, result',
    [
        ("abcba", True),
        ("aba", True),
        ("abcd", False),
        ("a", True),
        ("", True)
    ]
)

def test_isPalindrome(str1, result):
    assert x.isPalindrome(str1) == result