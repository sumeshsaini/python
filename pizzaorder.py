print("Thanks for Choosing Python Pizza delivery!")
pizz_size=input("Would you like a small,Medium,a Large pizza : ")
extra_cheese=input(" DO you want extra cheese Yes or No : ")
bill =0
if pizz_size =="S":
 bill+=100
elif pizz_size =="M":
 bill+=150
else :
 bill+=200
if extra_cheese == "Yes":
 bill+=30
print(f"Your total bill is : {bill}.")
