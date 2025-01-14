print('''             _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/   
   ||                hjm
''')

print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")

choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "Left" or Right". ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to lake, there is an island in the middle of the lake. '
                    'Type "Wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "Tehre is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over. ")
        elif choice3 == "yellow":
            print("You found the treasure. You Win! ")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over. ")
        else:
            print("You chose a door that doesn't exist. Game Over. ")
    else:
        print("You got attacked by angry trout. Game Over. ")
else:
    print("You fell in to a hole. Game Over. ")