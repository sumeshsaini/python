import random

def display_masked_gun():
    print(" _______")
    print("| ____ |")
    print("|_____|_|")
    print("|  ___  | |")
    print("| |___| | |")
    print("|  ___  |_|")
    print("| |   |___|")
    print("|_|______|")

def generate_secret_code():
    return str(random.randint(1000, 9999))

def validate_guess(guess):
    if len(guess) != 4 or not guess.isdigit():
        return False
    return True

def compare_guess(guess, secret_code):
    bull = sum(1 for i in range(4) if guess[i] == secret_code[i])
    cow = sum(min(guess.count(digit), secret_code.count(digit)) for digit in set(guess))
    cow -= bull
    return bull, cow

def play_game():
    attempts = 10
    secret_code = generate_secret_code()
    print(secret_code)
    print("Welcome to Masked Gun Game!")
    print("Try to unlock the masked gun by guessing a 4-digit code.")
    print("Each correct digit in the correct place earns a 'bull'.")
    print("Each correct digit in the wrong place earns a 'cow'.")
    print("You have 10 attempts.")

    while attempts > 0:
        print(f"Attempts left: {attempts}")
        guess = input("Enter your guess: ")

        if not validate_guess(guess):
            print("Invalid guess. Please enter a 4-digit numeric code.")
            continue

        bulls, cows = compare_guess(guess, secret_code)

        if bulls == 4:
            print("Congratulations! You've unlocked the masked gun!")
            display_masked_gun()
            break
        else:
            print(f"Feedback: Bulls: {bulls}, Cows: {cows}")
            attempts -= 1

    if attempts == 0:
        print("Sorry, you've run out of attempts. The secret code was:", secret_code)

play_game()
