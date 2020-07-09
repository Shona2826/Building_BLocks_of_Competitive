class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None
def inorder(root):
	stack = []
	current = root
	done = 0
	
	while True:
		if current is not None:
			stack.append(current)
			current = current.left
		elif stack:
			current = stack.pop()
			print(current.data,end = " ")
			current = current.right
		else:
			break
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
inorder(root)
