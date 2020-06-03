# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count
#  and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits
# and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

def runEncode(string):

	testletter = ""
	prev = string[0]
	count = 0
	encoded = ""
	for letter in string: 
		# print(letter)
		testletter = letter
		if testletter != prev: 
			encoded += (str(count) + prev)
			count = 1
			# print(encoded)
		else:
			count += 1
		prev = testletter
	# have to add the last one 
	encoded += (str(count) + string[-1])
	return encoded 


def runDecode(encoded):

	number = 0 
	letter = ""
	decoded = ""
	# all even indices [0..2..4..] are numbers
	# all odd indices [1..3..5..] are the letters
	# all encoded strings are even length
	for i in range(0,len(encoded), 2):
		for j in range(int(encoded[i])):
			decoded += encoded[i + 1]
	return decoded


# print(runEncode("AAAABBBCCDAA"))
# print(runEncode("teststring"))

# algebraic law: runDecode(runEncode(anystring)) == anystring
assert runDecode(runEncode("teststring")) == "teststring"
assert runDecode(runEncode("AAAABBBCCDAA")) == "AAAABBBCCDAA"

# print(runEncode("AABBCCDDDDAABBCCEEEEEDGGJZVBNNSSLLL"))
assert runDecode(runEncode("AABBCCDDDDAABBCCEEEEEDGGJZVBNNSSLLL")) == "AABBCCDDDDAABBCCEEEEEDGGJZVBNNSSLLL"
