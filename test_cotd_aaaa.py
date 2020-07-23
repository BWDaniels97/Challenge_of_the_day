import pytest
import cotd_aaaa

def test_1():
	assert cotd_aaaa.calc(9) == 11106

def test_2():
	assert cotd_aaaa.calc(1) == 1234

def test_3():
	assert cotd_aaaa.calc(6) == 7404

def test_4():
	assert cotd_aaaa.calc(3) == 3702

