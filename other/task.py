#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.

budget = int(input("enter your budget: "))

shakes = {
    "1": (3, "vanilla"),
    "2": (4, "chocolate"),
    "3": (5, "strawberry")
}

while True:
    print("shakes:")
    for option, (price, flavour) in shakes.items():
        print(f"{option}: {flavour} - ${price}")

    choice = input("what can i get you? (Q to quit)")

    if choice.upper() == "Q":
        print("goodbye")
        break

    if choice not in shakes:
        print("invalid option")
        continue

    price, flavour = shakes[choice]
    if price > budget:
        print("get out you cant afford it!!")
        break

    print(f"enjoy your {flavour} milkshake")
    budget -= price
    print(f"remaining budget is ${budget}")