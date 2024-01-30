print("Welcome to python security generator !\n")
import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
           'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+','_','=','<','>',
           ',','.','/','?','|',';',':','[',']','{','}']
numbers = ['0','1','2','3','4','5','6','7','8','9']
n_letters = int(input("How many letters do you like in your password : "))
print("\n")
n_symbols = int(input("How many symbols would you like in your password : "))
print("\n")
n_numbers= int(input("How many numbers would you like in your password :"))
print("\n")

password = []
for some in range(1,n_letters+1) :
    password.append( random.choice(letters))
for some in range(1,n_symbols+1) :
    password.append( random.choice(symbols))
for some in range(1,n_numbers+1) :
    password.append( random.choice(numbers))
    
random.shuffle(password)

password_2 = ""
for some in password :
    password_2 +=some
print(f"Your password is : {password_2}")
print("\n")
print("We wish you a safe account.")




