while True:
    n= int(input("Enter a number: "))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        print(f"{n} is an Armstrong number")
    elif n!= sum:
        print(f"{n} is not an Armstrong number")
    else :
        print(f"{n} is Invalid")