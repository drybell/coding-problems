# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring 
# that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, 
# the longest substring with k distinct characters is "bcb".

# Example 
# if k = 4 
# the string "slqsilooslqitslqislqi"
# will have "slqislqi" as the longest substring. 

# I believe, to start, we must take all slices of the string 
# while maintaining order and making sure there are k distinct 
# characters by appending it to a fixed k length list. 
# If you can't append the next character, save it and try again.

def kDistinctChar(k, s): 
	# initialize fixed k size array 
	kLetters = []

	#np.zeros but I'm lazy 
	for i in range(0, k): 
		kLetters.append(0)

	substrings = []
	# iterate through each letter, build up the substring 
	for i in range(0, len(s)):
		j = i 
		string = ""
		kLetters = []

		#np.zeros but I'm lazy 
		for i in range(0, k): 
			kLetters.append(0)

		curr = 0 #index of kLetters
		# definitely messed up simple logic here with k and curr 
		while j < len(s):
			newletter = s[j]
			if newletter not in kLetters and curr == k: 
				break
			elif newletter not in kLetters:
				kLetters[curr] = newletter
				curr += 1 
			# print(kLetters)
			# print(curr)
			string += newletter 
			j += 1
			# print(string)
		substrings.append(string)
	maxlength = 0
	index = 0
	for i in range(0, len(substrings)):
		sub = substrings[i]
		if len(sub) > maxlength:
			maxlength = len(sub)
			index = i 
	return substrings[index] 


assert kDistinctChar(2,"abcba") == "bcb"
assert kDistinctChar(4,"slqsilooslqitslqislqi") == "slqislqi"