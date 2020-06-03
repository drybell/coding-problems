# This problem was asked by Google.

# The area of a circle is defined as πr^2. 
# Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

# Basically asking, using only the rand function, approximate pi 

# So we create two domain spaces, one for a quarter unit circle, and one for a unit square,
# and divide the two counts to obtain pi/4 

# pick two points where x^2 + y^2 <= 1 

# Code to visualize, need to color the circle 1 color and square another
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
	# fig = plt.figure()
	# ax = fig.add_subplot(1, 1, 1)
	# ax.scatter(plane[:,0],plane[:,1],s=.5,marker=",")
	# plt.show()


from random import random
import numpy as np 

def approxPi(n):
	x = np.ones(n)
	y = np.ones(n)
	circle = 0
	for i in range(0, n):
		x[i] = random()
		y[i] = random()
	plane = np.column_stack((x,y))
	for [x,y] in plane:
		# print("x is %f y is %f" % (x,y))
		if (x*x + y*y) <= 1:
			circle += 1 
	pi = circle/n * 4
	return pi


# doing with random seed, answer will vary unless you specify a seed per run 
print(approxPi(1000)) # 3.292
print(approxPi(100000000)) # comes out to be 3.1414654




