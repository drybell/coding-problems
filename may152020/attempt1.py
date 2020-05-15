# This problem was asked by Apple.

# Implement a job scheduler which takes in a function 
# f and an integer n, and calls f after n milliseconds.

from time import sleep 

def jobSched(f, n):
	sleep(n)
	f()


def square5():
	return 5^2


print("Starting...")

# in milliseconds 
pause = 850 / 1000 # for use with time.sleep 

jobSched(square5, pause)

print("Done.\n Took %f seconds" % (pause))