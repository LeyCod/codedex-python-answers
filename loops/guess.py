guess = 0

tries = int(input("How many tries do you think you need to guess the number? "))

while guess != 6:
    guess = int(input("Guess the number:  "))
    tries -= 1
    if guess == 6:
        print("You got it! and it takes you", tries, "tries.")
    elif tries == 0:
        print("You lost!")
        break
    


