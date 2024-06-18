def tri(height,base):
    area = (base*height)/2
    print(f"The area of triangle is {area}")
def rect(length,width):
    area = width*length
    print(f"The area of the rect is {area}")
def sq(side):
    Area = side**2
    print(f"The area of the square is {Area}")
def circ(radius):
    import math
    area_2 = math.pi * (radius**2)
    print(area_2)
while True:
    print("Select a shape ")
    print("Press 1 for triangle")
    print("Press 2 for rect")
    print("Press 3 for sq")
    print("Press 4 for circ")
    user_call=int(input(("Enter : ")))
    if user_call==1:
        height = float(input("Enter the height : "))
        base = float(input("Enter the base : "))
        tri(height,base)
    elif user_call==2:
        length = float(input("Enter the length : "))
        width = float(input("Enter the width : "))
        rect(length,width)
    elif user_call==3:
        side = float(input("Enter the side : "))
        sq(side)
    elif user_call==4:
        radius = float(input("Enter the radius : "))
        circ(radius)
    else:
        print("Invalid")



    