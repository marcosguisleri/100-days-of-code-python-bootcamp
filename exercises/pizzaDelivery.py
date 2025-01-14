print("Welcome to Python Pizza Deliveries! ")

size = input("What size pizza do you wants? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price_Pizza = 0

if size == "S":
    price_Pizza += 15
    if pepperoni == "Y":
        price_Pizza += 2
    if extra_cheese == "Y":
        price_Pizza += 1
elif size == "M":
    price_Pizza += 20
    if pepperoni == "Y":
        price_Pizza += 3
    if extra_cheese == "Y":
        price_Pizza += 1
else:
    price_Pizza += 25
    if pepperoni == "Y":
        price_Pizza += 3
    if extra_cheese == "Y":
        price_Pizza += 1
        
print(f"Your final bill is: R${price_Pizza}")
        