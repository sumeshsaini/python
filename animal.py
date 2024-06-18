def cracker(word):
    n_word=word.lower().split()
    fw = n_word[0][0]
    sw = n_word[1][0]
    if fw == sw :
        return True
    else:
        return False
print(cracker("Hi  HBro"))