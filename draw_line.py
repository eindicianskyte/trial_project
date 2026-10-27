from matplotlib import pyplot
import csv

import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1) #skips the header row  


print(data )

# script to plot a line


fig, ax = pyplot.subplots() # creates a figure and a set of subplots

ax.plot(data)

pyplot.plot(data)

fig.savefig('line_plot.png') # saves the figure as a png file
pyplot.show()
