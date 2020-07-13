class Node:
	def __init__(self,key):
		self.key = key
		self.right = None
		self.left = None
def sum_root_to_leaf(root,partial_path_sum = 0):
	if not root:
		return 0
	partial_path_sum = partial_path_sum*10 +root.key
	print(root.key)
	if not root.left and not root.right:
		return partial_path_sum

	return(sum_root_to_leaf(root.left,partial_path_sum) + sum_root_to_leaf(root.right,partial_path_sum))

root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print(sum_root_to_leaf(root))
