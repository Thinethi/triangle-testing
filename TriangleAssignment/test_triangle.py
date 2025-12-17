import pytest
from triangle import classify_triangle


# Test for Equilateral Triangle
def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"

# Test for Isosceles Triangle
def test_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "Isosceles"

# Test for Scalene Triangle
def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"

# Test for Zero side length (ValueError expected)
def test_zero_side_length():
    with pytest.raises(ValueError):
        classify_triangle(0, 4, 5)

# Test for Negative side length (ValueError expected)
def test_negative_side_length():
    with pytest.raises(ValueError):
        classify_triangle(-3, 4, 5)

# Test for Triangle Inequality Violation - Scenario 1
def test_triangle_inequality_violation_1():
    with pytest.raises(ValueError):
        classify_triangle(1, 2, 3)

# Test for Triangle Inequality Violation - Scenario 2
def test_triangle_inequality_violation_2():
    with pytest.raises(ValueError):
        classify_triangle(5, 1, 1)

# Test floating point Equilateral Triangle
def test_floating_point_equilateral():
    assert classify_triangle(3.0, 3.0, 3.0) == "Equilateral"

# Test floating point Isosceles Triangle
def test_floating_point_isosceles():
    assert classify_triangle(5.5, 5.5, 2.5) == "Isosceles"

# Test floating point Scalene Triangle
def test_floating_point_scalene():
    assert classify_triangle(4.1, 5.2, 6.3) == "Scalene"

# Test very large numbers (Equilateral)
def test_large_number_equilateral():
    assert classify_triangle(1000000, 1000000, 1000000) == "Equilateral"

# Test boundary values - barely valid triangle
def test_boundary_triangle():
    assert classify_triangle(1, 1, 1.9999) == "Isosceles"

# Test triangle inequality violation with large numbers
def test_large_triangle_inequality_violation():
    with pytest.raises(ValueError):
        classify_triangle(1000000, 1, 1)

# Test zero side with floating point zero
def test_zero_side_float():
    with pytest.raises(ValueError):
        classify_triangle(0.0, 2, 2)