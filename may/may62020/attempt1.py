# Daniel Ryaboshapka
# Coding Interview Question from Google 
# Courtesy of Daily Coding Problem 

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


# Example inputs: [] k == false
#                 [1] k == false
#                 [1 2] 3 == true 
#                 [2 4] 3 == false 
#                 [5 3 7 1] 12 == true 
# 				  [5 3 7 1] 4  == true 

# Brute force solution: iterate through array of length n, then n - 1, all the way to list of size 1
# 	This way would find every pairing of numbers --> O(n^2)

def slowTwoSum(listofnums, k): 
	if listofnums == [] or len(listofnums) == 1:
		return False

	temp = listofnums.copy()

	num = 0
	while len(temp) >= 2 : 
		num = temp.pop()
		for elem in temp:
			if addUpToK([num,elem], k):
				return True
			else: 
				pass

	return False 


def addUpToK(pair, k):
	if pair[0] + pair[1] == k:
		return True
	else:
		return False


def twoSum(listofnums, k): 
	# with one pass, any two numbers add up to k 
	curr = 0 

def main():
	x = [5,3,7,1]
	y = [2,8,7,10,9,11,51]
	z = [3,2]
	w = []
	f = [2]
	k1 = 4
	k2 = 10 
	k3 = 19 
	k4 = 5

	print(slowTwoSum(f,k2))
	print(slowTwoSum(z, k4))

if __name__ == '__main__':
	main()
