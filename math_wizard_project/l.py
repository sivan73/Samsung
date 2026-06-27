

import math

# Pulling from built-in math object
PI = math.pi
E = math.e

# Custom mathematical constants
GOLDEN_RATIO = 1.618033988749895
EULER_MASCHERONI = 0.577215664901532

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

import math
from math_wizard.constants import PI

class Shapes:
    @staticmethod
    def circle_area(radius):
        return PI * (radius ** 2)
        
    @staticmethod
    def hypotenuse(a, b):
        # Using built-in math object internally
        return math.hypot(a, b)



# Expose constants
from .constants import PI, E, GOLDEN_RATIO

# Expose wrapped built-ins
from .core_extensions import MathWrapper

# Expose custom modules
from .custom_modules.geometry import Shapes

# Defining __all__ controls what gets imported with "from math_wizard import *"
__all__ = ["PI", "E", "GOLDEN_RATIO", "MathWrapper", "Shapes"]


