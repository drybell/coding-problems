# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i
#  of the new array is the product of all the numbers in the original array except 
# the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be     
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
# [2, 3, 6].

# Follow-up: what if you can't use division?

# alg laws: [cons x xs] == [x1 * x2 * ... * xn, x1 * x3 * ... * xn, ... , x1 * x2 * ... * xn-1]
#           [x, y ,z]   == [y*z, x*z, x*y]
#           [x, y]      == [y, x]
#           [x]         == [x]
#           []          == []

# example inputs ==> [3, 2, 1] == [2, 3, 6]
from functools import reduce 

def multiplyExceptI(array): 
	lengtharray = len(array)
	originalarray = array.copy()
	if lengtharray == 0: 
		return array
	else: 
		for i in range(0, lengtharray):
			temparray = originalarray.copy()
			temparray.remove(temparray[i])
			array[i] = reduce(lambda x,y: x*y, temparray, 1)
		return array


def main():
	print("Input = [1,2,3,4,5] Output = ", end="")
	print(multiplyExceptI([1,2,3,4,5]))
	print("Input =     [1,2,3] Output = ", end="")
	print(multiplyExceptI([3,2,1]))

if __name__ == '__main__':
	main()

# took a solid hour, learned about reduce and lambda syntax
# lots of copies here, will try in SML for less memory usage 
