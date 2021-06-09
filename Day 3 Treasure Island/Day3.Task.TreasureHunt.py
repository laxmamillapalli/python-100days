print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You got a map but it is not clear which direction to go!")
choice1 = input("You have arrived at a cross roads, now chose to go 'left' or 'right': ")
if choice1 == "left":
    print("You have chosen right direction!")
    print("You have arrived at a lake! Local people said the boat will come and asked you to wait.")
    choice2 = input("Would you like to wait for boat or swim. Type 'wait' to wait and 'swim' to swim: ")
    if choice2 == "wait":
        print("Good that you have waited for the boat! There are Alligators waiting for you.")
        print("You have found 3 houses: red, blue and yellow.")
        choice3 = input("Enter one of the 3 houses. Choose 'red', 'blue' or 'yellow' :")
        if choice3 == "red" :
            print("The caught on fire!")
            print("#### Gameover ####")
        elif choice3 == 'blue':
            print("This is a room full of ice. It is freezing!")
            print("#### Gameover ####")
        elif choice3 == "yellow":
            print("You have found the Treasure")
            print("##################")
            print("##################")
            print("#### Congrats ####")
            print("##################")
            print("##################")
        else:
            print("It looks like you are drunk! I do not think you entered one of the three houses!")
            print("#### Gameover ####")
    else:
        print(f"Wrong choice: {choice2}. Alligators ate your bum muhahaha!")
        print("#### Gameover ####")
else :
    print(f"Wrong choice: {choice1}. Bandits attacked you! You ran back home naked LOL!")
    print("#### Gameover ####")