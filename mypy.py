import random
import time 
import os
logo = '''
⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣼⣿⣀⣹⣿⡆⠀⢤⡄⢤⣄⢤⡤⠀⢤⣤⣤⣤⣤⢤⣄⠀⢤⣤⡤⣤⣤⣤⢠⡄⠀⣤⢤⡤⢤⡠⣤⠤⣴⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢹⣿⡇⠉⠉⢿⣿⡄⢸⡇⠀⢹⡏⢿⣠⡟⢹⣿⠤⠄⢸⡿⣷⣼⡇⠀⣿⡇⠀⢸⡇⠀⡇⢸⡇⣎⠀⣿⠶⠌⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠾⠿⠀⠀⠀⠘⠿⠿⠾⠿⠴⠛⠁⠘⠏⠀⠼⠿⠦⠖⠸⠃⠀⠙⠇⠀⠿⠇⠀⠘⠷⠚⠇⠾⠇⠘⠿⠿⠶⠶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢠⣤⡤⠀⢲⣶⣶⡄⠀⠀⠀⣰⣶⣶⠖⠀⢲⣶⣶⠶⠶⢶⣶⠀⠀⠀⠀
⢀⣀⠀⠀⠀⠀⠀⢀⣸⣿⣉⣀⠀⢟⡉⠉⡉⣿⣿⢉⣉⣙⣛⣘⣿⣇⣀⡀⣿⢿⣿⡄⠀⣼⡿⣿⣿⢠⣤⣬⣭⣭⣤⣤⣤⣬⣤⣤⣀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠰⠻⣿⣾⡿⠵⣿⣿⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⣍⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢰⣶⡆⠀⣼⣿⡆⠀⠹⡿⠁⠀⣿⣿⡀⠀⣸⣿⣿⣤⣤⣤⣤⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠀⠀⠀⠀⠀⠴⠟⠛⠂⠀⠀⠀⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠻⠋⠀⠀⠀⠀
'''
print(logo)
print("\n")
print("Welcome to the paradise!\n")
user_name = input("Enter Your Name : ")
print(f"{user_name} We hope you make it well!")
time = time.strftime("%I:%M:%S")
print(f"\n{user_name} your entry time is {time} keep  it in mind")
type = ["Easy", "Medium","Hard","Impossible"]
user_type = input("Select your mode 'Easy,Hard,Medium,Impossible' : ").capitalize()
print("\n")
if user_type == "Easy" :
    print(f"So you selected {user_type} intresting.")
elif user_type == "Hard" :
    print(f"So you selected {user_type} lets see what are you made up off")
elif user_type == "Medium" :
    print(f"So you selected {user_type} lets see what can you do")
elif user_type == "Impossible" :
    print(f"\nSo you selected {user_type} we will try our best")
else :
    print(f"{user_type} is not valid,select from given data only.")
print("\n\nThe forward route is not safe to travel alone so we hired you a partner.")
partner = ["Andrew","Angel","Viduit","Max","Joe","Kristi","Alex"]
your_partner = random.choice(partner)
check_partner = your_partner
print(f"\nSo your journey partner is {your_partner} hope you make a good team.")
def your_call (check_partner) :
    print(f"These are your partner details ▽\n",team[check_partner])

your_team = input("Do you want to know the strength and weakness of your friend yes or no :").capitalize()
team = {
    "Andrew" : "Strength->Super strength and,Viduit \nno weakness",
    "Angel"  : "Strength->Super IQ ,Viduit\n weakness -> Driving,cake,lycs",
    "Viduit" : "Strength->Superhuman strength,IQ,Driving Skills,Cooking,Andre\n Weakness-> None",
    "Max"    : "Strength->Street fighter,Army of dogs,Alex\nWeakness-> Cat hair,aiming,Iq",
    "Joe"    : "Strength->Jam,Acting,Manipulation,Kristi\nWeakness->Maths,Brain",
    "Kristi" : "Strength->Looks,Dance,Talking,Eye contact,Ridding,Joe\nWeaknes-> Red wine,Strength",
    "Alex"   : "Strength->Coding,Hacker,Chameleon behavior,IQ,Max\nWeakness->Fighting"
}
if your_team == 'Yes' :
    your_call(your_partner)
else :
    print("That's strange!")
