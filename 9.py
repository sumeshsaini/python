try:
    with open('my.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())  # Strip removes any leading/trailing whitespace
except FileNotFoundError:
    print("File not found. Please check the file path.")
