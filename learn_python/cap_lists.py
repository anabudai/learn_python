names = ["Ana", "Beto", "Carlos", "Diana", "Eva"]

print(names)

names.append("Fernando")
print(names)

names.insert(2, "Gabriela")
print(names)

names.remove("Carlos")
print(names)

names.pop()
print(names)

names.pop(1)
print(names)

names.sort()
print(names)    

names.reverse()
print(names)    

count = names.count("Ana")
print(count)

names.extend(["Hugo", "Irene"])
print(names)

index = names.index("Diana")
print(index)

