
#Merge Sort
#only indexed data types


def merge(a,b):                                 #Merge Function
    c=[]
    a.reverse()     #works better for pop and tail comparison
    b.reverse()     #works better for pop and tail comparison
    while a != [] and b!= []:
        if a[-1] < b[-1] : c.append(a.pop())
        else: c.append(b.pop())
    if a!= c : c.extend(b)
    else: c.extend(a)
    print(c)


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


        #Actual Merge Sort

def mergesort(a):
    if len(a) <= 1 : return a
    else:
        return merge(mergesort(a[:len(a)//2]),mergesort(a[len(a)//2:]))


        #To measure the time taken by the alogrithm

def 
