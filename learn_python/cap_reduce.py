from functools import reduce

input = [1, 2, 3, 4, 5]

def sum(a, b):
    return a + b

result = reduce(sum, input)
print(result)

