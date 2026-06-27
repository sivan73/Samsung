import math

class MathWrapper:
    """Wraps built-in math functions with extra validation or features."""
    
    @staticmethod
    def safe_sqrt(value):
        if value < 0:
            raise ValueError("Cannot calculate the square root of a negative number in real domain.")
        return math.sqrt(value)

    @staticmethod
    def factorial(n):
        return math.factorial(n)