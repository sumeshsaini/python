def calculate_length(string):
    return len(string)

def string_reversal(string):
    return string[::-1]

def check_equality(string1, string2):
    return string1 == string2

def check_palindrome(string):
    return string == string[::-1]

def check_substring(main_string, sub_string):
    return sub_string in main_string

def main():
    while True:
        print("\nString Operations Menu:")
        print("1. Calculate length of string")
        print("2. String reversal")
        print("3. Equality check of two strings")
        print("4. Check palindrome")
        print("5. Check substring")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            string = input("Enter a string: ")
            print("Length of the string:", calculate_length(string))
        elif choice == '2':
            string = input("Enter a string: ")
            print("Reversed string:", string_reversal(string))
        elif choice == '3':
            string1 = input("Enter the first string: ")
            string2 = input("Enter the second string: ")
            if check_equality(string1, string2):
                print("The strings are equal.")
            else:
                print("The strings are not equal.")
        elif choice == '4':
            string = input("Enter a string: ")
            if check_palindrome(string):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == '5':
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring: ")
            if check_substring(main_string, sub_string):
                print("The substring is present in the main string.")
            else:
                print("The substring is not present in the main string.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
