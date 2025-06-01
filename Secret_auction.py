from art import logo
print(logo)
def highest_bid(bid_dictionary):
    highest_bid=0
    winner=""
    for bidder in dic:
        bid_Amount=bid_dictionary[bidder]
        if highest_bid< bid_Amount:
            highest_bid=bid_Amount
            winner=bidder
    print(f"Winner is {winner} with amount Rs.{highest_bid}")

dic = {}
more_bids=True
while more_bids:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid:₨ "))
    dic[name] = bid
    more_bids= input("are there  more bids??(y/n): ").lower()
    if more_bids=="n":
        more_bids=False
        highest_bid(dic)
    elif more_bids == "y":
        print("\n"*30)
    else:
        print("Wrong input, please choose between yes or no")
