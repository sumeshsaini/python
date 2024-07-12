import ast
class Line():
    def __init__(self,cor1,cor2):
        self.cor1 = cor1
        self.cor2 = cor2
    def distance(self):
        x1,y1 = self.cor1
        x2,y2 = self.cor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.cor1
        x2,y2 = self.cor2
        return (y2-y1)/(x2-x1)
user_input = input("Enter X1 and Y1 : ")
user_input2 = input("Enter X2 and Y2 : ")
tup_input= ast.literal_eval(user_input)
tup_input2=ast.literal_eval(user_input2)
l = Line(tup_input,tup_input2)
print(l.distance())