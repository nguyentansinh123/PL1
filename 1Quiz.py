print("Welcome to my computer quiz!")

playing = input(" Do you want to play: ")

if playing != "yes":
    quit()

print("Okay lets play! ")

answer = input(" What does cpu stand for: ")

if answer != "cock":
    print("false")
else:
    print("true")