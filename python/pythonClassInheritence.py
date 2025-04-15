class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("i am an animal")
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def who_am_i(self):
        print(" i am a dog")

myDog = Dog()

myDog.who_am_i()
myDog.eat()