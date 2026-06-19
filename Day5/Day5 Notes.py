sorting
    organizing into monotonic sequence
    orderable, define < operator, = operator

non-indexable - i.e linkedlist
    Bubble sort

indexable - array/list(python)


arr = random.sample(range(0,13),11)

#Bubble sort - Mutating only (inplace)

def bubble(a,left,right):
    for i in range(left,right-1):
        if a[i] > a[i+1] : a[i],a[i+1] = a[i+1],a[i]

def bubblesort(a):
    for i in range(len(a)) : bubble(a,0,len(a)-i)


#Selection sort - Mutating only(inplace)

                find min/max
                swap if greater/lesser/ wrt current location
                O(n*n)

def selectionsort(x,compare):
    for i in range(len(x)):
        loc = find_element(x,i,len(x),compare)
        if compare(x[loc],x[i]) : x[loc],x[i] = x[i],x[loc]

        

def selectionsort(x,compare):
    for i in range(len(x)):
        loc = find_element(x,i,len(x),compare)
        if loc!= : x[loc],x[i] = x[i],x[loc]



def find_element(x,left,right,compare):
    curr,val = left,x[left]
    for i in range(left,right):
        if compare(x[curr],x[i]): curr,val = i,x[i]
    return curr


#Insertion sort 

def insertionsort(a): #Non-Mutating (using another list/array for new sorted array)
    if a==[] : return []
    b = [a.pop()]
    while a != []:
        i = 0
        while i < len(b) and b[i]<a[-1]:
            i+= 1
        b.insert(i,a.pop())
        print(a,b)
    return b

def insertionsort_NM(a): #mutating
    for i in range(1,len(a)):
        k = a[i]
        j = i=1
        while j>= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = k
        print(a)
    return a

def insertionsortsir(a):
    nop = len(a)        #nop- number of passes
    while nop > 0:
        print(a)
        curr = a.pop()
        i = 0
        while i <= (len(a) - nop) and a[i] < curr : i += 1
        a.insert(i,curr)
        nop -= 1


