def spy_game(l):
    c = [0,0,7,'x']
    for n in l :
        if n == c[0]:
            c.pop(0)
    return len(c)==1
print(spy_game([1,0,2,4,0,5,7]))