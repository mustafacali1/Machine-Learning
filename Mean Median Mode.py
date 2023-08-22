import numpy as np
from scipy import stats

# Mean Median Mode are basically how and where we look at to the numbers.

# for example, we have list of degrees which student had in math exam

degrees = [80, 90, 100, 80, 75, 85, 72, 80, 55, 95, 100, 80]

# region Mean
# Mean is average value in a list.

mean_value = np.mean(degrees)  # it will return 82.67
print(mean_value)

# endregion

# region Median

# Median is the middle value in a list

median_value = np.median(degrees)  # it will return 80
print(median_value)

# endregion

# region Mode

# Mode is the most appear value in a list

mode_value = stats.mode(degrees)  # it will return mode=80, count=4
print(mode_value)

# endregion
