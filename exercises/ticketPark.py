print("Welcome to the rollercoaster! ")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster. ")
    age = int(input("Whats is you age? "))
    if age < 12:
        bill = 5
        print("Child tickets are R$5. ")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are R$7. ")
    else:
        bill = 12
        print("Adult tickets are R$12. ")
    
    wants_photo = input("Do you want to have a phto take? Type y for Yes and n for No. ")
    
    if wants_photo == "y":
        bill += 3;
    
    print(f"Your final bill is R${bill} ")

else:
    print("Sorry you have to grow taller before you can ride. ")

