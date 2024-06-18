def palindrome(s):
    s=s.replace(' ','')
    k=s[::-1]
    if k == s:
        return f"{s} is palindrome"
    else:
        return f"{s} is not a palindrome"
print(palindrome("nurses run"))