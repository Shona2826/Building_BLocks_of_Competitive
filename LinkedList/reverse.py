class Node:
	def __init__(self,data=0):
		self.data = data
		self.next = None
class LinkedList():
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

	def reverse(self):
		current= self.head
		prev = None
		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev
	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.printlist()
list1.reverse()
list1.printlist()



