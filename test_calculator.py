

import pytest
from calculator import Calculator, calculate_average, is_prime


# ============================================
# FIXTURES
# ============================================

@pytest.fixture
def calc():
    """Fixture to create a fresh Calculator instance for each test"""
    return Calculator()


@pytest.fixture
def calc_with_history(calc):
    """Fixture with pre-populated history"""
    calc.add(5, 3)
    calc.subtract(10, 2)
    return calc


# ============================================
# TEST CALCULATOR CLASS - BASIC OPERATIONS
# ============================================

class TestCalculatorBasicOperations:
    """Test basic calculator operations"""
    
    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers"""
        result = calc.add(5, 3)
        assert result == 8
    
    def test_add_negative_numbers(self, calc):
        """Test adding negative numbers"""
        result = calc.add(-5, -3)
        assert result == -8
    
    def test_add_mixed_numbers(self, calc):
        """Test adding positive and negative"""
        result = calc.add(10, -3)
        assert result == 7
    
    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers"""
        result = calc.subtract(10, 3)
        assert result == 7
    
    def test_subtract_result_negative(self, calc):
        """Test subtraction resulting in negative"""
        result = calc.subtract(3, 10)
        assert result == -7
    
    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers"""
        result = calc.multiply(6, 7)
        assert result == 42
    
    def test_multiply_by_zero(self, calc):
        """Test multiplication by zero"""
        result = calc.multiply(100, 0)
        assert result == 0
    
    def test_multiply_negative_numbers(self, calc):
        """Test multiplying negative numbers"""
        result = calc.multiply(-5, -3)
        assert result == 15
    
    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers"""
        result = calc.divide(20, 4)
        assert result == 5
    
    def test_divide_with_decimal_result(self, calc):
        """Test division with decimal result"""
        result = calc.divide(10, 3)
        assert pytest.approx(result, rel=1e-9) == 10/3
    
    def test_divide_by_zero_raises_error(self, calc):
        """Test that dividing by zero raises ValueError"""
        with pytest.raises(ValueError) as exc_info:
            calc.divide(10, 0)
        assert "Cannot divide by zero" in str(exc_info.value)
    
    def test_power_positive_exponent(self, calc):
        """Test power with positive exponent"""
        result = calc.power(2, 8)
        assert result == 256
    
    def test_power_zero_exponent(self, calc):
        """Test power with zero exponent"""
        result = calc.power(5, 0)
        assert result == 1
    
    def test_power_negative_exponent(self, calc):
        """Test power with negative exponent"""
        result = calc.power(2, -3)
        assert result == 0.125


# ============================================
# TEST CALCULATOR - PARAMETRIZED TESTS
# ============================================

class TestCalculatorParametrized:
    """Parametrized tests for comprehensive coverage"""
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),
        (1, 1, 2),
        (100, 200, 300),
        (-5, 5, 0),
        (-10, -20, -30),
    ])
    def test_add_various_inputs(self, calc, a, b, expected):
        """Test addition with various input combinations"""
        assert calc.add(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 5, 5),
        (0, 0, 0),
        (5, 10, -5),
        (-5, -3, -2),
    ])
    def test_subtract_various_inputs(self, calc, a, b, expected):
        """Test subtraction with various inputs"""
        assert calc.subtract(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (0, 100, 0),
        (-2, 3, -6),
        (-2, -3, 6),
    ])
    def test_multiply_various_inputs(self, calc, a, b, expected):
        """Test multiplication with various inputs"""
        assert calc.multiply(a, b) == expected


# ============================================
# TEST CALCULATOR - HISTORY FUNCTIONALITY
# ============================================

class TestCalculatorHistory:
    """Test history tracking functionality"""
    
    def test_history_starts_empty(self, calc):
        """Test that new calculator has empty history"""
        assert len(calc.get_history()) == 0
    
    def test_history_records_addition(self, calc):
        """Test that addition is recorded in history"""
        calc.add(5, 3)
        history = calc.get_history()
        assert len(history) == 1
        assert "5 + 3 = 8" in history[0]
    
    def test_history_records_multiple_operations(self, calc):
        """Test multiple operations in history"""
        calc.add(5, 3)
        calc.multiply(2, 4)
        calc.subtract(10, 3)
        
        history = calc.get_history()
        assert len(history) == 3
    
    def test_clear_history(self, calc_with_history):
        """Test clearing history"""
        assert len(calc_with_history.get_history()) > 0
        calc_with_history.clear_history()
        assert len(calc_with_history.get_history()) == 0
    
    def test_history_is_copy(self, calc):
        """Test that get_history returns a copy"""
        calc.add(1, 2)
        history1 = calc.get_history()
        history2 = calc.get_history()
        
        # Modify one copy
        history1.append("fake")
        
        # Original should be unchanged
        assert len(history2) == 1


