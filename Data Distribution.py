import numpy
import matplotlib.pyplot as plt

# We worked on small data previously. Now we will create large data with using numpy.

rand_list = numpy.random.uniform(1, 100, 25000)

# Now we will create a histogram with the rand_list above

plt.hist(rand_list, 20)  # it draws 20 bars histogram
plt.show()

# and here is an example of normal distribution graph. also known as shape of a bell.
rand_list_normal = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(rand_list_normal, 100)
plt.show()
