import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# regression is a method use for find relationship between variables.

# region Linear Regression

# Linear regression is a linear approach for modelling the relationship between variables.

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept


my_model = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()

# endregion
