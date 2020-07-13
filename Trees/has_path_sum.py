class Node:
	def __init__(self,key):
		self.data = key
		self.right = None
		self.left = None

def has_path_sum(root,remaining_weight):
	if not root:
		return False
	if not root.left and not root.right:
		return remaining_weight == root.data

	return (has_path_sum(root.left,remaining_weight-root.data)) or has_path_sum(root.right,remaining_weight-root.data)


root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print(has_path_sum(root,11))