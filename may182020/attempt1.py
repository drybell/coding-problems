# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
#  Given N, write a function that returns the number of unique ways you can climb the staircase. 
#  The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? For example, 
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# N = 5
# 1 1 1 1 1 
# 1 1 1 2 
# 1 1 2 1 
# 1 2 1 1 
# 2 1 1 1 
# 2 2 1 
# 1 2 2
# 2 1 2 

# N = 6 
# 1 1 1 1 1 1 
# 1 1 1 1 2 
# 1 1 1 2 1 
# 1 1 2 1 1 
# 1 2 1 1 1 
# 2 1 1 1 1 
# 1 1 2 2 
# 1 2 1 2
# 2 1 1 2 
# 2 2 1 1 
# 2 1 2 1
# 2 2 2 1
# 1 2 2 2 


# For the simple approach with no limitations, its permutations 
# of 1 and 2 given they add to N 

# always calculate the simplest approach of all 1s, all 2s. 
# That gives us the min and max number of steps. 

# if N is even, len 1s is N, # 2s is N/2. 

# if N is odd, len 1s is N, # 2s is N/2 + 1 

# how many permutations do you have from lengths N/2 to N or N/2 + 1 to N? 

# it boils down to finding the permutations of how to write a word given two letters

# as the length of N/2 increases, the frequency of 1s increases by 2, and the frequency
# of 2 goes down by 1 

def factorial(n):
	if n <= 0:
		return 1 
	else:
		return n * factorial(n - 1)

assert factorial(6) == 720

def climbStairs(N):
	total = 0
	start = 0
	counter = 0
	if N % 2 == 0: 
		start = int(N/2)
		freq2 = start
		for i in range(start, N+1):
			# print("Counter is %d, i is %d" % (counter, i))
			freq1 = (counter * 2)
			total += int(factorial(i)/(factorial(freq1)*factorial(freq2)))
			# print("Frequency of 1s == %d, Frequency of 2s == %d" % (freq1, freq2))
			freq2 -= 1
			counter += 1
	else: 
		start = int(N/2 + 1)
		freq2 = int(N/2)
		for i in range(start, N+1):
			# print("Counter is %d, i is %d" % (counter, i))
			freq1 = (counter * 2) + 1
			total += int(factorial(i)/(factorial(freq1)*factorial(freq2)))
			# print("Frequency of 1s == %d, Frequency of 2s == %d" % (freq1, freq2))
			freq2 -= 1
			counter += 1
	return total

assert climbStairs(4) == 5
assert climbStairs(5) == 8
for i in range(6, 20):
	print("Climbing stairs of length %d has %d unique permutations" % (i, climbStairs(i)))




