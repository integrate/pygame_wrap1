from wrap_engine import math_utils

def test_circle_calcs():
    dx, dy = math_utils.get_point_on_circle([100, 100], [100, 50], 90)
    assert (-50, 50) == (round(dx), round(dy))

def test_point_calcs1():
    x, y = math_utils.get_point_by_angle([100, 100], 90, 50)
    assert (50, 100) == (round(x), round(y))

def test_point_calcs2():
    x, y = math_utils.get_point_by_angle([100, 100], -90, 50)
    assert (150, 100) == (round(x), round(y))