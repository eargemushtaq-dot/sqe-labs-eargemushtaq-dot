import pytest 
from calculator import add, subtract, multiply, divide
@pytest.mark.arithmetic
def test_add_two_positive_integers(): 
    assert add(2, 3) == 5 
 
 
@pytest.mark.arithmetic 
@pytest.mark.edge_case 
def test_divide_by_zero_raises_value_error(): 
    with pytest.raises(ValueError): 
        divide(10, 0) 
 
def test_add_two_positive_integers(): 
    """Adding two positive numbers gives their sum.""" 
    assert add(2, 3) == 5 
 
 
def test_add_positive_and_negative(): 
    """Adding a positive and negative number.""" 
    assert add(10, -3) == 7 
 
 
def test_add_two_floats(): 
    """Adding two float values.""" 
    assert add(1.5, 2.5) == 4.0 
 
 
def test_add_zero(): 
    """Adding zero is the identity operation — result equals the other 
operand.""" 
    assert add(7, 0) == 7 
 
 
# ─── Tests for subtract()
 
def test_subtract_positive_result(): 
    """Subtracting a smaller number gives a positive result.""" 
    assert subtract(10, 4) == 6 
 
 
def test_subtract_negative_result(): 
    """Subtracting a larger number gives a negative result.""" 
    assert subtract(3, 10) == -7 
 
 
# ─── Tests for multiply()
 
def test_multiply_two_integers(): 
    assert multiply(4, 5) == 20 
 
 
def test_multiply_by_zero(): 
    """Multiplying by zero always gives zero.""" 
    assert multiply(99, 0) == 0 
 
 
def test_multiply_negative_numbers(): 
 """Product of two negatives is positive.""" 
assert multiply(-3, -4) == 12 
 
 
# ─── Tests for divide()
 
def test_divide_even_division(): 
    assert divide(10, 2) == 5.0 
 
 
def test_divide_float_result(): 
    assert divide(7, 2) == 3.5 
 
 
def test_divide_by_zero_raises_value_error(): 
    """Dividing by zero must raise ValueError.""" 
    with pytest.raises(ValueError, match='Cannot divide by zero'): 
        divide(10, 0) 
 
 
# ─── Tests for power() 
 
def test_power_positive_exponent(): 
    assert power(2, 8) == 256 
 
 
def test_power_zero_exponent(): 
    """Any number to the power of 0 is 1.""" 
    assert power(99, 0) == 1 
 
 
# ─── Tests for is_even() 
def test_is_even_with_even_number(): 
    assert is_even(4) is True 
 
 
def test_is_even_with_odd_number(): 
    assert is_even(7) is False 
 
 
def test_is_even_with_zero(): 
    """Zero is defined as an even number.""" 
    assert is_even(0) is True 
