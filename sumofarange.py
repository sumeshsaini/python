num = int(input("Enter the first number : "))
num2 = int(input("Enter the last number : "))
num3 = num2+1
total = 0
for sum in range(num,num3) :
    total+=sum
print(f"The total sum of numbers starting from {num} to {num2} is {total}")