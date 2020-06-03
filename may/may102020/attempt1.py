# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear 
# time and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


# example inputs: [3, 4, -1, 1] = 2
# example inputs: [1, 2, 0] = 3 
# example inputs: [500, 200, 3, 5, 7, -12] = 1 

# definitely the size (length) of the array should be the giveaway for constant space
# i need to know only one number and the size of the array as we iterate through the array


# brute force algorithm: iterate from 1 until complete: 
# 							if number doesn't exist, return it

def bruteForce(array): 
	smallestmin = 1
	flag = False
	while not flag: 
		if smallestmin in array: 
			smallestmin += 1
		else: 
			flag = True
	return smallestmin

# def firstDecreasing(array):
# 	smallestmin = 1
# 	length = len(array)
# 	for number in array:
# 		if number == smallestmin:
# 			smallestmin = number + 1 
# 		elif number == length:
# 	return smallestmin


# assert firstDecreasing([3,4,-1,1]) == 2
# assert firstDecreasing([3,4,2,1]) == 5
# assert firstDecreasing([1,2,0]) == 3
# assert firstDecreasing([5,3,2,4,7,6]) == 1
assert bruteForce([3,4,-1,1]) == 2
assert bruteForce([1,2,0]) == 3
assert bruteForce([5,3,2,4,7,6]) == 1 
assert bruteForce([3,4,2,1]) == 5

# Guess I can't find a faster way to do this one. Tried to do two passes with 
# reversed list. 