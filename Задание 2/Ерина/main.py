import math
import pytest
import codewars

def test1():
   words = 'abba'
   anagr = ['aabb', 'abcd', 'bbaa', 'dada']
   assert codewars.anagrams(words, anagr) == ['aabb', 'bbaa']

def test2():
   words = 'racer'
   anagr = ['crazer', 'carer', 'racar', 'caers', 'racer']
   assert codewars.anagrams(words, anagr) == ['carer', 'racer']

def test3():
   words = 'laser'
   anagr = ['lazing', 'lazy',  'lacer']
   assert codewars.anagrams(words, anagr) == []

def test4():
   words = '1234'
   anagr = ['1324', '1673',  '1423']
   assert codewars.anagrams(words, anagr) == ['1324', '1423']

def test5():
   words = 'IRA'
   anagr = ['ARI', 'AIRA', 'IAR']
   assert codewars.anagrams(words, anagr) == ['ARI', 'IAR']

def test6():
   words = ''
   anagr = []
   assert codewars.anagrams(words, anagr) == []

def test7(): #не прошел
   words = 'iRA'
   anagr = ['ARI', 'AIRA', 'IAR']
   assert codewars.anagrams(words, anagr) == ['ARI', 'IAR']

def test8():
   words = ''
   anagr = ['ARI', 'AIRA', 'IAR']
   assert codewars.anagrams(words, anagr) == []

def test9():
   words = 'IRA'
   anagr = []
   assert codewars.anagrams(words, anagr) == []





