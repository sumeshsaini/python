# t3 = input("Enter : ")
# t1 = int(t3[0])
# t2 = int(t3[1])
# t4 = int(t3[2])
# t3 = t1 + t2 + t4
# print(t3)
# print(3*(3+(3/3)-3))
# print (type(4//3))
# score = 5
# height = 13.8
# w = True
# print(f"Your score is{score},your height is {height},and you are winning{w}")
# Which year do you want to check?
# year = int(input())
# #  Don't change the code above 

# # Write your code below this line 
# if year %4==0 :
#   if year%100!=0:
#     if year%400==0 :
#       print("Leap year")
# else :
#   print("Not leap year")
# ok = int(input("Enter : "))
# if ok>5 or ok<10 :
#     print("HI")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# numc = num1 * num2
# numa = num1 + num2
# if numc>=1000 :
#     print(f"The product of {num1} and {num2} is {numc}")
# else :
#     print(f"The sum of {num1} and {num2} is {numa}")
# import random 
 
# h = "how"
# p = "y"
# n = "no"
# word = [h,p,n]
# ok = int(input("Enter a numero 0,1,2 : "))
# comp = random.randint(0,2)
# if comp == 0 :
#     print(p)
# elif comp == 1:
#     print(n)
# else :
#     print(p)
# use = random.randint(0,2)
# print(word[use])
# name = "Sumesh Saini"
# print(name.find('i'))
# print("3>2")
# print(3>2)
# i = int(input("Enter starting number : "))
# k = int(input("Enter last number :"))
# while i<=k :
#     print(i*'*')
#     i+=1
# i = 5
# while i>=0 :
#     print(i * '*')
#     i-=1
# marks = ["99","98","100"]
# for score in marks :
#     print(score)
# print("Hey I am a \ " Good boy\" )
# nm = "Harry"
# print(nm[-4:-1])
# ok = "Sumesh"
# # # print(len(ok))
# # # m = ok.lower()
# # # n = ok.upper()
# # # print(f"{m} {n}")
# # print(ok.rstrip("h"))
# print(ok.replace("Sumesh","Saini"))
# for i in range(2,21,2) :
#     print(i)
# i = 5
# while (i>0) :
#     print("Wow "," ")
#     i+=1
# num = int(input("Enter a number : "))
# for i in range(11) :
#     print(f"{num} X {i} = {i*num}")
#     if i == 4:
#         print("Hi")
#         continue
# print(pow(2,2))
# def greet(name) :
#     print(f"Hello {name}")
    
#     age = int(input("What is your age : "))
#     if age >= 18 :
#         print(f"Mr . {name} you can drive.")
#     else :
#         print(f"Mr. {name} you cant drive.")
    
# greet(input("Enter your name : "))
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
#             , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet.index["d"])
# a = int(input("Enter"))
# b =int( input("Enter"))
# print(a+b)
# num1 = int(input("Enter a number : "))
# num2= int(input("Enter your last wanted digit"))
# for i in range(num1,num2+1,num1) :
#     print(i)
# z = int(input("Enter a numero : "))
# if z%2==0 :
#     for i in range(z,z) :
#         print(i)
# elif z%2!=0 :
#     for k in range(z,z):
#         print(k)
# x=int(input("Enter num :"))
# num = ["Hi","Bye"]
# print(num[0])
# print("XY")
# Xy = float(1)
# print(type(Xy))
# v = int(input("Enter a numer : "))
# c = int(input("Enter a numer : "))
# bc = v+c
# print(f"The sum of {v} and {c} is {bc}")
# OK = [
#     {
#         "show" : "TV",
#         "Watchedd" : ["Pokemon","UFC"],
#         "Daily_watch_time" : 7
#     },
#     {
#         "Country" : "INDIA",
#         "States" : ["Delhi","Mumbai"],
#         "Total_Number_of_staates" : 29
#     }
# ]
# print(OK)
# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
# print(order["main"][2][0])
# a = int(5)
# b = int(9)
# print(a/b)
# n = int(input())
# for i in range(n):
#     print(i*i)
# def add(n1, n2):
#   return n1 + n2
 
