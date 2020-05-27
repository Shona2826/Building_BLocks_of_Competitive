class Node:
	def __init__(self,data =0):
		self.data = 0
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def newNode(self,key):
		temp = Node(key)
		self.next = None
		return temp
	def rearrangeEvenOdd(self,head):
		if (self.head == None):
			return None
		odd = self.head
		even = self.head.next

		evenFirst = even
		while True:
			if odd == None or even == None or even.next == None:
				odd.next = evenFirst
				break
			odd.next = even.next
			odd = even.next

			if odd.next == None:
				even.next = None
				odd.next = evenFirst
				break
			even.next = odd.next
			even = odd.next
		return head
	def printlist(self, node):
		while (node != None):
			print(node.data, end = "")
			print("->", end = "")
			node = node.next
		print("NULL")
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

l1 = LinkedList()
l1.push(5)
l1.push(4)
l1.push(3)
l1.push(2)
l1.push(1)
l1.printlist(l1.head)
start = l1.rearrangeEvenOdd(l1.head)
l1.printlist(start)


