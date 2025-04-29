name = input("Enter your name: ")
print("Hello " +  name + " Welcome to my game!")

should_we_play = input("Should we play? (yes/no) ").lower()
# should_we_play = input("Should we play? (yes/no) ").upper()


if should_we_play == "y" or should_we_play == "yes":
    print("Let's play!")

    direction = input("Which direction do you want to go? (left/right) ").lower()

    if direction == "left":
        print("You found a treasure!")
        take = input("Do you want to take it? (yes/no) ").lower()
        if take == "y" or take == "yes":
            print("You die from poison")
        else:
            print("You see how many animal dies near the treasure.")
    elif direction == "right":
        print("You found a monster!")
        fight = input("Do you want to fight it? (yes/no) ").lower()
        if fight == "y" or fight == "yes":
            print("You die from the monster.")
        else:
            print("You run away.")
# elif should_we_play == "YES":
#         print("WELCOME TO THE GAME!")
else:
    print("No problem!")


