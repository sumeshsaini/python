def check(num,low,high):
    if num in range(low,high+1):
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is not in the range between {low} and {high}"
print(check(5,2,7))