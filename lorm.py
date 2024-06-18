def less_more(a,b):
    if a%2==0 and b %2 == 0:
        if a>b:
            return b 
        else :
            return a
    l = [a,b]
    for i in l:
        if i%2!=0:
            if a>b:
                return a 
            else :
                return b
a = int(input("Enter: "))
b = int(input("Enter: "))
print(less_more(a,b))