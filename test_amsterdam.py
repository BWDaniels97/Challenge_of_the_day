import pytest
import amsterdam

def test_1():
	assert amsterdam.am("I am from amsterdam") == 1

def test_2():
	assert amsterdam.am("I am amsterdam am ") == 2

def test_3():
	assert amsterdam.am("I from amsterdam") == 0