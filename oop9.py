class Cylinder():
    pi = 3.141592653589793238462643383279502884197
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
    def volume(self):
        return Cylinder.pi*(self.radius)**2 *self.height
    def area(self):
        return 2*Cylinder.pi*self.radius*(self.radius+self.height)
u_height = float(input("Enter the height : "))
u_radius = float(input("Enter the radius : "))
calculate = Cylinder(u_height,u_radius)
print(calculate.volume())