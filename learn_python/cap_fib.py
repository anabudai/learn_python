def fib(num):
    if (num == 0):
     return 0
    elif (num == 1):
     return 1
    else:
     return fib(num - 1) + fib(num - 2)
    
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
