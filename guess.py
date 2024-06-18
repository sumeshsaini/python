while True:
    import random
    asci = """ ___________                 ___ ___                  .___ 
\__    ___/______ ___.__.  /   |   \_____ _______  __| _/ 
  |    |  \_  __ <   |  | /    ~    \__  \\_  __ \/ __ |  
  |    |   |  | \/\___  | \    Y    // __ \|  | \/ /_/ |  
  |____|   |__|   / ____|  \___|_  /(____  /__|  \____ |  
                  \/             \/      \/           \/   """
    print(asci)
    print("Welcome to try hard!!")
    user_call=input("Select a Difficulity level (Hard/Easy) : ").capitalize()
    choice = 0
    if user_call == 'Hard':
        choice = 5
    elif user_call == 'Easy':
        choice = 10
    else:
        print("Invalid Entry!")
    print(f"You have {choice} chances to guess the correct number between 1 to 100")
    Given_number = random.randint(1,100)
    for i in range(1,choice+1,1):
        m = int(input("Enter The number you think off : "))
        if m == Given_number:
            print("Congratulation you won!")
            break
        elif m!=Given_number:
            if m>Given_number:
                print("Too High")
            else :
                print("Too Low")
            choice= choice-1
            print(f"You have {choice} turns remaining")
        elif choice == 0:
            print("You Lose")
        else:
            print("Invalid")

    if input("Do you want to play again (yes/no) : ") == 'no':
        break

    