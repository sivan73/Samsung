class Student:
    def __init__(self, name: str, marks: float):
        self.__name = name
        self.__marks = 0
        self.set_marks(marks)
    def set_marks(self, marks: float):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Marks must be between 0 and 100.")
    def get_marks(self) -> float:
        return self.__marks
    def __str__(self) -> str:
        return f"Student(Name={self.__name}, Marks={self.__marks})"
student1 = Student("David", 85)
student2 = Student("John", 92)
print(student1)
print(student2)
print()
print("After updating marks:")
student1.set_marks(95)
print(student1)
print()
student1.set_marks(105)
print(f"Current Marks: {student1.get_marks()}")


class Employee:
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = 0.0
        self.set_salary(salary)
    def set_salary(self, salary: float):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than zero.")
    def get_salary(self) -> float:
        return self.__salary
    def __str__(self) -> str:
        return f"Employee(Name={self.__name}, Salary={self.__salary})"
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 65000)
print(emp1)
print(emp2)
print()
print("After salary increment:")
emp1.set_salary(55000)
print(emp1)
print()
emp1.set_salary(-1000)  
print(f"Current Salary: {emp1.get_salary()}")


class Car:
    def __init__(self, brand: str, speed: float):
        self.__brand = brand
        self.__speed = 0.0
        self.set_speed(speed)

    def set_speed(self, speed: float):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative.")
    def get_speed(self) -> float:
        return self.__speed
    def __str__(self) -> str:
        return f"Car(Brand={self.__brand}, Speed={self.__speed} km/h)"

car1 = Car("Toyota", 80)
car2 = Car("Honda", 100)
print(car1)
print(car2)
print()
print("After speed update:")
car1.set_speed(120)
print(car1)
print()
car1.set_speed(-20)  
print(f"Current Speed: {car1.get_speed()} km/h")



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
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def main():
    n = int(input("Enter number of employees: "))
    s = []
    print(f"Enter {n} salaries:")
    while len(s) < n:
        line = input().split()
        for v in line:
            if len(s) < n:
                s.append(int(v))

    print("\nOriginal Salaries:")
    print(" ".join(map(str, s)))
    merge_sort(s)
    print("\nSorted Salaries:")
    for x in s:
        print(x)
    lo = s[0]
    hi = s[-1]
    r = hi - lo
    print(f"\nLowest Salary : {lo}")
    print(f"Highest Salary: {hi}")
    print(f"\nSalary Range  : {r}")
if __name__ == "__main__":
    main()



def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
    
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    n = int(input("Enter number of ticket prices: "))
    p = []
    print(f"Enter {n} ticket prices:")
    while len(p) < n:
        line = input().split()
        for v in line:
            if len(p) < n:
                p.append(int(v))
                
    print("\nOriginal Ticket Prices:")
    print(" ".join(map(str, p)))
    quick_sort(p, 0, len(p) - 1)
    
    print("\nSorted Ticket Prices:")
    for x in p:
        print(x)
    low_val = p[0]
    high_val = p[-1]
    
    print(f"\nCheapest Ticket: {low_val}")
    print(f"Costliest Ticket: {high_val}")

if __name__ == "__main__":
    main()
