import pytest
from programs.rectangles import rectangle

def test_rectangle_area1():
    
    rec=rectangle(5,5)
    assert rec.findarea() == 25

def test_rectangle_area2():
    
    rec=rectangle(9,6)
    assert rec.findarea() == 54

def test_rectangle_area3():
    
    rec=rectangle(7,2)
    assert rec.findarea() == 14