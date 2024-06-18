odd = []
even = []

while True:
    n = int(input("Enter a number: "))
    if n % 2 != 0:
        odd.append(n)
    elif n % 2 == 0:
        even.append(n)
    if input("Are there any more numbers (yes/no): ") == 'no':
        break

print("These are the odd numbers:", ', '.join(map(str, odd)))
print("These are the even numbers:", ', '.join(map(str, even)))