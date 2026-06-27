Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def merge(a,b):
    c=[]
    a.reverse()
    b.reverse()
    while a != [] and b!= []:
        if a[-1] < b[-1] : c.append(a.pop())
        else: c.append(b.pop())

        
def merge(a,b):
    c=[]
    a.reverse()     #works better for pop and tail comparison
    b.reverse()     #works better for pop and tail comparison
    while a != [] and b!= []:
        if a[-1] < b[-1] : c.append(a.pop())
        else: c.append(b.pop())
    if a!= c : c.extend(b)
    else: c.extend(a)

    
a = [2,4,6,8,10]
b = [1,3,5,7,9,11,13]
merge(a,b)
a
[]
b
[13, 11]
a = [2,4,6,8,10]

b = [1,3,5,7,9,11,13]

def merge(a,b):
    c=[]
    a.reverse()     #works better for pop and tail comparison
    b.reverse()     #works better for pop and tail comparison
    while a != [] and b!= []:
        if a[-1] < b[-1] : c.append(a.pop())
        else: c.append(b.pop())
    if a== []:
        b.reverse()
        c.extend(b)
    else:
        a.reverse()
        c.extend(a)
    return c

merge(a,b)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

def mergesort(a):
    if len(a) <= 1 : return a
    else:
        return merge(mergesort(a[:len(a)//2]),mergesort(a[len(a)//2:]))

    
arr = random.sample(range(0,13),11)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    arr = random.sample(range(0,13),11)
NameError: name 'random' is not defined. Did you forget to import 'random'?
import random
arr = random.sample(range(0,13),11)
arr
[8, 1, 0, 11, 9, 6, 2, 5, 7, 10, 12]
mergesort(arr)
[0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12]
arr
[8, 1, 0, 11, 9, 6, 2, 5, 7, 10, 12]


#print
print('"')
"
print('print('print('print()')')')
SyntaxError: invalid syntax. Is this intended to be part of the string?
print("print("print("print("print("print()")")")")")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('''print("print("print("print("print()")")")")''')
print("print("print("print("print()")")")")
print("Print"i for i in range(8))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Print",i for i in range(8))
SyntaxError: Generator expression must be parenthesized
print("Print",(i for i in range(8)))
Print <generator object <genexpr> at 0x000001DA2D2C3ED0>
print("Print",*(i for i in range(8)))
Print 0 1 2 3 4 5 6 7
def mergesortlp(a):
    if len(a) <= 1 : return a
    else:
        for i in range(len(a))
        
SyntaxError: expected ':'
import time
time.time()
1781859736.7817466
time.date()

time.day()

import timedate

exit
Use exit() or Ctrl-D (end-of-file) to exit
no
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    no
NameError: name 'no' is not defined
def no():
    return 'No is defined :thumbs up'
no()
SyntaxError: invalid syntax
print(no())

def no():
    print("no is defined")

    
no()
no is defined
#yes
def yesno():
    if random.randint()%2 == random.randint()%2:
        print("yes")
        return "No"
    else:
        return "Yes"

    
yesno()

def yesno():
    if random.randint(0,99)%2 == random.randint(100,1000)%2:
        print("yes")
        return "No"
    else:
        return "Yes"

    
yesno()
yes
'No'
yesno()
yes
'No'
yesno()
'Yes'
def yesno():
    if random.randint(0,99)%2 == random.randint(100,1000)%2:
        return "Yes"
    else:
        return "No"

    
yesno()
'Yes'
yesno()
'Yes'
yesno()
'No'
yesno()
'No'
yesno()
'Yes'
yesno()
'Yes'
yesno()
'No'
yesno()
'No'
yesno()
'Yes'
yesno()
'Yes'
yesno()
'No'
yesno()
'Yes'
yesno()
'No'
def yesno():
    if random.randint(round(random.random()),time.time()/7)%2 == random.randint(100,1000)%2:
        return "Yes"
    else:
        return "No"

    
yesno()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    yesno()
  File "<pyshell#96>", line 2, in yesno
    if random.randint(round(random.random()),time.time()/7)%2 == random.randint(100,1000)%2:
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\random.py", line 339, in randint
    b = _index(b)
TypeError: 'float' object cannot be interpreted as an integer
def yesno():
    if random.randint(int(random.random()),time.time()/7)%2 == random.randint(100,1000)%2:
        return "Yes"
    else:
        return "No"

    
yesno()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    yesno()
  File "<pyshell#99>", line 2, in yesno
    if random.randint(int(random.random()),time.time()/7)%2 == random.randint(100,1000)%2:
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\random.py", line 339, in randint
    b = _index(b)
TypeError: 'float' object cannot be interpreted as an integer
def yesno():
    if random.randint(int(random.sample()),time.time()/7)%2 == random.randint(100,1000)%2:
        return "Yes"
    else:
        return "No"

    
yesno()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    yesno()
  File "<pyshell#102>", line 2, in yesno
    if random.randint(int(random.sample()),time.time()/7)%2 == random.randint(100,1000)%2:
TypeError: Random.sample() missing 2 required positional arguments: 'population' and 'k'
>>> def yesno():
...     if random.randint(int(random.sample(0,64)),time.time()/7)%2 == random.randint(100,1000)%2:
...         return "Yes"
...     else:
...         return "No"
... 
...     
>>> yesno()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    yesno()
  File "<pyshell#105>", line 2, in yesno
    if random.randint(int(random.sample(0,64)),time.time()/7)%2 == random.randint(100,1000)%2:
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\random.py", line 419, in sample
    raise TypeError("Population must be a sequence.  "
TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
>>> if 0 or 1 == 0 or 1:
...                     print("yes")
... 
...                     
yes
>>> dir()
...                     
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'arr', 'b', 'merge', 'mergesort', 'no', 'random', 'time', 'yesno']
>>> yesno()
...                     
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    yesno()
  File "<pyshell#105>", line 2, in yesno
    if random.randint(int(random.sample(0,64)),time.time()/7)%2 == random.randint(100,1000)%2:
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\random.py", line 419, in sample
    raise TypeError("Population must be a sequence.  "
TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
>>> def yesno()
SyntaxError: expected ':'
>>> numbers = [1, 2, 3, 4]
... for num in numbers:
...     numbers.remove(num)
... print(numbers)
SyntaxError: multiple statements found while compiling a single statement
>>> numbers = [1, 2, 3, 4]
>>> for num in numbers:
...     numbers.remove(num)
... print(numbers)
SyntaxError: invalid syntax
>>> for num in numbers:
...     numbers.remove(num)
... 
...     
>>> print(numbers)
[2, 4]
>>> 