# def subtract(n1, n2):
#   return n1 - n2
 
# def multiply(n1, n2):
#   return n1 * n2
 
# def divide(n1, n2):
#   return n1 / n2
 
# print(add(2, multiply(5, divide(8, 4))))
# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)
#import random 
#print({0:"Back off",1:"Participate"}[random.randint(0,1)])

# x=-49
# print(max((0,min((x,50)))))
# an= int(input("Enter a number: "))
# sum = 0
# temp = an
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if an == sum:
#    print(an,"is an Armstrong number")
# else:
#    print(an,"is not an Armstrong number")
# from googletrans import Translator

# def translate_text(text, target_language):
#     translator = Translator()
#     translated_text = translator.translate(text, dest=target_language)
#     return translated_text.text

# if __name__ == "__main__":
#     text = input("Enter the text you want to translate: ")
#     target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

#     translated_text = translate_text(text, target_language)
#     print(f"Translated text: {translated_text}")
# ok=int(input("Enter : "))
# ok-5
# pass
# print(ok)
# ok = True
# num_count=0
# neg_count=0
# while ok:
#     n = int(input("Enter a number : "))
#     if n>0:
#         num_count=num_count+1
#     elif n<0:
#         neg_count=neg_count+1
#     print(f"The positive number count is {num_count}")
#     print(f"The negative number count is {neg_count}")
#     nop = int(input("Do you still want to continue if no enter zero : "))
#     if nop == 0:
#         ok = False
# def checkpas(pas):
#     if len(pas)<8 or len(pas)>32:
#         return f"{pas} is invalid password"
#     if not pas[0].isalpha():
#         return f"{pas} is invalid password"
#     c = "/\\='\""
#     for check in pas:
#         if check in c:
#             return f"{pas} is invalid password"
#     else:
#          return f"{pas} is valid"
# pas=input("Enter Password : ")
# print(checkpas(pas))
# __xyz__ = 5  
# print(__xyz__)
# x_y_z_p = 5,000,000  
# print(x_y_z_p)
# x = 1
# while True:
#     if x % 5 == 0:
#         break
#     print(x)
#     x+= 1
# print("javatpoint"[5:]) 
# print(r"\njavat\npoint")   
# a = 1
# while True:
#     if a % 7 == 0:
#         break
#     print(a)
#     a += 1
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(0)
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print(0)
# z = "xyz"
# j = "j"
# while j in z:
#     print(j, end=" ")
# d = {0: 'a', 1: 'b', 2: 'c'}
# for i in d:
#     print(i)
# MANGO = APPLE
# print('2' == 2)
# print(print(print("javatpoint")))     
# print(True ** False / True)
# int1 = 10
# int2 = 6
# if int != int2:
#     int2 = ++int2
# print(int1 - int2)
# print(6 + 5 - 4 * 3 / 2 % 1)     
# print(6 + 5 - 4 * 3 / 2 % 1)
# word = "javatpoint"
# print(*word)
# _ = '1 2 3 4 5 6'
# print(_)
# print(max("zoo 145 com"))
# a = "123789"
# while x in a:
#     print(x, end=" ")
# flag = ""
# a = 0
# i = 1
# while(a < 3):
#     j = 1
# if flag:
#     i = j * i + 5
# else:
#     i = j * i + 1
# a = a + 1
# print(i)
# str = [(1, 1), (2, 2), (3, 3)]   
# print(type(str))
# a = 2
# count=0
# while(a > -100):
#     a = a - 1
#     print(a)
#     count+=1
# print(count)
# arr = [3 , 2 , 5 , 6 , 0 , 7, 9]
# add1 = 0
# add2 = 0
# for elem in arr:
#     if (elem % 1 == 0):
#         add1 = add1 + elem
#         continue
#     if (elem % 3 == 0):
#         add2 = add2 + elem
# print(add1 , end=" ")
# print(add2)
# mytuple1=(5, 1, 7, 6, 2)
# mytuple1.pop(2)
# print(mytuple1)
# mytuple1 = (2, 4, 3)
# mytuple3 = mytuple1 * 2
# print(mytuple3)
# numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# sorted_numbers = sorted(numbers)
# print(type(sorted_numbers))
# example = ["Sunday", "Monday",
# "Tuesday", "Wednesday"];
# print(example[-3:-1])
# dict1 = {'first' : 'sunday', 'second' : 'monday'}
# dict2 = {1: 3, 2: 4}
# dict1.update(dict2)
# print(dict1)
# s = {1, 2, 3, 3, 2, 4, 5, 5}
# print(type(s))
# arr = [3 , 2 , 5 , 6 , 0 , 7, 9]
# add1 = 0
# add2 = 0
# for elem in arr:
#     if (elem % 1 == 0):
#         add1 = add1 + elem
#         continue
#     if (elem % 3 == 0):
#         add2 = add2 + elem
# print(add1 , end=" ")
# print(add2)
# flag = ""
# a = 0
# i = 1
# while(a < 3):
#     j = 1
#     if flag:
#         i = j * i + 5
#     else:
#         i = j * i + 1
#     a = a + 1
# print(i)
# x = 1
# while True:
#     if x % 5 == 0:
#         break
#     print(x)
#     x += 1
# k = min(max(False,-3,-4),2,7)
# print(k)
# x=1
# print(x<<2)
# x = 'abcd'
# for i in range(len(x)):
#     print(i)
# d = {"jhon":40,"Peter":45}
# print(d["jhon"])
# x =15 
# y = 12
# print(x&y)
# m = []
# while True:
#     o = int(input("Enter a  number : "))
#     m.append(o)
#     if input("do you want to add more numbers)yes/no)") == 'no' :break
# advit = int(input("Enter the number in list you would like to see"))
# print(m[advit-1])
# odd = []
# even = []

