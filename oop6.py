class Dog():
    def __init__(self,name):
        self.name = name
    def speaks(self):
        print(f"{self.name} says woof!!")
class Cat():
    def __init__(self,name):
        self.name = name
    def speaks(self):
        print(f"{self.name} says Meow!!")
Fin = Dog("Fin")
Niko = Cat("Niko")
Fin.speaks()
Niko.speaks()

for pet in [Fin,Niko]:
    print(type(pet))
    pet.speaks()
class Animal():
    def __init__(self,name):
        self.name = name
    def speaks(self):
        raise NotImplementedError("Subclass must implement this abstract method")
myanimal = Animal(Fin)
myanimal.speaks()