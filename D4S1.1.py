Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
expr2 = '[][[[[]]]][[]]'
expr = '[][][[]]]]['

for i in exp:
    print(exp[i])

    
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    for i in exp:
NameError: name 'exp' is not defined. Did you mean: 'expr'?
for i in expr:
    print(expr[i])

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print(expr[i])
TypeError: string indices must be integers, not 'str'
for i in expr:
    print(i)

    
[
]
[
]
[
[
]
]
]
]
[
print'e'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(...)
Ellipsis
print(.)
SyntaxError: invalid syntax
print(....)
SyntaxError: invalid syntax
for i in expr:
    print(s)

    
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(s)
NameError: name 's' is not defined
s = '(->'
expr3 = "{[][][][[[[[]]]]][][[][][[]][][][[]]][}[]"
class Queue:
    def __int__(self):
        self.data = []
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(self.data) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval

    
q1 = Queue()
q1.enqueue(5)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    q1.enqueue(5)
  File "<pyshell#43>", line 5, in enqueue
    self.data.append(val)
AttributeError: 'Queue' object has no attribute 'data'
q1
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    q1
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#43>", line 19, in __repr__
    retval = '('+ "->".join(self.data) + ')'
AttributeError: 'Queue' object has no attribute 'data'
class Queue:
    def __int__(self):
        self.data = []
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval

    
q1
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    q1
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#43>", line 19, in __repr__
    retval = '('+ "->".join(self.data) + ')'
AttributeError: 'Queue' object has no attribute 'data'
q1 = Queue()
q1
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    q1
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#48>", line 19, in __repr__
    retval = '('+ "->".join(map(str,(self.data))) + ')'
AttributeError: 'Queue' object has no attribute 'data'
q1.enqueue(1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    q1.enqueue(1)
  File "<pyshell#48>", line 5, in enqueue
    self.data.append(val)
AttributeError: 'Queue' object has no attribute 'data'
class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval

    
q1 = Queue()
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1
(5->6->7->8)
25*25
625
def J(n,k):
    for k in range(n):
        return (J(n-1,k)+k) % n

    
J(7,3)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    J(7,3)
  File "<pyshell#65>", line 3, in J
    return (J(n-1,k)+k) % n
  File "<pyshell#65>", line 3, in J
    return (J(n-1,k)+k) % n
  File "<pyshell#65>", line 3, in J
    return (J(n-1,k)+k) % n
  [Previous line repeated 4 more times]
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
def J(n,k):
    if n== 1:
        return 0
    else:
        return (J(n-1,k)+k) % n
    print(J(n,k)+1)

    
J(7,3)
3
def J(n,k):
    if n== 1:
        return 0
    else:
        return ((J(n-1,k)+k) % n) +1

    
J(7,3)
3
k = 3

while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
        print(q.dequeue())

        
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    while len(q) != 1:
NameError: name 'q' is not defined. Did you mean: 'q1'?
q = Queue([1,2,3,4,5,6,7])
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    q = Queue([1,2,3,4,5,6,7])
TypeError: Queue.__init__() takes 1 positional argument but 2 were given
class Queue:
    def __init__([self]):
        self.data = []
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval
    
SyntaxError: invalid syntax
class Queue:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = list(data)

    def enqueue(self, val):  # add at back
        self.data.append(val)

    def dequeue(self):       # remove from front
        return self.data.pop(0)

    def front(self):         # peek front
        return self.data[0]

    def __len__(self):       # size
        return len(self.data)

    def __repr__(self):      # pretty print
        return '(' + "->".join(map(str, self.data)) + ')'


k = 3
q = Queue([1,2,3,4,5,6,7])
SyntaxError: multiple statements found while compiling a single statement
k = 3
q = Queue([1,2,3,4,5,6,7])
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
        print(q.enqueue(val))

        
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
Traceback (most recent call last):
  File "<pyshell#95>", line 5, in <module>
    print(q.enqueue(val))
KeyboardInterrupt
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.enqueue(val))

    
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
Traceback (most recent call last):
  File "<pyshell#97>", line 5, in <module>
    print(q.enqueue(val))
KeyboardInterrupt
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue(val))

    
Traceback (most recent call last):
  File "<pyshell#99>", line 5, in <module>
    print(q.dequeue(val))
