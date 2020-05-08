a = [2,4,5,8,9]
b = [3,1,0,6,10]

def merge(a,b,m,n):
	for i in reversed(range(n-1)):
		last = a[m-1]
		j = m-2
		while j>=0 and a[j] > b[i]:
			a[j+1] = a[j]
			j -= 1
			print(a)
		if (j != m-2 or last > b[i]):
			a[j+1] = b[i]
			b[i] = last
			print(a)
			print(b)

merge(a,b,len(a),len(b))