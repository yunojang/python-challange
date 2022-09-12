from replit import clear

print("Welcome to Auction")
product = input("What is product name? ")

bids = {}

next = True
while next:
    name = input("What is your name?: ")
    bid = int(input(f"What's your bid for {product}? $"))

    bids[name] = bid
    next = input("Are there any oter bidders? Type 'yes' or 'no': ") == 'yes'
    if next:
        clear()

winner = ""
max = 0
for name, price in bids.items():
    if price > max:
        max = price
        winner = name

clear()
print(
    f"The winner is {winner} with a bid of ${bids[winner]}, get your {product}"
)
