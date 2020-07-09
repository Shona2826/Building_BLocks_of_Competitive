from queue import Queue
class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None
def level(root):
	q = []
	q.append(root)
	while q:
		for _ in range(len(q)):
			temp = q.pop()
			print(temp.data,end = " ")
		if temp.right:
			q.append(temp.right)
		if temp.left:
			q.append(temp.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
level(root)
