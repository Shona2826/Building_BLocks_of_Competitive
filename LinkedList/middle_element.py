class Node:
	def __init__(self,data=0):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def middle(self):
		slow_p =self.head
		fast_p = self.head

		if self.head is not None:
			while fast_p is not None and fast_p.next is not None:
				if fast_p.next.next == None:
					fast_p = fast_p.next
				else:
						fast_p= fast_p.next.next
				slow_p = slow_p.next
			print("Middle element is: ",slow_p.data)

list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.middle()


