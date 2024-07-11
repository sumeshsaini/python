class Animal():
    def __init__(self):
        print("Animal Created!")
    def who_am_i(self):
        print("I am a animal!!")
    def eat(self):
        print("I am Eating!!")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def who_am_i(self):
        print("I am a Dog!!")
my_dog = Dog()
my_dog.who_am_i()