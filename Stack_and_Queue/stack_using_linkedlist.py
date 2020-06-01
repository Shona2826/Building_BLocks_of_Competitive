class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None
	def isempty(self):
		if self.head == None:
			return True
		else:
			return False
	def push(self,data):
		if self.head == None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node
	def pop(self):
		if self.isempty():
			return None
		else:
			popnode = self.head
			self.head = self.head.next
			popnode.next = None
			return popnode.data

	def peek(self):
		if self.isempty():
			return None

		else:
			return self.head.data
	def display(self):
		iternode = self.head
		if self.isempty():
			print("Stack Underflow")
		else:
			while iternode != None:
				print(iternode.data,"->",end = " ")
				iternode = iternode.next
			return 

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.pop()
s.display()