# while True:
#     n = int(input("Enter a number: "))
#     if n % 2 != 0:
#         odd.append(n)
#     elif n % 2 == 0:
#         even.append(n)
#     if input("Are there any more numbers (yes/no): ") == 'no':
#         break

# print("These are the odd numbers:", ', '.join(map(str, odd)))
# print("These are the even numbers:", ', '.join(map(str, even)))
# print(1==1 and (not(1==1 or 1==0)))
# def s (v):
#     sum1=0
#     for i in v:
#         if i%2!=0:
#             sum1+=v[i]
#         else:
#             sum1-=i
#     print(sum1)
# dict={1:2,2:4,3:6,5:8}
# s(dict)
# def ink (k):
#     print(k)

# ink("Hi")
# class test:
#     def __init__(self,a="Hello World"):
#         self.a=a

#     def display(self):
#         print(self.a)
# object = test()
# object.display()
# class test:
#     def init(self,a) :
#         self.a=a
#     def display(self):
#         print(self.a)
# obj=test()
# obj.display()
# class A:
#     def init (self,b):
#         self.b=b
#     def display(self):
#         print (self.b)
# obj=A("Hello")
# del obj
# s=open("C:\Users\Sumesh Saini\Desktop\sum.txt" ,mode='r')
# number_of_words=0
# number_of_words_chars=0
# number_of_line=0
# for line in s:
#     number_of_line+=1
#     line=line.strip("\n")
#     number_of_words_chars+=len(line)
#     list1=line.split()
#     number_of_words+=len(list1)
# s.close
# print("number of lines:" ,number_of_line)
# print("number of lines:" ,number_of_words)
# print("number of lines:" ,number_of_line)
# suyash = [1,2,3,4,5]
# suyash.pop[1]
# print(suyash)
# l=[]
# l.append(3)
# print(l)
# a,b=0,1
# count=2
# print("Fibonacci Serie Upto 10 : ")
# print(f"{a}\n{b}")
# while count<10:
#     c = a+b
#     print(c)
#     a=b
#     b=c
#     count+=1
# def add (x,y):
#     return x + y
# def sub (x,y):
#     return x - y
# def product (x,y):
#     return x * y
# def divide (x,y):
#     if y == 0 : 
#         return "Error Division by zero!"
#     else:
#         return x / y
# def modulus (x,y):
#     if y == 0:
#         return "Error Modulus by zero"
#     else:
#         return x + y
# def Menu():
#     print("Select a operation with a given number : ")
#     print("1 -> Addition")
#     print("2 -> Subtraction")
#     print("3 -> Divide")
#     print("4 -> Multiplication")
#     print("5 -> Modulus")
#     print("6 -> Exit")
# def calculator():
#     while True:
#         Menu()
#         user_choice = int(input("Enter your choice (1-6) :" ))
#         if user_choice in (1,2,3,4,5):
#             x = float(input("Enter first number : "))
#             y = float(input("Enter second number : "))
#             if user_choice == 1 :
#                 print(f"Result {add(x,y)}")
#             elif user_choice == 2 :
#                 print(f"Result {sub(x,y)}")
#             elif user_choice == 4 :
#                 print(f"Result {product(x,y)}")
#             elif user_choice == 3 :
#                 print(f"Result {divide(x,y)}")
#             elif user_choice == 5 :
#                 print(f"Result {modulus(x,y)}")
#         elif user_choice == 6 :
#             print("Exited")
#             break
#         else :
#             print(f"{user_choice} is invalid please select a valid one among (1-6)")
            
