import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissors_sign = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper_sign = """
    _______
---'   ____
      /    /
     /    /
    /    /
---/____/
"""
game_images = [rock, scissors_sign, paper_sign]

while True:
  use = int(input("Enter 0 for rock, 1 for scissors, 2 for paper : "))
  if use >= 3 or use < 0 :
    exit("You entered an invalid number , you lose")

  if use <=2  :
    print("You chose : ")
    print(game_images[use])
  computer = random.randint(0,2)
  print("Computer chose :")
  print(game_images[computer])
  if use == 0 and computer == 2 :
    print("You Lose")
  elif use == 2 and computer == 0 :
    print("You Win")
  elif use == 0 and computer == 1 :
    print("You Won")
  elif use == 1 and computer == 2 :
    print(" You won")
  elif use == 2 and computer == 1:
    print("You Lose")
  elif use == computer :
    print("It is a draw")
  elif use == 1 and computer == 0 :
    print("You Lose")
