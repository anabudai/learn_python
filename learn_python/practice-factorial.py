def factorial(n):
    if (n <= 0):
        print(f"Factorial can only be calculated for positive integers. You provided: {n}")
        return None
    elif (n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
def sum_of_digits(n):
    if (n < 0):
        print(f"Sum of digits can only be calculated for non-negative integers. You provided: {n}")
        return None 
    elif (n <= 9):
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)
    

print(factorial(-2))
print(factorial(0))
print(factorial(1))
print(factorial(5)) 

print()

print(sum_of_digits(-15))
print(sum_of_digits(0))
print(sum_of_digits(7))
print(sum_of_digits(1234))

