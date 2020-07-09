class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

def postorder(root):
	s1 = []
	s2 = []
	s1.append(root)
	while s1:
		a = s1.pop()
		s2.append(a)

		if a.left is not None:
			s1.append(a.left)
		if a.right is not None:
			s1.append(a.right)
	while s2:
		a = s2.pop()
		print(a.data,end = " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
postorder(root)
