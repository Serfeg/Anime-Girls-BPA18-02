import pytest
import moduleOgnegin as mO


#Положительный тест
def testHttpGithub():
    n = "http://github.com/carbonfive/raygun"
    assert mO.domain_name(n) == "github"


#Положительный тест
def testWwwGithub():
    n = "www.github.com/carbonfive/raygun"
    assert mO.domain_name(n) == "github"


#Положительный тест
def testCodeWars():
    n = "https://www.codewars.com/kata/514a024011ea4fb54200004b"
    assert mO.domain_name(n) == "codewars"


#Отрицательный тест
def testEmpty():
    n = ''
    assert mO.domain_name(n) == ''


#Отрицательный тест
def testNone():
    n = None
    assert mO.domain_name(n) == None


#Положительный тест
def testVk():
    n = "vk.com"
    assert mO.domain_name(n) == "vk"