import os
number = int(input("Enter a number : "))
match number :
    case 0 :
        print("The number is zero.")
    case _ if number %2 == 0 :
        print(f"{number} is a even number")
    case _ if number %5 == 0 :
        print(f"{number} is divisible by 5")
    case _ :
        print(number)

