class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def inorder(temp):
	if not temp:
		return
	inorder(temp.left)
	print(temp.data,end = " ")
	inorder(temp.right)

def deletion(root,key):
	
root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

inorder(root)

key = 11
deletion(root,key)
print()
inorder(root)