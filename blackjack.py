import random
your_name = input("Enter your name : ")
def b_card () :
    """Selects a random card from the deck of cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
user_card = []
computer_card = []
for _ in range(2):
    user_card.append(b_card)
    computer_card.append(b_card)
