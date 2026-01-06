multiline_text = '''Ana are mere
si pere
si caise
'''

print(multiline_text)

text = "Flower"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print()

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])

text = "123456789"
print(text[0:3])
print(text[0:-2])
print(text[0:9:3])

print()

text = "my name is Ana"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(len(text))

print()

text = " \n my name is Ana  \n "
print(text.strip())
print(text.rstrip())
print(text.lstrip())

print()

text = "my name is Ana"
print(text.find("na"))
print(text.replace("Ana", "Maria"))