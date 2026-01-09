first = {"name": "Anamaria", "age": 25, "city": "Bucharest"}

print(first)
print(type(first))
print(first["city"])
first["city"] = "Cluj-Napoca"
print(first["city"])

print()

print(first.keys())
print(first.values())

print()

first.pop("age")
print(first)

result = first.get("name")
print(result)
print(first)

print()

second = {i:i*2 for i in range(10, 20)}
print(second)