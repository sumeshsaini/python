def ask():
    while True:
        try :
            result = int(input("Enter a integer : "))
        except:
            print("An error occured, please try again.")
        else:
            print(f"The square of your number is {result**2}")
            break
if __name__ == "__main__":
    ask()


