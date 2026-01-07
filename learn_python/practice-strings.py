name = "Ana Maria"

print(name[0])
print(name[len(name) - 1])
print("Lenght name = {}".format(len(name)))
print(f"Lenght name = {len(name)}")

print()

words = ['Hello', 'World']
print(" ".join(words))

print()

text = "Python Programming"
print(text[0:7])
print(text[len(text) - 6:len(text)])
print(text[0:len(text):2])
print(text[-1:-len(text)-1:-1])

print()

text = " i love python programming "
print(text.strip()) 
print(text.title())     
print(text.count("o"))

print()

text = "123abc"
print(text.isalnum())

print()

name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

print()

sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"))
print(sentence.find("Python"))
print(sentence.upper())

print()

text = input("Please give a text to count the vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
print(f"The number of vowels in the text is: {count}")

text = input("Please give a text to check if it is palindrom: ")
text_reversed = text[::-1].lower()
if text.lower() == text_reversed:
    print(f"The text={text} is palindrom")
else:
    print(f"The text={text} is not a palindrom")
