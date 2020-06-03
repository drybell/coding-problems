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

	print(substrings)
	print(clean)
	print(tabs)

	chains = []
	curr = []
	index = 1
	check = 1
	ctr = 1
	# feels really convoluted. There's gotta be a simpler way 
	while ctr < len(tabs):
		

print(longestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(longestPath("c\n\tc1\n\tc2\n\tc3\n\tc4\n\t\tf1.txt\n\t\td1\n\t\td2\n\t\t\tf2.txt\n\t\t\tz1\n\t\t\t\tf3.txt"))
