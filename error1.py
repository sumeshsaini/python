try :
    f = open('testfile','r')
    f.write("Write a test line")
except:
    print("Error")
finally:
    print("It always run")