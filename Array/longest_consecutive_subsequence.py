def longest(a):
	a.sort()
	ans = 0
	count = 0
	for i in range(len(a)):
		if i>0 and a[i] == a[i-1]+1:
			count+=1
		else:
			count = 1
		ans = max(ans,count)
	return ans

a = [1,9,3,10,4,20,2]
print(longest(a))