class Node:
	def __init__(self,data=0):
		self.data = data
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
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node
			new_node.next = None
	def swap(self):
		temp = self.head
		if temp is None:
			return
		while temp is not None and temp.next is not None:
			temp.data,temp.next.data = temp.next.data,temp.data
			temp = temp.next.next

	def printlist(self):
		temp = self.head
		while temp:
			print(temp.data,end = " ")
			temp = temp.next
		
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.printlist()
list1.swap()
list1.printlist()
