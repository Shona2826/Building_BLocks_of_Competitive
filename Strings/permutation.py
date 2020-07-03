def permute(a,l,r):
	if 1 == r:
		return ''.join(a)
	else:
		for i in range(1,r+1):
			a[l],a[i] = a[i],a[l]
			permute(a,l+1,r)
			a[l],a[i] = a[i],a[l]

s = "SUMAN"
n = len(s)
a = list(s)
permute(a,0,n-1)