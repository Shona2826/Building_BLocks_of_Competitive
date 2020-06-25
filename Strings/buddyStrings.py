class Solution:
	def buddyStrings(self,A,B):
		if len(A) < 2:
			return False
		if len(A) != len(B):
			return False
		diff = [[a,b] for a,b in zip(A,B) if a!= b]
		if len(diff) not in [0,2]:
			return False
		if len(diff) == 0:
			count = set()
			for letter in A:
				if letter in count:
					return True
				count.add(letter)
			return False
		return (diff[0][0] == diff[1][1]) and (diff[0][1] == diff[1][0])

