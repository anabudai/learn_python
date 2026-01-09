class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def isRetirementAge(self):
        return self.age > 65
    
    @isRetirementAge.setter
    def isRetirementAge(self, new_age):
        if new_age > 65:
            self.age = 65
        else:
            self.age = new_age

a_person = Person("Ana", 67)
print(a_person.isRetirementAge)
a_person.isRetirementAge = 70
print(a_person.age)