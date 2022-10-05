airplane_toys = [ 898, 732, 543, 878 ]

#TODO Which airplane toy part are we missing the most? Use min() to find the minimum values in each list.

print('toy part we are missing the most: ', min(airplane_toys))

#TODO Is there an airplane toy part that we are overstocking? Use max() to find the maximum value in each list.

if max(airplane_toys) > 1000:
    print('this toy part is overstocking: ', max(airplane_toys))
else:
    print("there is not overstocking")