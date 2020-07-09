class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

INT_MAX = 4294967296
INT_MIN = -4294967296

def bst(root,minx,maxx):
	if root is None:
		return True
	if root.data < minx or root.data > maxx:
		return False
	return bst(root.left,minx,root.data - 1) and bst(root.right,root.data+1,maxx)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
if (bst(root,INT_MIN,INT_MAX)):
	print("Is BST")
else:
	print("Not a BST")
