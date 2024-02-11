number = int(input("Enter the number till where you want to check : "))
for num in range(1,number +1) :
  if num%3 == 0 and num %5==0 :
    print("FizzBuzz")
  elif num %3 == 0 :
    print("Fizz")
  elif num%5 == 0 :
    print("Buzz")
  else :
    print(num)