import time
exact = time.strftime('%I : %M :%S')
print(f"Time at your location is {exact}\n")
Hour = int(time.strftime('%H'))
print(f"Hour in your location is {Hour}\n")
min = int(time.strftime('%M'))
print(f"Miniutes in your location is {min}\n")
sec = int(time.strftime('%S'))
print(f"Seconds in your location is {sec}")
if Hour>= 5 and Hour <=12 :
    print("Good Morning")
elif Hour>=13 and Hour<=18 :
    print("Good Afternoon")
else :
    print("Good Night")



