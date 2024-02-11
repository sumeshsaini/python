print("Welcome to the rollercoaster.")
height =int(input("Enter your height : "))
bill = 0
if height >=120 :
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age : "))
    if age<12 :
        bill = 140
        print("Childs ticket 140.")
    elif age<=18 :
        bill = 170
        print("Youth ticket 170.")
    else :
        bill = 200
        print("Adult ticket 200.")
    pic = input("Do you want pictures type yes or no. ")
    if pic =="yes":
        bill+=30
        print(f"Your final bill is {bill}")
    elif pic== "no":
        print(f"Your bill is {bill}")
else :
    print("You cannot ride the rollercoaster.")
