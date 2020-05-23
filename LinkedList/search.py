class ListNode:
	def __init__(self,data = 0,next_node = None):
		self.data = data
		self.next = next_node
	#search 
	def search_list(L,key):
		while L and L.data != key:
			L = L.next
		return L
	#insert a newnode after node.
	def insert_node(node,new_node):
		new_node.next = node.next
		node.next = new_node
	#delete
	def delete_after(node):
		node.next = node.next.next 

def merge_two_sorted_lists(L1,L2):
	dummy_head = tail = ListNode()
	while L1 and L2:
		if L1.data < L2.data:
			tail.next,L1= L1,L1.next
		else:
			tail.next,L2 = L2,L2.next
		tail = tail.next
	return dummy_head.next
def reverse_sublist(L,start,finish):
	dummy_head = sublist_head = ListNode(0,L)
	for _ in range(1,start):
		sublist_head = sublist_head.next
	sublist_iter = sublist_head.next
	for _ in range(finish-start):
		temp = sublist_iter.next
		sublist_iter.next,temp.next,sublist_head.next = (temp.next,sublist_head.next,temp)
	return dummy_head.next


