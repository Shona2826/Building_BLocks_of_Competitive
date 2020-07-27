class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None
	def push(self,new_data):
		new_node = Node(new_data)
		if self.head == None:
			self.head = new_node

		else:
			temp = self.head
			while temp.next:
				temp = temp.next

			temp.next = new_node
		new_node.next = None
	def detect_loop(self):
		temp = self.head
		s= set()
		while temp:
			if temp.data in s:
				print("loop detected")
				break
			s.add(temp.data)
			temp = temp.next


llist = Linkedlist() 
llist.push(10) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
#llist.push(50)
llist.detect_loop()