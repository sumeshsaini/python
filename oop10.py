class Account():
    def __init__(self,owner,value):
        self.owner = owner
        self.value = value
    def deposit_money(self,amount):
        self.value+=amount
        return f"{amount} deposited successfully. New balance: {self.value}"
    def withdraw_money(self,amount_2):
        if amount_2> self.value:
            return f"{amount_2} exceeds your current blance."
        elif amount_2<=self.value:
            return f"{amount_2} withdrawed successfully new balance : {self.value-amount_2}"
    def __str__(self):
        return f"Owner : {self.owner} Blance : {self.value}"
    def __del__(self):
        print("Account has been delted")
Money = Account("Sumesh",10000)
m = Money.withdraw_money
d = Money.deposit_money
i = Money
pro = True
while pro:
    while True:
        your_call = input("Enter W for withdraw and D for Deposit  and I for Information or Dl to delete account : ").capitalize()
        if your_call not in ["W","D","I","Dl"]:
            print("Enter a valid service")
        else:
            break
    if your_call == "Dl":
        del Money
        break
    if your_call == "I":
        print(i)
    if your_call == "W":
        m_give = float(input("Enter the amount you would like to withdraw : "))
        print(Money.withdraw_money(m_give))
        ontinue_bank = input("Enter no to exit : ").capitalize()
        if ontinue_bank == "No":
            pro=False
    elif your_call =="D":
        m_take =float(input("Enter the amount you would like to deposit : "))
        print(Money.deposit_money(m_take))
        ontinue_bank = input("Enter No to exit : ").capitalize()
        if ontinue_bank == "No":
            pro=False
