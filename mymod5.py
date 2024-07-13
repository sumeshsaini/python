import mymod4
print("TOP level in two.py")
mymod4.finc()
if __name__ == "__main__":
    print("Two.PY is running directly")
else:
    print("TWO.py has been imported")