print("Welcom to Treasure Island. Your mission is to find the treasure!!")
choice = input("Enter a specific direction Left or Right ? ").lower()
if choice == 'left':
    choice = input("Choice Swim or Wait ? ").lower()
    if choice == 'wait':
        choice = input("Which door Red, Blue or Yellow ? ").lower()
        if choice == 'yellow':
            print("You are the winner!!")
        elif choice == 'bleu':
            print("Eaten by beasts. Game Over!!")
        elif choice == 'red':
            print("Burned by fire. Game Over!!")
        else:
            print("Game Over!!")
    elif choice == 'swim':
        print("Attacked by trout. Game Over!!")
    else:
        print("Game Over!!")
elif choice == 'right':
    print("Fall into a hole. Game Over!!")
else:
    print("Game Over!!")