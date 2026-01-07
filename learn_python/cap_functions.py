def average(a, b, c , d = 10):
    
    '''this returns the average of four numbers'''

    result = (a + b + c + d) / 4
    return result

print(average(10, 20, 30))
print(average.__doc__)