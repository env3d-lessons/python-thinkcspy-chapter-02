import math
from main import *


def test_calculate_price_have_remaining():
    assert abs(calculate_price(7) - ((6 * 1.25) + 1.50)) < 0.0000001

def test_distance_SCIENCE_WORLD_LANGARA():
    assert abs(distance(49.272967, -123.101732, 49.225798, -123.108383) - 5200) < 70

def test_calculate_price_non_3_multiple():
    assert abs(calculate_price(2) - (2 * 1.5)) < 0.0000001

def test_calculate_price_3_multiple():
    assert abs(calculate_price(6) - (6 * 1.25)) < 0.0000001

def test_cone_surface_area():
    def expected_area(r, h):
        return (math.pi * r) * (r + math.sqrt(h ** 2 + r ** 2))
    assert abs(expected_area(5, 10) - cone_surface_area(5, 10)) <= 0.00001

def test_midterms_weighted():
    assert abs(midterms_weighted(5, 10, 20, 40) - 10) <= 0.00001

def test_calculate_average():
    assert abs(calculate_average(5, 10, 20, 40) - 50) <= 0.00001

def test_convert_to_percentage_basic():
    assert abs(convert_to_percentage(5, 10) - 50) <= 0.0001
    assert abs(convert_to_percentage(5, 20) - 25) <= 0.0001

def test_average_mark_normal():
    assert abs(average_mark(60, 70) - 65) <= 0.00001

def test_average_mark_boundary():
    assert average_mark(1, 1) == 1
