def name (fname,lname) :
    if fname =="" or lname =="":
        return f"Invalid input."
    n = fname.title()
    p = lname.title()
    return(f"{n} {p}")
f = input("Enter first name : ")
l = input("Enter Second name : ")
print(name(f,l))