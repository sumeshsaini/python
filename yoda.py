your_Text = input("Enter : ")
# method 1
def yods(n):
    """Reverses a text"""
    n2 = ''.join(reversed(n))
    return n2
print(yods(your_Text))
#method 3
word = your_Text.split()
reverse_word=word[::-1]
r2 = ' '.join(reverse_word)
print(r2)
#method 4
word = your_Text.split()
reverse_word=word[::-1]
print(*reverse_word)