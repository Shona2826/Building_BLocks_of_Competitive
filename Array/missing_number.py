a = [1,2,3,4,5,6,7,8,10]
a.sort()
for i in range(len(a)-1):
	if a[i+1] - a[i] == 1:
		continue
	else:
		print(i+2)