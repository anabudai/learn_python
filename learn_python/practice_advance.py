import time
from functools import reduce

def decorator_before_function_call(func):
    def wrapper():
        print("Before function is called")
        func()
    return wrapper

@decorator_before_function_call
def say_hello():
    print("Hello")

say_hello()

print()

def decorator_duration(func):
    def wrapper():
        start_ns = time.time_ns()
        func()
        end_ns = time.time_ns()
        return end_ns - start_ns
    return wrapper

@decorator_duration
def sum_up():
    total = 0
    for i in range(1, 1000001):
        total +=i
    return total

duration_ns = sum_up()
print(f"Function execution duration in ns={duration_ns}")

print()

class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary;

    @salary.setter
    def salary(self, value):
        if value <= 0:
            self._salary = 0
        else:
            self._salary = value

an_employee = Employee(8)
an_employee.salary = 49
print(f"Employee salary={an_employee.salary}")
an_employee.salary = -7
print(f"Employee salary={an_employee.salary}")

print()

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operations")
    
print(MathUtils.add(4, 8))
print(MathUtils.description())

print()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title by Author. Title={self.title}, author={self.author}"
    
    def __len__(self):
        return len(self.title)
    
a_book = Book("Bed Time Story", "Gigel")
print(str(a_book))
print(f"Length = {len(a_book)}")

print()

class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# try:
#     input_number = int(input("Insert a number:\n"))
#     if input_number < 0:
#         raise NegativeNumberError(f"Number needs to be positive, but {input_number} is not")
# except ValueError as e:
#     print(f"Please insert a valid positive number. Error={e}")
# except NegativeNumberError as e:
#     print(f"{e}")
# else:
#     print("Thank you")

print()

input_numbers = [1, 2, 3, 4, 5]

def cube(x):
    return x * x * x

result = list(map(cube, input_numbers))
print(f"Cuber for {input_numbers} are: {result}")

print()

input_numbers = [10, 11, 12, 13, 14]
def is_even(n):
    return n % 2 == 0

result = list(filter(is_even, input_numbers))
print(f"Even numbers from: {input_numbers} are: {result}")

print()

def product(m, n):
    return m * n

input_numbers = [1, 2, 3, 4]
result = reduce(product, input_numbers)
print(f"Product={result}")

# while (text := input("Insert text=\n") ) != 'quit':
#     print(text)

texts = ["python", "roks", "ai"]
lengths_bigger_than_4 = [l for x in texts if (l:=len(x)) > 4]
print(f"Lengths bigger than 4: {lengths_bigger_than_4}")

print()

