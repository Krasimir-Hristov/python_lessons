name = input("Enter your name: ")
print("Hello " +  name + " Welcome to my game!")

should_we_play = input("Should we play? (yes/no) ")

play = should_we_play == "yes"


if play:
    print("Let's play!")
else:
    print("No problem!")