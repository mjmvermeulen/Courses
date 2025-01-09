# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
auction_active = True
winning_user = ""
winning_bid = 0.00
auction_bids = {}

while auction_active:
    user_name = input("What's your name? : ")
    user_bid = float(input("Place your bid: € "))
    auction_bids.update([(f"{user_name}", f"{user_bid}")])

    other_bidders = input('\nAre there any other bidders? Type "yes" or "no" : ')

    if other_bidders == "no" or other_bidders == "No":
        auction_active = False
        for user in auction_bids.keys():
            if float(auction_bids[user]) > winning_bid:
                winning_user = user
                winning_bid = float(auction_bids[user])
        print(f"\n{winning_user} won the auction with the bid: €{winning_bid}")
        break
    print("\n" * 30)