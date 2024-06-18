def black_jack(a,b,c):
    d = (a+b+c)
    if d<=21:
        return d
    elif d>21 and a ==11 or b==11 or c == 11:
        return(d-10)
    elif d>21:
        return 'BUST'
print(black_jack(9,9,11))