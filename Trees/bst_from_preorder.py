class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def bstfrompreorder(root):
	if not root:
		return None
	
