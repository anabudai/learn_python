class Car:
    def drive(self):
        print("Car is moving")

a_car = Car()
a_car.drive()

print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a_person = Person("Ana", 7)
print(a_person.age)
print(a_person.name) 

print()

class Animal:
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self):
        print("bark")

an_animal = Animal()
print(an_animal.sound())
a_dog = Dog()
print(a_dog.sound())