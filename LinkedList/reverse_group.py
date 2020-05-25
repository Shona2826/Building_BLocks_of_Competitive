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

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
	def rotate_group(self,head,k):
		cur = head
		prev = None
		next = None
		count = 1
		while count < k and cur is not None:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
			count +=1
		if next is not None:
			head.next = self.rotate_group(next,k)
		return prev
list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
#list1.printlist()
list1.rotate_group(list1.head,3)
list1.printlist()
		


