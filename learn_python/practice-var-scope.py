counter = 0

def increment():
    global counter
    counter +=1

print(counter)
increment()
print(counter)
increment()
print(counter)
increment()
print(counter)

print()

def multiply(a, b):
    '''
    Return the result of multiplying a and b.
    
    :param a: first parameter
    :param b: second parameter
    '''
    return a * b


def help():
    print(multiply.__doc__)

help()