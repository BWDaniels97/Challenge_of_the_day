import pytest
import cotd_alphabetize

def test_1():
	assert cotd_alphabetize.alpha('alpha alpha charlie alpha delta bravo') == 'alpha bravo charlie delta'

def test_2():
	assert cotd_alphabetize.alpha('delta bravo romeo alpha alpha') == 'alpha bravo delta romeo'

def test_3():
	assert cotd_alphabetize.alpha('one two three four five') == 'five four one three two'

def test_4():
	assert cotd_alphabetize.alpha('alpha') == 'alpha'