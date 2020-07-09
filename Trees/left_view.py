class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def maxdepth(root):
	if root is None:
		return 0
	else:
		l = maxdepth(root.left)
		r = maxdepth(root.right)
		if l > r:
			return l+1
		else:
			return r+1

def left_view(root):
	m = maxdepth(root)
	#print(m)
	l = [0]*m
	#print(l)
	stack = []
	stack.append(root)
	level = 1
	while stack and level <= m:
		temp = stack.pop()
		if l[level-1] == 0:
			print(temp.data,end = " ")
			l[level-1] = 1
		level += 1
		if temp.right:
			stack.append(temp.right)
		if temp.left:
			stack.append(temp.left)
		if temp.left is None and temp.right is None:
			level -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
left_view(root)

