def kth_node_binary_tree(tree,k):
	while tree:
		left_size = tree.left.size if tree.left else 0
		if left.size +1 < k:
			k = k- (left_size+1)
		elif left_size == k-1:
			return tree
		else:
			tree = tree.left

	return None 

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right  = Node(5)

print(kth_node_binary_tree(root,4))