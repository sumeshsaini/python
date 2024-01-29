print("Welcome to the hunt let the fun begain!")
side = str(input("Where do you want to go left or right or you are afraid : "))
if side =="left" :
    exit("You were killed by a ant!lol.")
elif side =="right" :
    print("Now you are at the river ")
else :
    print("So you are weak.")
option = str(input("Do you want to wait or jump in river? : "))
if option =="wait" : 
    print("Hope on the boat to the safe room.")
else :
    exit("Snakes said you taste so bad.")
room = str(input("Select a room 1,2,3 : "))
if room == "1":
    print("Angry man said get lost hence game over!")
elif room =="2" : 
    print("Mrbeast Gave you gold!You won the game!")
else :
    print("Mrbeast in another universe killed you game over!!!")
  