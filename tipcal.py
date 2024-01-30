print("Welcome to the tip calculator .")
bill = float(input("What is the total amount?\n"))
tip  = int(input("Percentage for the tip of the bill? \n"))
people = int(input("How many persons are going to split ?\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
to_pay_each = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {to_pay_each}")