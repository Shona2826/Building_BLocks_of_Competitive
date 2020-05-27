class Node:
	def __init__(self,data=0):
		self.data = data
		self.next = None
def newNode(key):
	temp = Node(key)
	temp.data = key
	temp.next = None
	return None
def printList(node):
	while node != None:
		print(node.data,end = " ")
		node = node.next
def merge(h1,h2):
	if h1 == None:
		return h2
	if h2 == None:
		return h1
	if h1.data < h2.data:
		h1.next = merge(h1.next,h2)
		return h1
	else:
		h2.next = merge(h1,h2.next)
		return h2

if __name__=='__main__':
	head1 = newNode(1)
	head1.next = newNode(3)
	head1.next.next = newNode(5)

	head2 = newNode(0)
	head2.next = newNode(2)
	head2.next.next = newNode(4)

	mergedhead = merge(head1,head2)
	printList(mergedhead)