# calculator()
# def add(a, b):
#     """
#     This function adds two numbers together.

#     Parameters:
#     a (int): The first number.
#     b (int): The second number.

#     Returns:
#     int: The sum of a and b.
#     """
#     return a + b
# print(add.__doc__)
# class Employee:
#     def __init__(self, name, designation, gender, date_of_joining, salary):
#         self.name = name
#         self.designation = designation
#         self.gender = gender
#         self.date_of_joining = date_of_joining
#         self.salary = salary

# class Organization:
#     def __init__(self):
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def total_employees(self):
#         return len(self.employees)

#     def count_gender(self):
#         male_count = sum(1 for emp in self.employees if emp.gender == 'Male')
#         female_count = sum(1 for emp in self.employees if emp.gender == 'Female')
#         return male_count, female_count

#     def salary_more_than_10000(self):
#         return [emp for emp in self.employees if emp.salary > 10000]

#     def asst_manager(self):
#         return [emp for emp in self.employees if emp.designation == 'Asst Manager']

# # Creating employees
# emp1 = Employee("John Doe", "Manager", "Male", "2022-01-01", 15000)
# emp2 = Employee("Jane Smith", "Asst Manager", "Female", "2022-01-15", 12000)
# emp3 = Employee("Mike Johnson", "Clerk", "Male", "2022-02-10", 8000)
# emp4 = Employee("Emily Brown", "Asst Manager", "Female", "2022-03-05", 11000)

# # Creating organization
# org = Organization()
# org.add_employee(emp1)
# org.add_employee(emp2)
# org.add_employee(emp3)
# org.add_employee(emp4)

# # Computing various details
# print("Total number of employees:", org.total_employees())

# male_count, female_count = org.count_gender()
# print("Number of male employees:", male_count)
# print("Number of female employees:", female_count)

# print("Employees with salary more than 10,000:")
# for emp in org.salary_more_than_10000():
#     print(emp.name, emp.salary)

# print("Employees with designation Asst Manager:")
# for emp in org.asst_manager():
#     print(emp.name, emp.designation)

# Function definition with keyword arguments
# def greet(name, message):
#     print(f"Hello, {name}! {message}")

# # Using keyword arguments
# greet(name="Alice", message="Good morning")  # Output: Hello, Alice! Good morning
# greet(message="How are you?", name="Bob")    # Output: Hello, Bob! How are you?
# Define a lambda function to check if a number is even
# is_even = lambda x: x % 2 == 0

# # Function to display whether the number is even or odd
# def display_even_or_odd(number):
#     if is_even(number):
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

# # Input from the user
# number = int(input("Enter a number: "))

# # Display whether the number is even or odd
# display_even_or_odd(number)

# def find_greatest(a, b, c):
#     """
#     Function to find the greatest number from three given numbers.
#     """
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# # Input from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Call the function and display the result
# greatest = find_greatest(num1, num2, num3)
# print(f"The greatest number is: {greatest}")
