Abstraction -
    Living Being
        Animal Plant
        Inv Vert
            Mammals
                Human

ENcapsulation - methodd + data
Polymorphism - Runtime
Inheritance :

    A
    B
    C



A       C
    B

    

    A
B       C
    D

Stack - parsing
    push
    pop
    peek

    status checks - full empty


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

#Josephus N=7 -> q[],k=3

while len(q) != 1:
    for i in range(k):
        val = q.dequeue()
        q.enqueue(val)
    print(q.dequeue())



















Store:
    Indexable data struct - arrays
Hask function / Mapping
    finds an empty slot




class HashTable:                    #Seperate chaining - storing multiple items in a bucket list
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

book = "Hello World"
key = sum(map(ord,book))
key

table.put(key,book)


for key in table.table.keys():
    print(key, table.table[key])


books = ["hello WORLD","New World","Lenovo","Samsung"]
for i in books:
    key = sum(map(ord,i))
    table.put(key,i)
    print(key)

for key in table.table.keys():
    print(key,table.table[key])





    unsorted/unindexed data
        sequential/linear search
        1+2+3+...n for n elements
        n(n+1)/2 divide by n for average over n lements
        = n(n+1)/2
        = O(n)
    min/max
        curr,maxval = 0 x[0]
        for i in range(1,len(x)):
            if x[curr] < x[i] : curr,maxval = i,x[i]

        curr,minval = 0,x[0]
        for i in range(1,len(x)):
            if x[curr] > x[i] : curr,minval = i,x[i]

sorted data





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





