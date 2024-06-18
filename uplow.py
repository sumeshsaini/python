def up_lows(st):
    d = {'upper':0,'lower':0}
    for k in st:
        if k.isupper():
            d['upper']+=1
        elif k.islower():
            d['lower']+=1
    return f"Original String : {st}\nNo. of upper case : {d['upper']}\nNo. of lower case : {d['lower']}"
print(up_lows("Hello Mr. Rogers, how are you this fine Tuesday?"))