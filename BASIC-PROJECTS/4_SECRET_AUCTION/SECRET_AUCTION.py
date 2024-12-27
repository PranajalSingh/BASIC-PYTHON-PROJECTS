data={}
more="yes"
max_bid=0
winner = None
bid = None
winner_bid = None

while more=="yes":
    bidder=input("name of the user : ")
    bid=int(input("bid amount : $"))
    data[bidder]=bid
    for i in data:
        if bid>max_bid:
            max_bid=bid
            winner=bidder
            winner_bid = data[bidder]
    more=input("type yes if there are more people : ")

#print(data)
print(f"{winner} won the auction with ${winner_bid} bid.")