TypeError: Queue.dequeue() takes 1 positional argument but 2 were given
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue())

    
6
6
6
6
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
3
3
3
Traceback (most recent call last):
  File "<pyshell#101>", line 5, in <module>
    print(q.dequeue())
KeyboardInterrupt
q
(3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3)
class Queue:
    def __init__([self, data= None]):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval
    
SyntaxError: invalid syntax
class Queue:
    def __init__(self, data= None):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.push(val)
    def __radd__(self,val):     #operator overloading+
        self.push(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval

    
q
(3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->4->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->5->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->6->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->7->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->1->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->2->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3->3)
q = Queue([1,2,3,4,5,6,7])
k = 3
q
(1->2->3->4->5->6->7)
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
        print(q.dequeue)

        
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
Traceback (most recent call last):
  File "<pyshell#115>", line 5, in <module>
    print(q.dequeue)
KeyboardInterrupt
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue)

    
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
<bound method Queue.dequeue of (1->2->3->4->5->6->7)>
<bound method Queue.dequeue of (4->5->6->7->1->2->3)>
<bound method Queue.dequeue of (7->1->2->3->4->5->6)>
<bound method Queue.dequeue of (3->4->5->6->7->1->2)>
<bound method Queue.dequeue of (6->7->1->2->3->4->5)>
<bound method Queue.dequeue of (2->3->4->5->6->7->1)>
<bound method Queue.dequeue of (5->6->7->1->2->3->4)>
Traceback (most recent call last):
  File "<pyshell#118>", line 5, in <module>
    print(q.dequeue)
KeyboardInterrupt
class Queue:
    def __init__(self, data= None):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
    def enqueue(self,val): #adding at the back of the queue
        self.data.append(val)
    def dequeue(self): #removing at the back of queue
        return self.data.pop(0)
    def front(self):        #return element at the front of queue
        return self.data[0]
    def emplace(self,val): #update last entry/ back of queue
        self.data[-1] = val
    def __len__(self):      #return size of queue
        return len(self.data)
    def __add__(self,val):      #operator overloading+
        self.enqueue(val)
    def __radd__(self,val):     #operator overloading+
        self.enqueue(val)
    def __repr__(self):         #(a ->b ->c)
        retval = '('+ "->".join(map(str,(self.data))) + ')'
        # for i in range(len(self.data)) : retval += str(self.data[i] + '->')
        return retval

    
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue())

    
1
5
3
2
4
7
q
(6)
q = Queue([for i in range(7)])
SyntaxError: invalid syntax
q = Queue([i for i in range(7)])
q
(0->1->2->3->4->5->6)
q = Queue([i for i in range(1,8)])
q
(1->2->3->4->5->6->7)
k
3
while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue())

    
4
1
6
5
7
3
Hash function/ mapping
SyntaxError: invalid syntax
Class HashTable:
    
SyntaxError: invalid syntax
class HashTable:
    def __int__(self,size):
        self.size = size
        self.table{}
        
SyntaxError: invalid syntax
class HashTable:
    def __int__(self,size):
        self.size = size
        self.table{}
        
SyntaxError: invalid syntax
class HashTable:
    def __init__(self,size):
        self.size = size
        self.table{}
        
SyntaxError: invalid syntax
class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[i] = []
    def hash(self, key):
        return key % self.size
    def get(self,key):
        return self.table[self.hash(key)]
    def put(self,key,value):
        bucket = self.table[self.hash(key)]
        if value not in bucket:
            bucket.append(value)

            
table = HashTable(8)
for key in table.table.keys():
    print(key, table.table[key])

    
0 []
1 []
2 []
3 []
4 []
5 []
6 []
7 []
book = "Hello World"
key = sum(map(ord,book))
key
1052
table.put(key,book)
table
<__main__.HashTable object at 0x000001F824652270>
list(table)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    list(table)
TypeError: 'HashTable' object is not iterable
for key in table.table.keys():
    print(key, table.table[key])

    
0 []
1 []
2 []
3 []
4 ['Hello World']
5 []
6 []
7 []
books = ["hello WORLD","New World","Lenovo","Samsung"]
for i in books:
    key = sum(map(ord,i))
    table.put(key,i)
    print(key)

    
956
850
627
734
for key in table.table.keys():
    print(key,table.table[key])

    
