yuan = float(input("What do you have left in yuan?: "))
yen = float(input("What do you have left in yen?: "))
won = float(input("What do you have left in won?: "))

yuanToDolar = yuan * 0.15 

yenToDolar = yen * 0.0074

wonToDolar = won * 0.00077

usd = yuanToDolar + yenToDolar + wonToDolar

print("Your total in USD is: ", usd)

