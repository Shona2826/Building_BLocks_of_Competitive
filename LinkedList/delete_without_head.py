class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
def push(head_ref,new_data):
	new_node = Node(new_data)
	new_data.data = new_data
	new_node.next = head_ref
	head_ref = new_node
	return head_ref

def printList(head):
	temp = head
	while temp != None:
		print(temp.data,end = ' ')
		temp = temp.next

def deleteNode(node_ptr):
	temp = node_ptr.next
	node_ptr.data = temp.data
	node_ptr.next = temp.next

if __name__ == '__main__':
	head = None
	head = push(head,1)
	head = push(head,4)
	head = push(head,1)
	head = push(head,12)
	head = push(head,1)

	print("Before deleting ")
	printList(head)

	deleteNode(head)
	print("After deleting")
	printList(head)