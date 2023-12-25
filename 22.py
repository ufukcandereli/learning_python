# The Auction

print("Welcome to the Auction!")
auction_going = True
highest = 0
winner = None
names_and_bids = {}

while auction_going:
    name = input("What is your name?: ")
    bid = int(input("How much is your offer?: $"))
    names_and_bids[name] = bid
    another_user = input("Is there anybody who wants to bid? (yes/no): ").lower()

    if another_user == "no":
        auction_going = False
        for user, value in names_and_bids.items():
            if value > highest:
                highest = value
                winner = user
        print(f"The winner is {winner} with a bid of ${highest}")





