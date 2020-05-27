class Node:
	def __init__(self,data = 0):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def push(self,new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node
			new_node.next = None
	def kth_node(self,l,k):
		temp = self.head
		count = 1
		if l < k:
			return "-1"
		while temp and count < l-k+1:
			temp = temp.next
			count +=1
		return temp.data

list1 = LinkedList()
list1.push(10)
list1.push(5)
list1.push(100)
list1.push(5)

print(list1.kth_node(4,4))




