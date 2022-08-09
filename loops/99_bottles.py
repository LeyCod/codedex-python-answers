number = 99

for num in range(number, 0, -1):
    if num == 1:
        print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall...")
    else:
        print(f"{num}, bottles of beer on the wall, {num}, bottles of beer.")
        print(f"Take one down, pass it around, {num-1}, bottles of beer on the wall.")
