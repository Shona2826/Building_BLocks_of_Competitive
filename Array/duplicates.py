import collections
def duplicate(a):
	print([item for item,count in collections.Counter(a).items() if count == 1])
	
	

a = [2,3,1,2,3]
duplicate(a)

