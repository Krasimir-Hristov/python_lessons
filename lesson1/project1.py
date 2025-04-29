name = input("Enter your name: ")
print("Hello " +  name + " Welcome to my game!")

should_we_play = input("Should we play? (yes/no) ").lower()
# should_we_play = input("Should we play? (yes/no) ").upper()



if should_we_play == "y" or should_we_play == "yes":
    print("Let's play!")
# elif should_we_play == "YES":
#         print("WELCOME TO THE GAME!")
else:
    print("No problem!")
