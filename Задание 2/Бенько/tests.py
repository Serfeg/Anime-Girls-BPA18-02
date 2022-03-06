import moduleEgor as mE
import pytest


def test_check():
    n = 10
    assert mE.solution(n) == 'X'


def test_none():
    n = 0
    assert mE.solution(n) == '0'


def test_max_length():
    n = 1990
    assert mE.solution(n) == 'MCMXC'


def test_none():
    n = 0
    assert mE.solution(n) == None


def test_zero():
    n = 0
    assert mE.solution(n) == ""


def test_zero_num():
    n = 4000
    assert mE.solution(n) == "MMMM"  # не может быть более 3 одинаковых симовола подряд, а по факту пропускат
