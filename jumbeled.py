import random 
art = """       _                 _     _          _ 
      | |               | |   | |        | |
      | |_   _ _ __ ___ | |__ | | ___  __| |
  _   | | | | | '_ ` _ \| '_ \| |/ _ \/ _` |
 | |__| | |_| | | | | | | |_) | |  __/ (_| |
  \____/ \__,_|_| |_| |_|_.__/|_|\___|\__,_|"""
words=["water","computer","AI","mobile","game","laptop","lamp","pokemon","cook","facebook","stock","cry","die","surfaceweb",
       "deepweb","fang","DYPSST","DPU","Cricket","tabel","man","women","men","child","mountain","actor","master","shoe",
       "word","random","letter","return","print","list","join","shuffle","import","clean","eat","food"]


def choose_word():
    # Choose a random word from the list
    return random.choice(words)

def jumble_word(word):
    # Shuffle the characters of the word
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled
print(f"{art}\n")
player1 = input("Enter your name : ")
player2 = input("Enter your name : ")
player1_score = 0
player2_score = 0
number_of_rounds = int(input("Enter number of rounds : "))

def player_1_play():
    global player1_score
    print(f"{player1} 's turn")
    for i in range(number_of_rounds):
        selected=choose_word()
        unarranged_word= jumble_word(selected)
        print(unarranged_word)
        guess = input("Enter your answer : ")
        if guess == selected:
            print("Correct")
            player1_score+=1
        else :
            print("Incorrect")
def player_2_play():
    global player2_score
    print(f"{player2} 's turn")
    for i in range(number_of_rounds):
        selected=choose_word()
        unarranged_word= jumble_word(selected)
        print(unarranged_word)
        guess = input("Enter your answer : ")
        if guess == selected:
            print("Correct")
            player2_score+=1
        else :
            print("Incorrect")
        
player_1_play()
player_2_play()
if player1_score > player2_score:
    print(f"{player1} wins with {player1_score-player2_score}")
elif player2_score>player1_score:
    print(f"{player2} wins with {player2_score-player1_score}")
else :
    print(f"{player1} and {player2} has equal score of {player2_score}")
