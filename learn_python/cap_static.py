class Utils:
    name = "abc"

    def __init__(self, age):
        self.age = age
        name = "kkk"


    @staticmethod
    def sum(a, b):
        return a + b
    
    @classmethod
    def changeName(cls, new_name):
        cls.name = new_name
    
utils1 = Utils(3)
print(utils1.sum(4, 6))
print(utils1.age)

utils1.changeName("ana")
print(utils1.name)

print()

utils2 = Utils(4)
print(utils2.name)
print(utils2.age)