0 []
1 []
2 ['New World']
3 ['Lenovo']
4 ['Hello World', 'hello WORLD']
5 []
6 ['Samsung']
7 []
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[i] = None  
    def hash(self, key):
        return key % self.size
    def put(self, key, value):
        initial_index = self.hash(key)
        index = initial_index        
        # Step linearly (+1) until an empty slot is found
        while self.table[index] is not None:
            if self.table[index] == value:
                return # Value already exists           
            index = (index + 1) % self.size            
            # Table is completely full
            if index == initial_index:
                print("Table is full!")
                return                
        self.table[index] = value

        

2**0.5
1.4142135623730951
import math
sqrt(2)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    sqrt(2)
NameError: name 'sqrt' is not defined
math.sqrt(2)
1.4142135623730951
del math
dir(math)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    dir(math)
NameError: name 'math' is not defined. Did you forget to import 'math'?
'
dir()
['HashTable', 'HashTableLinearProbing', 'J', 'Queue', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'book', 'books', 'expr', 'expr2', 'expr3', 'i', 'k', 'key', 'q', 'q1', 's', 'table', 'val']
dir
<built-in function dir>

================================================ RESTART: Shell ================================================
dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
x1 = [9,1,8,2,7,3,6,4,5,0]
def bin_search(x,key):
    low=0
    high = len(x)
    mid = (low+high)//2
    while key != x[mid] and low <high:
        if x[mid] < key:
            low = mid + 1
        elif x[mid] > key +1
        
SyntaxError: expected ':'
def bin_search(x,key):
    low=0
    high = len(x)
    mid = (low+high)//2
    while key != x[mid] and low <high:
        if x[mid] < key:   #right half search
            low = mid + 1
        elif x[mid] > key:  #left half search
            high = mid - 1
        mid = (low+high)//2
    if low<high : return mid
    else: return -1

    
bin_search(x1,9)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    bin_search(x1,9)
  File "<pyshell#203>", line 5, in bin_search
    while key != x[mid] and low <high:
IndexError: list index out of range
bin_search(9,x1)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    bin_search(9,x1)
  File "<pyshell#203>", line 3, in bin_search
    high = len(x)
TypeError: object of type 'int' has no len()
def bin_search(x,key):
    low=0
    high = len(x)
    mid = (low+high) // 2
    while key != x[mid] and low <high:
        if x[mid] < key:   #right half search
            low = mid + 1
        elif x[mid] > key:  #left half search
            high = mid - 1
        mid = (low+high)//2
    if low<high : return mid
    else: return -1

    
x1.bin_search(9)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    x1.bin_search(9)
AttributeError: 'list' object has no attribute 'bin_search'
bin_search(x1,4)
-1
bin_search(x1,0)
-1
def bin_search(x,key):
    low=0
    high = len(x)-1
    mid = (low+high) // 2
    while key != x[mid] and low <high:
        if x[mid] < key:   #right half search
            low = mid + 1
        elif x[mid] > key:  #left half search
            high = mid - 1
        mid = (low+high)//2
    if low<= high : return mid
    else: return -1

    
bin_search(x1,4)
-1
x1
[9, 1, 8, 2, 7, 3, 6, 4, 5, 0]
bin_search(x1,4)
-1
bin_search(sort(x1),4)
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    bin_search(sort(x1),4)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
bin_search(x1.sort,4)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    bin_search(x1.sort,4)
  File "<pyshell#212>", line 3, in bin_search
    high = len(x)-1
TypeError: object of type 'builtin_function_or_method' has no len()
bin_search(x=(x1.sort()),4)
SyntaxError: positional argument follows keyword argument
bin_search(x=(x1.sort),4)
SyntaxError: positional argument follows keyword argument
x1.sort()
bin_search(x1,4)
4
bin_search(x1,9)
9
x1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x1.append(11)
x1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
bin_search(x1,11)
10
def sqrt1(n):
    return n**0.5
sqrt1(2)
SyntaxError: invalid syntax
def sqrt1(n):
    return n**0.5
sqrt1(2)
SyntaxError: invalid syntax
def sqrt(n, e= 0.01):
    low = 0
    high = n
    mid = (low+high)/2
    while abs(n - mid * mid)> e and low != high:
        if n> mid*mid : low = mid
        else : high = mid
        mid =(low + high)/2
    if low<= high : return mid
    else: return -1

    
