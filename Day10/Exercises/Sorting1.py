Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
...             arr[k] = L[i]
...             i += 1
...         else:
...             arr[k] = R[j]
...             j += 1
...         k += 1
...     while i < len(L):
...         arr[k] = L[i]
...         i += 1
...         k += 1
...     while j < len(R):
...         arr[k] = R[j]
...         j += 1
...         k += 1
... 
...     
>>> def sortingfun():
...     n = int(input("Enter number of employees: "))
...     s = []
...     print(f"Enter {n} salaries:")
...     while len(s) < n:
...         line = input().split()
...         for v in line:
...             if len(s) < n:
...                 s.append(int(v))
... 
...     print("\nOriginal Salaries:")
...     print(" ".join(map(str, s)))
...     merge_sort(s)
...     print("\nSorted Salaries:")
...     for x in s:
...         print(x)
...     lo = s[0]
...     hi = s[-1]
...     r = hi - lo
...     print(f"\nLowest Salary : {lo}")
...     print(f"Highest Salary: {hi}")
...     print(f"\nSalary Range  : {r}")
... 
...     
>>> sortingfun()
Enter number of employees: 3
Enter 3 salaries:
123000
334505
430000

Original Salaries:
123000 334505 430000

Sorted Salaries:
123000
334505
430000

Lowest Salary : 123000
Highest Salary: 430000

Salary Range  : 307000
