a = [1,2,3,4,5]
k = 3
i = 0
n = len(a)
while i<n:
	left = i
	right = min(i+k-1,n-1)
	while(left<right):
		a[left],a[right] = a[right] , a[left]
		left+=1
		right-=1
	i+=k
		
print(a)
