import numpy as np

height = [86, 76, 74, 80, 69, 71]
weight = [34, 56, 78,  67, 47, 78]

np_height = np.array((height, weight))

print(np_height)

# For loop over np_height
for x in np.nditer(np_height):
    print(x)
