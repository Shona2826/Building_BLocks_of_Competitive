class Node:
	def __init__(self,data =0):
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
			while(temp.next is not None):
				temp = temp.next
			temp.next = new_node
			new_node.next = None
	def rotate(self,k):
		if k == 0:
			return 
		cur = self.head
		count = 1
		while count < k and cur != None:
			cur = cur.next
			count +=1
		if cur == None:
			return
		kNode = cur
		while cur.next is not None:
			cur = cur.next
		cur.next = self.head
		self.head =  kNode.next
		kNode.next = None

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp= temp.next


list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.printlist()
list1.rotate(3)
list1.printlist()


