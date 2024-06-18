while True:
    def tri (k):
        n = 1
        for i in range(1,k+1):
            for j in range(i):
                print(n,end=" ")
                n+=1
            print()
    tri (int(input("Enter Number of rows : ")))