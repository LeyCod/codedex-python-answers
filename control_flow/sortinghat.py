# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each freshman student goes to:

# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin

# Write a sortinghat.py program that asks the user some questions using int() and places them into one of the Houses based on their answers. 

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = input("""Do you like Dawn or Dusk? 
    Your answerd: """).lower()

if Q1 == "dawn":
    Gryffindor +=1 
    Ravenclaw += 1
elif Q1 == "dusk":
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Invalid input")

Q2 = input("""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold 
    Your answerd: """).lower()

if Q2 == "the good": 
    Hufflepuff += 1
elif Q2 == "the great":
    Slytherin += 1
elif Q2 == "the wise":
    Ravenclaw += 1
elif Q2 == "the bold":
    Gryffindor += 1
else:
    print("Invalid input")


Q3 = input("""Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum 
    Your answerd: """).lower()

if Q3 == "the violin":
    Slytherin += 1
elif Q3 == "the trumpet":
    Hufflepuff += 1
elif Q3 == "the piano":
    Ravenclaw += 1
elif Q3 == "the drum":
    Gryffindor += 1
else:
        print("Invalid input")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("The Sorting Hat has decided that you will be in Gryffindor!")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("The Sorting Hat has decided that you will be in Ravenclaw!")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("The Sorting Hat has decided that you will be in Hufflepuff!")
else:
    print("The Sorting Hat has decided that you will be in Slytherin!")