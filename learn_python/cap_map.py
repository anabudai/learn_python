numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = list(map(square, numbers))
print(result)