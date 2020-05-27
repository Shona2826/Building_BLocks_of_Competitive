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
			new_node.next = None

	def detectLoop(self):
		s = set()
		temp = self.head
		while temp:
			if temp in s:
				return True
			s.add(temp)
			temp = temp.next
		return False

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
llist.head.next.next.next.next = llist.head; 
if llist.detectLoop():
	print("Loop Found")
else:
	print("No Loop")