import random 
score = 0
logo = """             
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/"""
data = [
    {"Name": "Ronaldo",
     "Followers": 256,
     "Social Source": "Football player"
    },
    {"Name": "Instagram",
     "Followers": 431,
     "Social Source": "Social media platform"
    },
    {
        "Name": "Vin Diesel",
        "Followers": 278,
        "Social Source": "Actor"
    },
    {
        "Name": "Barack Obama",
        "Followers": 392,
        "Social Source": "Politician"
    },
    {
        "Name": "YouTube",
        "Followers": 546,
        "Social Source": "Video-sharing platform"
    },
    {
        "Name": "Taylor Swift",
        "Followers": 623,
        "Social Source": "Musician"
    },
    {
        "Name": "Elon Musk",
        "Followers": 729,
        "Social Source": "Entrepreneur"
    },
    {
        "Name": "Beyoncé",
        "Followers": 874,
        "Social Source": "Musician"
    },
    {
        "Name": "Cristiano Ronaldo",
        "Followers": 782,
        "Social Source": "Football player"
    },
    {
        "Name": "Ellen DeGeneres",
        "Followers": 698,
        "Social Source": "TV host"
    },
    {
        "Name": "Katy Perry",
        "Followers": 571,
        "Social Source": "Musician"
    },
    {
        "Name": "Bill Gates",
        "Followers": 362,
        "Social Source": "Entrepreneur"
    },
    {
        "Name": "Neymar",
        "Followers": 487,
        "Social Source": "Football player"
    },
    {
        "Name": "Selena Gomez",
        "Followers": 512,
        "Social Source": "Musician"
    },
    {
        "Name": "Oprah Winfrey",
        "Followers": 599,
        "Social Source": "TV host"
    },
    {
        "Name": "Stephen Hawking",
        "Followers": 378,
        "Social Source": "Scientist"
    },
    {
        "Name": "Emma Watson",
        "Followers": 444,
        "Social Source": "Actor"
    },
    {
        "Name": "Serena Williams",
        "Followers": 451,
        "Social Source": "Tennis player"
    },
    {
        "Name": "Leonardo DiCaprio",
        "Followers": 497,
        "Social Source": "Actor"
    },
    {
        "Name": "Ariana Grande",
        "Followers": 506,
        "Social Source": "Musician"
    },
    {
        "Name": "Virat Kohli",
        "Followers": 469,
        "Social Source": "Cricket player"
    },
    {
        "Name": "David Beckham",
        "Followers": 495,
        "Social Source": "Football player"
    },
    {
        "Name": "Chris Hemsworth",
        "Followers": 421,
        "Social Source": "Actor"
    },
    {
        "Name": "Angelina Jolie",
        "Followers": 498,
        "Social Source": "Actor"
    },
    {
        "Name": "Roger Federer",
        "Followers": 498,
        "Social Source": "Tennis player"
    },
    {
        "Name": "Michelle Obama",
        "Followers": 376,
        "Social Source": "Politician"
    },
    {
        "Name": "Tom Hanks",
        "Followers": 379,
        "Social Source": "Actor"
    },
    {
        "Name": "Sunny Leone",
        "Followers": 353,
        "Social Source": "Actor"
    },
    {
        "Name": "Mia Khalifa",
        "Followers": 348,
        "Social Source": "Adult actress"
    },
    {
        "Name": "Johnny Sins",
        "Followers": 325,
        "Social Source": "Adult actor"
    }
]
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
def format_account(account):
    """Format the account data into printable format"""
    account_name = account["Name"]
    account_Followers = account["Followers"]
    account_source = account["Social Source"]
    return f"{account_name} {account_Followers} {account_source}"
def check_ans(ans,a_follower,b_follower):
    """Take the user guess and followers  counts and returns  if they got it right """
    if a_follower>b_follower:
        return ans =="a"
    else :
        return ans == "b"

print(f"Compare A :  {format_account(account_a)}")
print(logo)
print(f"Compare B :  {format_account(account_b)}")
ans = input("Who has more followers (A/B) : ").upper()
a_follower = account_a["Followers"]
b_follower = account_b["Followers"]
is_correct = check_ans(ans,a_follower,b_follower)
if is_correct:
    score+=1
    print(f"You are right your score is {score}")
else :
    print(f"Sorry thats wrong , Final score is {score}")
