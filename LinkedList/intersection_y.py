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

	def getIntersectionPoint(self,headA,headB):
		if headA == None or headB == None:
			return None 
		alen = 0
		blen = 0
		a = headA
		while a:
			alen += 1
			a = a.next
		b = headB
		while b:
			blen += 1
			b = b.next
		a = headA
		b = headB
		while alen > blen:
			a = a.next
			alen -= 1
		while blen > alen:
			b = b.next
			blen -= 1
		while a != b:
			a = a.next
			b = b.next
		return a