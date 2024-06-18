def generate_pins_with_zero():
    pins_with_zero = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                pin = str(i) + str(j) + str(k)
                if '0' in pin:
                    pins_with_zero.append(pin)
    return pins_with_zero

pins_with_zero = generate_pins_with_zero()
print(pins_with_zero)
print("Total number of 3-digit PINs containing zero:", len(pins_with_zero))
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

print(art)
player_1 = input("Player 1 name : ")
player_2 = input("Player 2 name : ")
player_1_score = 0
player_2_score = 0
number_of_rpunds = int(input("Enter Number of rounds : "))

def select_word():
    selected_word =random.choice(words)
    return selected_word
def shuffle():
    jumbled = "".join(random.sample())
def shuffle(word):
    """Used to shuffle letters"""
    letter = list(word)
    random.shuffle(letter)
    idk = ''.join(letter)
    return idk