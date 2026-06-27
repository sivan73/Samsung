Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Employee:
...     def __init__(self, names, salary):
...         self.name = names
...         self.salary = 0.0
...         self.set_salary(salary)
...     def set_salary(self, salary):
...         if salary > 0:
...             self.salary = salary
...         else:
...             print("Salary must be  > zero :/")
...     def get_salary(self):
...         return self.__salary
...     def __str__(self):
...         return f"Employee(Name={self.__name}, Salary={self.__salary})"
... 
...     
>>> emp1 = Employee("random name", 50000)
>>> emp1
<__main__.Employee object at 0x000001D00EA23620>
>>> print(emp1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(emp1)
  File "<pyshell#1>", line 14, in __str__
    return f"Employee(Name={self.__name}, Salary={self.__salary})"
AttributeError: 'Employee' object has no attribute '_Employee__name'
>>> class Employee:
...     def __init__(self, names, salary):
...         self.name = names
...         self.salary = 0.0
...         self.set_salary(salary)
...     def set_salary(self, salary):
...         if salary > 0:
...             self.salary = salary
...         else:
...             print("Salary must be  > zero :/")
...     def get_salary(self):
...         return self.__salary
...     def __str__(self):
...         return f"Employee(Name={self.name}, Salary={self.salary})"
... 
...     
>>> emp1 = Employee("random name", 50000)
... 
>>> print(emp1)
Employee(Name=random name, Salary=50000)
>>> emp1.set_salary(55000)
>>> print("After salary increment:", emp1)
After salary increment: Employee(Name=random name, Salary=55000)
>>> emp1.set_salary(-1000)
Salary must be  > zero :/
