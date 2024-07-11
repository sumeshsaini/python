class Dog():
    #class object attribute
    species = 'Mammal'
    #user defined attributes
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
    #Operation/Action------>Method------>A method is nothing but a function within a class
    def bark(self):
        print(f"Woof!! my name is {self.name}")
my_dog = Dog("Lab","Max",False)
my_dog.bark()
