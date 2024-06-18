n = int(input("Enter number of rows : "))
m = int(input("Columns : "))
for i in range(n):
    for _ in range(m):
        print("*",end="")
    print()