def checkpas(pas):
    if len(pas)<8 or len(pas)>32:
        return f"{pas} is invalid password"
    if not pas[0].isalpha():
        return f"{pas} is invalid password"
    c = "/\\='\""
    for check in pas:
        if check in c:
            return f"{pas} is invalid password"
    else:
         return f"{pas} is valid"
pas=input("Enter Password : ")
print(checkpas(pas))