name = input("Enter your name: ")
print("Hello " +  name + " Welcome to my game!")

should_we_play = input("Should we play? (yes/no) ")

if should_we_play == "yes":
    print("Let's play!")
elif should_we_play == "YES":
    print("LETS PLAY!")
else:
    print("No problem!")
