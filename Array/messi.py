t = int(input())
while t:
	n = int(input())
	l = list(map(int,input().strip().split()))
	k = int(input())
	s = 0
	l.sort()
	print(l)
	for i in range(k):
		s += l[i]
	for j in range(k,n):
		s = s+l[k-1]
		print(s)
		t = t-1
