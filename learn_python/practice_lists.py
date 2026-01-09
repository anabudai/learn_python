fruits = ["apple", "banana", "cherry"]

print(fruits[0])
index_banana = fruits.index("banana")
fruits.remove("banana")
fruits.insert(index_banana, "orange")
print(fruits)
print(len(fruits))

print()

numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)
print(numbers[0:3])
print(numbers[len(numbers) - 3 : len(numbers)])

print()

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)

print()

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)

print()

coordinates = (10, 20)
print(coordinates)

a_list = list(coordinates)
a_list[0] = 50
a_tuple = tuple(a_list)
print(a_tuple)

print()
a_set = {1, 2, 3, 3, 4}
print(a_set)
a_set.add(5)
print(a_set)
a_set.remove(2)
print(a_set)
print(4 in a_set)

print()
first_set = {1, 2, 3}
second_set = {3, 4, 5}
union_result = first_set.union(second_set)
print(union_result)
intersection_result = first_set.intersection(second_set)
print(intersection_result)
difference_result = first_set.difference(second_set)
print(difference_result)

print()

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student)
student["city"] = "Delhi"
print(student)

phones = {"ana": "0772927898", "maria": "078967676", "rob":"07865445"}
print(phones.keys())
print(phones.values())

print()

for name, phone in phones.items():
    print(f"{name}: {phone}")

print()

numbers = {3, 8, 20, 6, 2, 8, 78, 3, 44}
unique_numbers = set(numbers)
print(unique_numbers)

print()

products = {"chair": 45, "table": 150, "lamp": 30}

max_price = 0
max_product_name = ""
for product_name, price in products.items():
    if (price > max_price):
        max_price = price
        max_product_name = product_name

print(f"The product with the highest price is \"{max_product_name}\" with price {max_price}")


merged = {}
for key, value in products.items():
    merged[key] = value
for key, value in student.items():
    merged[key] = value
print(merged)