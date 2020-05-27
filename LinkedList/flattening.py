class Node:
	def __init__(self,data = 0,next = None,down = None):
		self.data = 0
		self.next = next
		self.down = down
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
	def createVerticalList(self,head,A):
		for key in A:
			head = Node(key,head)
		return head

	def SortedMerge(a,b):
		if a is None:
			return b
		elif b is None:
			return a
		if a.data <= b.data:
			result = a
			result.down = self.SortedMerge(a.down,b)
		else:
			result = b
			result.down = self.SortedMerge(a,b.down)

		return result


	def flatten(self,head):
		curr = head
		while curr:
			temp = curr
			while temp.down:
				temp = temp.down
			temp.down = curr.next
			curr = curr.next

	def frontBackSplit(self,source):
		if source is None or source.down is None:
			return source,None
		(slow,fast) = (source,source.down)
		while fast:
			fast = fast.down
			if fast:
				slow = slow.down
				fast = fast.down

			A = (source,slow.down)
			slow.down = None
			return A

	def MergeSort(self,head):
		if head is None or head.down is None:
			return head
		front,back = self.frontBackSplit(head)
		front = self.MergeSort(front)
		back = self.MergeSort(back)
		return self.SortedMerge(front,back)


first = [8,6,4,1]
second = [7,3,2]
third = [9,5]
fourth = [12,11,10]

list1 = LinkedList()
head = list1.createVerticalList(None,first)
head.next = list1.createVerticalList(head.next,second)
head.next.next = list1.createVerticalList(head.next.next,third)
head.next.next.next = list1.createVerticalList(head.next.next.next,fourth)
list1.flatten(head)
list1.MergeSort(head)
list1.printlist(head)



















































