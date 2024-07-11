class Circle():
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        self.circumferenceofcircle = radius*Circle.pi**2
    def area_of_circle(self):
        return(self.radius**2*self.pi)
my_circle = Circle(5)
print(my_circle.circumferenceofcircle)
