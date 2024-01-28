import random

names = input("Enter names : ")
values = names.split()
people = len(values)
rc = random.randint(0,people - 1)
pay = values[rc]
print(f"{pay} is going to pay for the bill!")