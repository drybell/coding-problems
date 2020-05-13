# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

mappings = {}

for i in range(1,27):
	mappings[str(i)] = str(chr(i + 96))

# example inputs: 
#					'111' = 3 
#                   

# basically just have to make all substrings of the string
# and see if any fall into our encoding chart 
# most of the time it's the length of the substring list
# but you have to make sure they fall within the numbers within
# the encoding chart. 

def allSublists(aList):
	sublist = []
	for i in range(0, len(aList)):
		for j in range(i + 1, len(aList)):
			curr = aList[i:j]
			sublist.append(curr)
	return sublist

def numDecodings(aString):
	allDigits = list(aString)
	sublist = allSublists(allDigits)
	counter = 0 
	for sub in sublist:
		tempstring = ""
		if len(sub) > 1:
			for item in sub:
				tempstring += item
		else:
			tempstring += sub[0]

		if mappings.get(tempstring):
			counter += 1 
	return counter

assert numDecodings('111') == 3 
assert numDecodings('1111') == 5
assert numDecodings('2626') == 4
