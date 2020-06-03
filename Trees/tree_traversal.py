class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

def tree_traversal(root):
	if root:
		print('Preorder: %d' % root.data)
		tree_traversal(root.left)
		print('Inorder : %d' % root.data)
		tree_traversal(root.right)
		print('Postorder: %d' % root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tree_traversal(root)
