import random

word_list = ["Pokemon","Mouse","Physics","Maths","Rich","Python",
            "Moon","Sun","Apple","Mango","Pen","Run","Return","Welcome","Happy","Night","Marvel","Radio","Hangman","Letter","Game","List","Brother","Mother","Father","Sister","Family","Netflix","Cricket","Football","Gym","TOP-G","Andrew Tate","Tristan Tate","Amazon","Alexa","Siri","Googlr","Youtube","Facebook","Instagram","Fang","Million","Programing","Typewriter","Wrong","Game Over","Winner","Rock","Jumanji","Bodmas","Ball","Samsung","Microsoft","Whatsapp"]
word = random.choice(word_list).lower()
print(f"The solution is {word}")
guess = input("Guess a letter : ").lower()
display = []
word_length = len(word)
for _ in range(word_length):
  display+= "_"
for position in range(word_length) :
  letter = word[position]
  if letter == guess :
    display[position] = letter
print(display)