# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 
# and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
# represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# The directory dir contains two sub-directories subdir1 and subdir2. 
# subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a 
# file within our file system. For example, in the second example above, 
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 
# (not including the double quotes).

# Given a string representing the file system in the above format, return the 
# length of the longest absolute path to a file in the abstracted file system. 
# If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.

# Assuming that valid strings are passed in. Example, if theres more tabs after a file 
# than the previous file that is an invalid file system. If multiple files are in tandem
# then they must have the same amount of tabs 

# \t xxxx \n is how we get the filename substrings
# if . in substring, then its a file 
# if false, its a directory 

def numTabs(string):
	count = 0
	for char in string:
		if char == "\t":
			count += 1
	return count

def longestPath(path):
	print("File System is:\n")
	print(path)

	substrings = path.split("\n")
	clean = [st.replace("\t", "") for st in substrings]
	tabs = [numTabs(sub) for sub in substrings]
	# we can now identify an ascending order of digits, where every number except the last
	# must be a directory

	print(substrings)
	print(clean)
	print(tabs)
	# if the number decreases from the previous highest number, 
	# start the search over at the next index and append the current result

	chains = []
	curr = []
	index = 1
	check = 1
	ctr = 1
	# feels really convoluted. There's gotta be a simpler way 
	while ctr < len(tabs):
		# print("Current Number = %d Check = %d Index = %d" % (tabs[ctr], check, index))
		if tabs[ctr] == check:
			curr.append(ctr)
			check += 1
			ctr += 1
		elif tabs[ctr] < check:
			chains.append(curr)
			curr = []
			check = 1
			index += 1
			ctr = index
		elif tabs[ctr] > check:
			index += 1
			ctr = index
	chains.append(curr)

	print(chains)

	# we want the longest length chain
	# with a check that the last elem in the list
	# is indeed a file, not a directory

	fileCatch = []
	temp = []
	for chain in chains: 
		temp = []
		if "." in clean[chain[-1]]:
			temp.append(clean[0])
			for item in chain:
				temp.append(clean[item])
			fileCatch.append(temp)

	longest = max(fileCatch, key = len)

	finalstring = ""
	for file in longest: 
		finalstring += file + "/"


	return finalstring[:-1]

print(longestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(longestPath("c\n\tc1\n\tc2\n\tc3\n\tc4\n\t\tf1.txt\n\t\td1\n\t\td2\n\t\t\tf2.txt\n\t\t\tz1\n\t\t\t\tf3.txt"))
