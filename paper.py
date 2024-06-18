def paper_doll(text):
    r = 0
    l = []
    for i in text:
        k=(text[r]*3)
        l.append(k)
        r+=1
    print(*l,sep='')   
t = input("Enter : ")
paper_doll(t)
#method 2
r = ''
for char in t:
    r+=char*3
print(r)