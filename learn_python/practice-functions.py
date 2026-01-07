import math
import my_utils

def greet():
    return "Hello, Python Learner!"

def square(num):
    return num * num

def full_name(first, last):
    return f"{first} {last}"

def calculate_aria(length, width=10):
    return length * width

print(greet())
      
print()

print(square(0))
print(square(1))
print(square(3))

print()

print(full_name("Ana", "Budai"))

print(calculate_aria(6))
print(calculate_aria(6, 4))

print()

print(math.sqrt(144))
print(math.sin(math.radians(90)))

print(my_utils.is_even(4))
print(my_utils.is_even(41))
print(my_utils.is_even(40))
print(my_utils.is_even(0))