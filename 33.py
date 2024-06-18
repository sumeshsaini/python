def find_33(k):
    for i in range(0,len(k)-1):
        if k[i] == 3 and k[i+1]==3:
            return True
    return False
print(find_33([1,2,3,4,3,4]))