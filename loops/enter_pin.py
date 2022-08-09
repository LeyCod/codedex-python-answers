print("BANK OF CODÉDEX")

pin = int(input("Enter your PIN: "))

while pin != 1111:
    pin = int(input("Incorrect PIN. Enter your PIN again: "))

    if pin == 1111:
        print("PIN accepted!")