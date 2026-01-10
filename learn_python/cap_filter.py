numbers = [1, 2, 3, 4, 5]

def greater_than_3(x):
    return x > 3

number_greater_than_n = filter(greater_than_3, numbers)

print(list(number_greater_than_n))