def is_linked_list_palindrome(L):
	slow=fast=L
	while fast and fast.next:
		fast,slow = fast.next.next,slow.next
	first_half_iter,second_half_iter = L,reverse_linked_list(slow)
	while second_half_iter and first_half_iter:
		if second_half_iter != first_half_iter:
			return False
		second_half_iter,first_half_iter = second_half_iter.next,first_half_iter.next
	return True