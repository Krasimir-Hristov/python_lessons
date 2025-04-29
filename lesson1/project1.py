name = input("Enter your name: ")
print("Hello " +  name + " Welcome to my game!")

should_we_play = input("Should we play? (yes/no) ").lower()

if should_we_play == "yes":
    print("Let's play!")
else:
    print("No problem!")
