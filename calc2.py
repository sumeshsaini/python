logo = """
 _____________________
|  _________________  |
| |                   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1,n2):
        return n1+n2
def sub(n1,n2):
        return n1-n2
def multi(n1,n2):
        return n1*n2
def div(n1,n2):
        return n1/n2
operator = {
        '+' : add,
        '-' : sub,
        '*' : multi,
        '/' : div
    }
def calculator():
    """ It will apply recursion"""
    print(logo)
    num1= float(input("Enter first number : "))
    for i in operator :
        print(i)
    to_continue = True
    while to_continue:
        symbol = input("Select an operator : ")
        num2= float(input("Enter Second number : "))
        if symbol == '+' or symbol== '-' or symbol == '*' or symbol =='/':
            output=(operator[symbol](num1,num2))
            print(f"{num1} {symbol} {num2} = {output}")
        if input("press y to continue or c to reset :  ").lower() == 'y':
            num1 = output
        else :
            to_continue =False
            calculator()
calculator()