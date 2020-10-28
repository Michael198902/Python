class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!!"

class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meaw!!"
## FACTORY METHOD ##  
def get_pet(pet = " "):
    pets = dict(dog = Dog("Hope"), cat = Cat("Light"))
    return pets[pet]

d = get_pet("dog")
print(d.speak(),d._name) 

c = get_pet("cat")
print(c.speak(), c._name)