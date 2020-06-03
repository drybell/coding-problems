# This problem was asked by Google.

# A unival tree (which stands for "universal value") 
# is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# In this example all the 1 leaves have NULL left and right children
# and theres a copy of the 0 1 0 0 1 0 from the right subtree of the root 
# All Nodes under it are the same, for every root of the tree.
# So there will be a lot of leaf-to-root traversal 

# maybe make a list of all subtrees then iterate on that?

from may92020/problem3att1 import serialize, deserialize  

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# For every subtree, find another one in the list
# and add to the counter 
def uniVal(subtreeList):


# Start with root, traverse the whole tree
# and gather every node. then move the root node 
# to the left, do it again, then the right, do it again.

def allSubtrees(aNode):
	subtrees = []
	if aNode == None: 
		ret
	temprootleft = aNode.left
	temprootright = aNode.right 


node = Node('root', Node('left', Node('left.left')), Node('right'))

