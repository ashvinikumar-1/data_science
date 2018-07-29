# Import pandas as pd
import pandas as pd
import numpy as np

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)
# Use dr to subset cars: sel
sel =cars[(dr == True)]

# Print sel
print(sel)


# Create car_maniac: observations that have a cars_per_cap over 500

cpc = cars['cars_per_cap']
print(cpc)
many_cars = cars[cpc > 500]

# Print car_maniac
print(many_cars)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']

between = np.logical_and(cpc>100,cpc<500)

medium = cars[between]

print(medium)
