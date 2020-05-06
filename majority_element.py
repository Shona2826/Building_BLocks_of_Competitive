import collections
def majority(a):
	count = collections.Counter(a)
	#65s`73333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333print(count)
# find the index
	for ch in a:
		
		if count[ch] > len(a)//2:
			#print("suman")
			return ch     
	return -1

a = [2,2,1,1,1,2,2]
print(majority(a))