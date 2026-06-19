Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#D4S1
class A:
    def foo(self):
        return 10

    
class B:
    def foo(self):
        return 20

    
class C(A,B):
    pass

c = c()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c = c()
NameError: name 'c' is not defined. Did you mean: 'C'?
c.foo()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.foo()
NameError: name 'c' is not defined. Did you mean: 'C'?
def c():
    print(x)

    
c.foo()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c.foo()
AttributeError: 'function' object has no attribute 'foo'
c1 = 20
id(c1)
140719461156568
id(c)
2345082585856
f = iter(['a','b','c'])
next(f)
'a'
next(f)
'b'
next(f)
'c'
next(f)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    next(f)
StopIteration
def foo():
    yield 1
    yield 2
    yield 3

    
foo()
<generator object foo at 0x0000022201BE31C0>
for i in foo(): print(i)

1
2
3
def foo():
    print('line 1')
    yield 1
    print('line 2')
    yield 2
    print('line 3')
    yield 3

    
for i in foo(): print(i)

line 1
1
line 2
2
line 3
3
f = iter(foo())
next(f)
line 1
1
next(f)
line 2
2
next()f
SyntaxError: invalid syntax
next(f)
line 3
3
next(f)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    next(f)
StopIteration
f = iter(foo())
.
.
SyntaxError: invalid syntax


class stack:
    def __init__(self:)
    
SyntaxError: invalid syntax
class stack:
    def __init__(self):
        self.data = []

        
class stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        return self.pop()
    def peek(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)
    def __add__(self,val):
        self.push(val)
    def __radd__(self,val):
        self.push(val)
    def __repr__(self):
        retval = ''
        for i in (self.data) : retval += str(self.data[i]) + '->'

        
class stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        return self.pop()
    def peek(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)
    def __add__(self,val):
        self.push(val)
    def __radd__(self,val):
        self.push(val)
    def __repr__(self):
        retval = ''
        for i in (self.data) : retval += str(self.data[i]) + '->'
        return retval

    
s = stack()
class stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        return self.pop()
    def peek(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)
    def __add__(self,val):
        self.push(val)
    def __radd__(self,val):
        self.push(val)
    def __repr__(self):
        retval = ''
        for i in range(len(self.data)) : retval += str(self.data[i]) + '->'
        return retval

    
s = stack()
s.push(5)
s.push(6)
s
5->6->
s.push(66)
s.push(7)
s
5->6->66->7->
s.pop()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  [Previous line repeated 1023 more times]
RecursionError: maximum recursion depth exceeded
s.pop(1)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.pop(1)
TypeError: stack.pop() takes 1 positional argument but 2 were given
s
5->6->66->7->
class stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)
    def __add__(self,val):
        self.push(val)
    def __radd__(self,val):
        self.push(val)
...     def __repr__(self):
...         retval = ''
...         for i in range(len(self.data)) : retval += str(self.data[i]) + '->'
...         return retval
... 
...     
>>> s
5->6->66->7->
>>> s.pop()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  File "<pyshell#82>", line 7, in pop
    return self.pop()
  [Previous line repeated 1023 more times]
RecursionError: maximum recursion depth exceeded
>>> s = stack()
>>> s

>>> s.push(1)
>>> s.push(7)
>>> s
1->7->
>>> s.pop()
7
>>> class stack:
...     def __init__(self):
...         self.data = []
...     def push(self,val):
...         self.data.append(val)
...     def pop(self):
...         return self.data.pop()
...     def peek(self):
...         return self.data[-1]
...     def __len__(self):
...         return len(self.data)
...     def __add__(self,val):
...         self.push(val)
...     def __radd__(self,val):
...         self.push(val)
...     def __repr__(self):
...         retval = ''
...         for i in range(len(self.data)) : retval += str(self.data[i]) + '->'
...         return retval
... 
...     

================================================ RESTART: Shell ================================================
>>> expr = '[][][[]]]]['

================================================ RESTART: Shell ================================================
>>> expr2 = '[][[[[]]]][[]]'

================================================ RESTART: Shell ================================================
>>> print('clean')
