import numpy as np

# Standard Deviation is a value that explain how spread the list.

# for example, we have list of degrees which student had in math exam

degrees = [80, 90, 100, 80, 75, 85, 72, 80, 55, 95, 100, 80]

std_value = np.std(degrees)

print(std_value)  # it will return 12.17 which means  most of the values are within the range of 12.17 from the mean value, which is 82.6.