# ============================================
# TEST STANDALONE FUNCTIONS
# ============================================

class TestCalculateAverage:
    """Test calculate_average function"""
    
    def test_average_of_positive_numbers(self):
        """Test average of positive numbers"""
        result = calculate_average([1, 2, 3, 4, 5])
        assert result == 3.0
    
    def test_average_of_single_number(self):
        """Test average of single number"""
        result = calculate_average([42])
        assert result == 42.0
    
    def test_average_with_negatives(self):
        """Test average with negative numbers"""
        result = calculate_average([-5, 0, 5])
        assert result == 0.0
    
    def test_average_empty_list_raises_error(self):
        """Test that empty list raises ValueError"""
        with pytest.raises(ValueError) as exc_info:
            calculate_average([])
        assert "empty list" in str(exc_info.value).lower()
    
    @pytest.mark.parametrize("numbers,expected", [
        ([10, 20, 30], 20.0),
        ([1, 1, 1, 1], 1.0),
        ([100], 100.0),
        ([-10, 10], 0.0),
    ])
    def test_average_parametrized(self, numbers, expected):
        """Parametrized test for various averages"""
        assert calculate_average(numbers) == expected


class TestIsPrime:
    """Test is_prime function"""
    
    def test_prime_numbers(self):
        """Test known prime numbers"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in primes:
            assert is_prime(num) == True, f"{num} should be prime"
    
    def test_non_prime_numbers(self):
        """Test known non-prime numbers"""
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 15, 18, 20]
        for num in non_primes:
            assert is_prime(num) == False, f"{num} should not be prime"
    
    def test_negative_numbers_not_prime(self):
        """Test that negative numbers are not prime"""
        assert is_prime(-5) == False
        assert is_prime(-17) == False
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (100, False),
        (97, True),
    ])
    def test_is_prime_parametrized(self, number, expected):
        """Parametrized test for prime checking"""
        assert is_prime(number) == expected


# ============================================
# INTEGRATION TESTS
# ============================================

class TestCalculatorIntegration:
    """Integration tests for complete workflows"""
    
    def test_complex_calculation_workflow(self, calc):
        """Test a complex series of calculations"""
        # Calculate: (10 + 5) * 2 - 3 = 27
        result1 = calc.add(10, 5)      # 15
        result2 = calc.multiply(result1, 2)  # 30
        result3 = calc.subtract(result2, 3)  # 27
        
        assert result3 == 27
        assert len(calc.get_history()) == 3
    
    def test_calculator_maintains_state(self, calc):
        """Test that calculator maintains state across operations"""
        calc.add(1, 1)
        history_len_1 = len(calc.get_history())
        
        calc.multiply(2, 3)
        history_len_2 = len(calc.get_history())
        
        assert history_len_2 == history_len_1 + 1


# ============================================
# EDGE CASES AND ERROR HANDLING
# ============================================

class TestEdgeCases:
    """Test edge cases and error conditions"""
    
    def test_very_large_numbers(self, calc):
        """Test calculator with very large numbers"""
        result = calc.add(10**100, 10**100)
        assert result == 2 * (10**100)
    
    def test_very_small_numbers(self, calc):
        """Test calculator with very small numbers"""
        result = calc.add(0.0000001, 0.0000002)
        assert pytest.approx(result) == 0.0000003
    
    def test_float_precision(self, calc):
        """Test floating point precision"""
        result = calc.add(0.1, 0.2)
        assert pytest.approx(result, rel=1e-9) == 0.3


# ============================================
# PERFORMANCE MARKERS (optional)
# ============================================

@pytest.mark.slow
class TestPerformance:
    """Performance tests (marked as slow)"""
    
    def test_many_operations(self, calc):
        """Test performance with many operations"""
        for i in range(1000):
            calc.add(i, i+1)
        
        assert len(calc.get_history()) == 1000
