logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
bidding = False
def bid_top(bidder_rec):
    highest = 0
    winner = ''
    for bidder in bidder_rec : 
        bid_amount = bidder_rec[bidder]
        if bid_amount>highest :
            highest = bid_amount
            winner  = bidder
    print(f"The winner is {winner} with a bid of {highest}")
while not bidding :
    name = input("Enter your name : ").capitalize()
    price =float(input("Enter your bid : "))
    bids[name] = price
    continue_y = input("Anymore biders type 'Yes' or 'No' : ").lower()
    if continue_y == 'no' :
        bidding = True
        bid_top(bids)
    elif continue_y == 'yes':
        pass    