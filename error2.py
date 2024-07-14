def ask_a_int():
    while True:
        try :
            result = int(input("Enter a int number : "))
        except:
            print("That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
ask_a_int()