import pytest
import erina_solution

def test1():
    number = 88
    assert erina_solution.very_even(number) == False

def test2():
    number = 222
    assert erina_solution.very_even(number) == True

def test3():
    number = 5
    assert erina_solution.very_even(number) == False

def test4():
    number = 841
    assert erina_solution.very_even(number) == True

def test4():
    number = -1
    assert erina_solution.very_even(number) == "Введено недопустимое значение"
