# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# def deserialize(aString):
# 	if aString == "" or aString is None: 
# 		return None
# 	else: 
# 		newString = aString.split(" ")
# 		print(newString)
# 		if newString[0] == "-1": 
# 			return None 
# 		else:
# 			newstr = ""
# 			newNode = Node(newString[0])
# 			for string in newString[1:]:
# 				newstr += string + " "
# 			newNode.left = deserialize(newstr)
# 			newNode.right = deserialize(newstr)


def removeWord(aString):
	if aString == "":
		return "",""
	else: 
		string = ""
		wordToUse = aString.split(" ")[0]
		rebuild = aString.split(" ")[1:]
		for s in rebuild:
			string += s + " "
		return wordToUse, string

def deserialize(aString): 
	curr, rest = removeWord(aString)
	if curr == "-1":
		return None
	else: 
		node = Node(curr)
		node.left = deserialize(rest)
		node.right = deserialize(rest)
		return node

def serialize(aNode):
	if aNode is None: 
		return "-1 "
	else:
		string = aNode.val + " "
		string += serialize(aNode.left)
		string += serialize(aNode.right)
		return string


node = Node('root', Node('left', Node('left.left')), Node('right'))

#             root
#            /    \ 
#          left   right
#         /
# left.left
# center left right 
# preorder 
# root left left.left -1 -1 -1 right -1 -1 
print(serialize(node))

# The following test should pass:
assert deserialize(serialize(node)).left.left.val == 'left.left'

# this one took forever, since I messed up the base case for deseralize. 
# serialize was quite simple, i overcomplicated the cases for deserialize.
# Brushed up on classes here.
 