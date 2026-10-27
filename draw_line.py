from matplotlib import pyplot
import csv

import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1) #skips the header row  


print(data )

# script to plot a line


line = pyplot.plot(data)
pyplot.show()
