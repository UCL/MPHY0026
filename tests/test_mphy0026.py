# coding=utf-8

"""MPHY0026 tests"""

from mphy0026.ui.mphy0026_demo import run_demo
from mphy0026.algorithms import addition, multiplication
import six

# Pytest style

def test_using_pytest_mphy0026():
    x = 1
    y = 2
    verbose = False
    multiply = False

    expected_answer = 3
    assert run_demo(x, y, multiply, verbose) == expected_answer

def test_addition():

    assert addition.add_two_numbers(1, 2) == 3

def test_multiplication():

    assert multiplication.multiply_two_numbers(2, 2) == 4

