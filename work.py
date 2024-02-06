ok = True
num_count=0
neg_count=0
while ok:
    n = int(input("Enter a number : "))
    if n>0:
        num_count=num_count+1
    elif n<0:
        neg_count=neg_count+1
    print(f"The positive number count is {num_count}")
    print(f"The negative number count is {neg_count}")
    nop = int(input("Do you still want to continue if no enter zero : "))
    if nop == 0:
        ok = False