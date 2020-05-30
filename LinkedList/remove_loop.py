class Node:
	def __init__(self,data = 0):
		self.data = 0
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self,new_data):
		new_node = Node(new_data)
		if self.head == None:
			self.head = new_node
		else:
			temp = self.head
			while(temp.next is not None):
				temp = temp.next
			temp.next = new_node
	def detect_loop(self):
		s = set()
		temp = self.head
		while temp:
			if temp in s:
				self.remove_loop(temp)
				break
			s.add(temp)
			temp = temp.next

	def remove_loop(self,loop_node):
		ptr1 = self.head
		while 1:
			ptr2 = loop_node
			while ptr2.next != loop_node and ptr2.next != ptr1:
				ptr2 = ptr2.next
			if ptr2.next == ptr1:
				break
			ptr1 = ptr1.next
		ptr2.next = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

llist = LinkedList() 
llist.push(10) 
llist.push(4) 
llist.push(15) 
llist.push(20) 
llist.push(50) 
  
# Create a loop for testing 
llist.head.next.next.next.next.next = llist.head.next.next
llist.printList() 
llist.detectAndRemoveLoop() 
llist.printList() 
