def greet(name) :
    print(f"Hello {name}")
    
    age = int(input("What is your age : "))
    if age >= 18 :
        print(f"Mr . {name} you can drive.")
    else :
        print(f"Mr. {name} you cant drive.")
    
greet(input("Enter your name : "))