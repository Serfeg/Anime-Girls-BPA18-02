import pytest
import math
import Решение

def test(): #Работает
   n = 4
   arr = [10, 11, 12, 13]
   assert Решение.solve(arr, n) == 4.6

def test1(): #Работает
   n = 2
   arr = [1, 1]
   assert Решение.solve(arr, n) == 0.1

def test2(): #Работает
   n = 1
   arr = [10]
   assert Решение.solve(arr, n) == 0

def test3(): #Ошибка
   n = 0
   arr = []
   assert Решение.solve(arr, n) == 0

def test4(): #Ошибка
   n = 10
   arr = [12,23]
   assert Решение.solve(arr, n) == 1.75

def test5(): #Ошибка
   n = 10
   arr = [12,23]
   assert Решение.solve(arr, n) == 0
