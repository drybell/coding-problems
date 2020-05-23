# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. 
# i is guaranteed to be smaller than or equal to N.

# fixed and sorted array that is allocated to hold N order ids,
# has constant time for last element and O(n) time for record

# assuming order ids are distinct integers
# recent is first. 
# Don't shift every single array index, but create a new array with 
# 

import random # for testing 

class SortedFixedArray: 
	def __init__(self, N):
		self.N = N
		self.array = [None] * N
		self.size = 0

	def record(self, order_id): 
		if self.size < self.N:
			i = 0
			while self.array[i] != None: 
				i += 1
			self.array[i] = order_id
			self.size += 1
		else:
			self.array.append(order_id)
			del self.array[0]

	def get_last(self, i):
		if i > self.size: 
			return "Error: i must be less than array size"
		else:
			return self.array[self.size - i]

	def size():
		return self.size

	def print(self):
		print("Most recent order IDs: ", end="")
		rev = [ele for ele in reversed(self.array)]
		for i in range(self.N - self.size, self.N):
			print(rev[i], end=" ")
		print()


temp = SortedFixedArray(10)
temp.print()
print(temp.size)
for i in range(5):
	temp.record(i)
print(temp.get_last(2))
temp.print()

test = SortedFixedArray(100)
noduplicates = []
samples = random.sample(range(100000,1000000), 300)
for item in samples:
	test.record(item)
test.print()
print(test.size)



