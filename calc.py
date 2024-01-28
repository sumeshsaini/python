print("Welcome python calculator .\n")
num1= float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
operator = input("Enter the operator +,-,*,/,%,** : ")
if operator == '+' :
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")
elif operator == '-' :
    sub = num1 - num2
    print(f"The sub of {num1} and {num2} is {sub}")
elif operator == '*' :
    multi = num1 *num2
    print(f"The product of {num1} and {num2} is {multi}")
elif operator == '/' :
    divide = num1 / num2
    print(f"On dividing {num1} and {num2} we get {divide}")
elif operator == '%' :
    modulo = num1 % num2
    print(f"The modulus of {num1} and {num2} is {modulo}")
elif operator == '**' :
    power = num1 ** num2
    print(f"The exponent of {num1} with {num2} is {power}")
else :
    print(f"{operator} is not a valid operator.")