# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits.csv'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)