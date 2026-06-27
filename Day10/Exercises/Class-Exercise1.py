Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class student:
    def __init__(self,names,marks):
        self.name = name
        self.marks = 0
        self.set_marks(marks)
    def  set_marks(self,marks):
        if 0<=marks <=100:
            self.marks = marks
        else:
            print("Invalid marks, please enter marks between 0 and 100")
        def get_marks(self):
            return self.marks
        def __str__(self):
            return f"Student (Name = {self.name}, Marks = {self.marks})"

        
student1 = student("JOhn", 85)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    student1 = student("JOhn", 85)
  File "<pyshell#14>", line 3, in __init__
    self.name = name
NameError: name 'name' is not defined. Did you mean: 'names'?
class student:
    def __init__(self,names,marks):
        self.name = names
        self.marks = 0
        self.set_marks(marks)
    def  set_marks(self,marks):
        if 0<=marks <=100:
            self.marks = marks
        else:
            print("Invalid marks, please enter marks between 0 and 100")
        def get_marks(self):
            return self.marks
        def __str__(self):
            return f"Student (Name = {self.name}, Marks = {self.marks})"

        
student1 = student("JOhn", 85)
print(student1)
<__main__.student object at 0x000002244FA13770>
student1
<__main__.student object at 0x000002244FA13770>
student1.set_marks(95)
print(student1)
<__main__.student object at 0x000002244FA13770>
str(student1)
'<__main__.student object at 0x000002244FA13770>'
student1
<__main__.student object at 0x000002244FA13770>
class student:
    def __init__(self,names,marks):
        self.name = names
...         self.marks = 0
...         self.set_marks(marks)
...     def  set_marks(self,marks):
...         if 0<=marks <=100:
...             self.marks = marks
...         else:
...             print("Invalid marks, please enter marks between 0 and 100")
...     def get_marks(self):
...          return self.marks
...     def __str__(self):
...          return f"Student (Name = {self.name}, Marks = {self.marks})"
... 
...         
>>> student1 = student("JOhn", 85)
>>> student1
<__main__.student object at 0x000002244FA138C0>
>>> class student:
...     def __init__(self,names,marks):
...         self.name = names
...         self.marks = 0
...         self.set_marks(marks)
...     def  set_marks(self,marks):
...         if 0<=marks <=100:
...             self.marks = marks
...         else:
...             print("Invalid marks, please enter marks between 0 and 100")
...     def get_marks(self):
...          return self.marks
...     def __str__(self):
...          return f"Student (Name = {self.name}, Marks = {self.marks})"
... 
...         
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'student', 'student1']
>>> del student
>>> del student1
>>> class Student:
...     def __init__(self,names,marks):
...         self.name = names
...         self.marks = 0
...         self.set_marks(marks)
...     def  set_marks(self,marks):
...         if 0<=marks <=100:
...             self.marks = marks
...         else:
...             print("Invalid marks, please enter marks between 0 and 100")
...     def get_marks(self):
...          return self.marks
...     def __str__(self):
...          return f"Student (Name = {self.name}, Marks = {self.marks})"
... 
...         
>>> student1 = Student("John", 85)
>>> student1
<__main__.Student object at 0x000002244FA138C0>
>>> str(student1)
'Student (Name = John, Marks = 85)'
>>> print(student1)
Student (Name = John, Marks = 85)