sqrt(2)
1.4140625
def sqrt1(w):
    return w**0.5

sqrt1(2)
1.4142135623730951
import math
math.sqrt(2)
1.4142135623730951
sqrt1(2) is math.sqrt(2)
False
int(sqrt1(2))
1
float(sqrt(2))
1.4140625
def bin_search2(x,key):
    if len(x)==0: return 'not found'
    mid = len(x)//2
    if x[mid] == key : return 'found'
    elif: x[mid] < key : return bin_search(x[mid+1 :],key)  #right half
    
SyntaxError: invalid syntax
def bin_search2(x,key):
    if len(x)==0: return 'not found'
    mid = len(x)//2
    if x[mid] == key : return 'found'
    elif x[mid] < key : return bin_search(x[mid+1 :],key)  #right half
    else: return bin_search(x[:mid],key)                    #left half

    
bin_search2(x2,13)
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    bin_search2(x2,13)
NameError: name 'x2' is not defined. Did you mean: 'x1'?
x2 = [32,23,51,11,27,08,76,3]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
x2 = [32,23,51,11,27,8,76,3]
binsearch2(x2,76)
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    binsearch2(x2,76)
NameError: name 'binsearch2' is not defined. Did you mean: 'bin_search2'?
bin_search2(x2,76)
1
def bin_search2(x,key):
    if len(x)==0: return 'not found'
    mid = len(x)//2
    if x[mid] == key : return 'found'
    elif x[mid] < key : return bin_search2(x[mid+1 :],key)  #right half
    else: return bin_search2(x[:mid],key)                    #left half

    
NameError: name 'binsearch2' is not defined. Did you mean: 'bin_search2'?
bin_search2(x2,76)
SyntaxError: invalid syntax
bin_search2(x2,76)
'found'
bin_search2(x2,52)
'not found'
bin_search(x2,76)
6
x2
[32, 23, 51, 11, 27, 8, 76, 3]
bin_search(x2,3)
0
bin_search(x2,32)
-1
x2.sort()
bin_search(x2,3)
0
bin_search(x2,32)
5
x2
[3, 8, 11, 23, 27, 32, 51, 76]
x1+x2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 3, 8, 11, 23, 27, 32, 51, 76]
sort(x1+x2, reverse=true)
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    sort(x1+x2, reverse=true)
NameError: name 'sort' is not defined. Did you mean: 'sqrt'?
(a = x1+x2).sort(reverse=true)
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a = x1+x2
print(a.sort(reverse=true))
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    print(a.sort(reverse=true))
NameError: name 'true' is not defined. Did you mean: 'True'?
print(a.sort(reverse=True))
None
a
[76, 51, 32, 27, 23, 11, 11, 9, 8, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]
print(a)
[76, 51, 32, 27, 23, 11, 11, 9, 8, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]
print(a.sorted())
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    print(a.sorted())
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
print(sorted(a))
[0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 11, 11, 23, 27, 32, 51, 76]
help
Type help() for interactive help, or help(object) for help about object.
help()
Welcome to Python 3.14's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.14/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

You can use the following keyboard shortcuts at the main interpreter prompt.
F1: enter interactive help, F2: enter history browsing mode, F3: enter paste
mode (press again to exit).

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> modules spam

Here is a list of modules whose name or summary contains 'spam'.
If there are any, enter a module name to get more help.

__phello__.spam 
0.01s - Debugger warning: It seems that frozen modules are being used, which may
0.05s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
0.00s - to python to disable frozen modules.
0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.

help> exit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> sys.stdin.readline()
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    sys.stdin.readline()
NameError: name 'sys' is not defined. Did you forget to import 'sys'?
>>> import sys
>>> z = sys.stdin.readline("Enter a paragraph:")
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    z = sys.stdin.readline("Enter a paragraph:")
TypeError: must be int, not str
>>> z = sys.stdin.readline()
hello world
>>> z
'hello world\n'
>>> strip(z)
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    strip(z)
NameError: name 'strip' is not defined
>>> z.strip()
'hello world'
>>> list(z.strip())
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> list(z)
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\n']
>>> tuple(z)
('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\n')
>>> import string
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'bin_search', 'bin_search2', 'math', 'sqrt', 'sqrt1', 'string', 'sys', 'x1', 'x2', 'z']
