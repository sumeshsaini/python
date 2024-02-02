def pay(earn):
    hra = 0.1*earn
    ta = 0.05*earn
    gs = hra+ta+earn
    tax = 0.02*gs
    net_earning = gs - tax
    return net_earning
earn = float(input("Enter your earnings : "))
check = pay(earn)
print(f"\n{check} is your net salary")