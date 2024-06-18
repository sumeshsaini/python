def old_macdo(a):
    first_letter = a[0]
    in_range = a[1:3]
    fourth_letter = a[3]
    rest_letters = a[4:]
    return first_letter.upper() + in_range+ fourth_letter.upper()+rest_letters
print(old_macdo("Byebb"))
    