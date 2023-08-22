import numpy as np

# Percentiles describe the value that a given percent of the values are lower than.

# for example, we have list of degrees which student had in math exam

degrees = [80, 90, 100, 80, 75, 85, 72, 80, 55, 95, 100, 80]

# what is the 80. percentile?

eighty_percentile = np.percentile(degrees, 80)

print(eighty_percentile)  # it will return 94 which means 80% of notes are below 94.
