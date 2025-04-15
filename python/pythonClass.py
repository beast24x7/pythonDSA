mylist = [1,2,4]
mySet = set()


class Dog():
    #class object attribute is going 
    # to be same for any instance of the class
    species = 'mammal'

    #called when we create instance of the class
    #constructor for a class
    #self is the instance of class itself
    def __init__(self,breed,name,spot):
        self.breed = breed
        self.name = name
        self.spot = spot
    # OPERATION /ACTIONS -----> METHODS

    def bark(self, number):
        print("WOOF!!! {} {}".format(self.name,number))

myDog = Dog(breed="lab",name="Sammy",spot=False)

myDog.bark(number=10)


class Circle():
    pi = 3.142
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle_object = Circle(10)
print(my_circle_object.get_circumference())
print(my_circle_object.area)