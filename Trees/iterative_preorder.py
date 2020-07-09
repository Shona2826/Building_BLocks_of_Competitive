class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None
def preorder(root):
	stack = []
	stack.append(root)
	while stack:
		a = stack.pop()
		print(a.data,end = " ")
		if a.right is not None:
			stack.append(a.right)
		if a.left is not None:
			stack.append(a.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
preorder(root)
