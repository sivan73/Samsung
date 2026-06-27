import math
from math_wizard.constants import PI

class Shapes:
    @staticmethod
    def circle_area(radius):
        return PI * (radius ** 2)
        
    @staticmethod
    def hypotenuse(a, b):
        return math.hypot(a, b)