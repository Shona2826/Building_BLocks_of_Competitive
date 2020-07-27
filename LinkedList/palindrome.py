class Node:
	def __init__(self,new_data):
		self.data = new_data
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

	def ispalindrome(self,string):
		return (string == string[::-1])

	def palindrome(self):
		node = self.head
		temp =[]
		while node is not None:
			temp.append(node.data)
			node = node.next
		string = "".join(str(temp))
		return self.ispalindrome(string)

l = Linkedlist()
l.push(1)
l.push(2)
l.push(1)
l.push(4)
l.push(5)
print(l.palindrome())