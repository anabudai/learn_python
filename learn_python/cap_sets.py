first_set = {1, 2, 3, 5, 3, 3, 2}
second_set = {4, 5, 6}

print(first_set)

print(type(first_set))

first_set.add(4)
print(first_set)

first_set.remove(2)
print(first_set)    

# first_set.remove(10)  # This will raise a KeyError if 10 is not in the set
# print(first_set)

first_set.discard(10)  # This will not raise an error if 10 is not in the set
print(first_set)

print()

result = first_set.intersection(second_set)
print(first_set)
print(second_set)
print(result)

print()

result = first_set.union(second_set)
print(first_set)
print(second_set)
print(result)