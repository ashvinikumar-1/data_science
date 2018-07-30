# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)


# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+": "+str(row['cars_per_cap']))


# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = str.upper(row["country"])


# Print cars
print(cars)

cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
