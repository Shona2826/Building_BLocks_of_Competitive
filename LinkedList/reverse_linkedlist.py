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
	def reverse(self):
		curr=self.head
		prev = None
		nexts = None
		while curr is not None:
			nexts = curr.next
			curr.next = prev
			prev = curr
			curr = nexts
		self.head = prev

	def printlist(self):
		temp = self.head
		while temp.next:
			print(temp.data,"-->",end = " ")
			temp = temp.next
		print(temp.data)

node = Linkedlist()
node.push(1)
node.push(2)
node.push(3)
node.push(4)
node.push(5)
node.reverse()
node.printlist()
