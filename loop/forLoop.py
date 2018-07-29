# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for var in areas:
    print(var)

# Change for loop to use enumerate() and update print()
for x,y in enumerate(areas) :
    print("room "+str(x)+": "+str(y))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for list in house:
    print("the " + str(list[0]) + " is " + str(list[1]) + " sqm")