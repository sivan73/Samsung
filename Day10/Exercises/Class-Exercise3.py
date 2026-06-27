Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Car:
...     def __init__(self, brand, speed):
...         self.brand = brand
...         self.speed = 0.0
...         self.set_speed(speed)
... 
...     def set_speed(self, speed):
...         if speed >= 0:
...             self.speed = speed
...         else:
...             print("Speed cannot be negative.")
...     def get_speed(self):
...         return self.speed
...     def __str__(self) ->:
...         return f"Car(Brand={self.brand}, Speed={self.speed} km/h)"
...     
SyntaxError: expected ':'
>>> class Car:
...     def __init__(self, brand, speed):
...         self.brand = brand
...         self.speed = 0.0
...         self.set_speed(speed)
... 
...     def set_speed(self, speed):
...         if speed >= 0:
...             self.speed = speed
...         else:
...             print("Speed cannot be negative.")
...     def get_speed(self):
...         return self.speed
...     def __str__(self) :
...         return f"Car(Brand={self.brand}, Speed={self.speed} km/h)"
... 
...     
>>> car1 = Car("Toyota",80)
>>> car2 = Car("Tata", 90)
>>> print(car1)
Car(Brand=Toyota, Speed=80 km/h)
>>> print(car2)
Car(Brand=Tata, Speed=90 km/h)
>>> car1.set_speed(120)
>>> car2.set_speed(-80)
Speed cannot be negative.
>>> print(car1)
Car(Brand=Toyota, Speed=120 km/h)
>>> print(car2)
Car(Brand=Tata, Speed=90 km/h)
