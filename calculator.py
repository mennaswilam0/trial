

class Calculator:
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
      
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
     
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
   
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
      
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self):
        """
        Get calculation history
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()


def calculate_average(numbers):
    """
    Calculate average of a list of numbers
    
    Args:
        numbers: List of numbers
    
    Returns:
        Average of the numbers
    
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n: Number to check
    
    Returns:
        True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Demo usage
    calc = Calculator()
    
    print("Calculator Demo")
    print("-" * 40)
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    
    print("\\nHistory:")
    for calculation in calc.get_history():
        print(f"  {calculation}")
    
    print(f"\\nAverage of [1,2,3,4,5]: {calculate_average([1,2,3,4,5])}")
    print(f"Is 17 prime? {is_prime(17)}")

