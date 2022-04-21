import pytest
import codewars

def test():
   test_info = '493193' #4+9+3+1+9+3=29 2+9=11 1+1=2  
   assert codewars.digital_root(test_info) == 2, 'Тест не пройден'

def test2():
   test_info = '493193' #4+9+3+1+9+3=29 2+9=11 1+1=2  
   assert codewars.digital_root(test_info) == 3, 'Тест не пройден'
   
