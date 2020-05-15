a = [1,2,3,5,1,6,5,7,9,0]
pivot = 3
b = a[pivot]
smaller = 0
for i in range(len(a)):
	if a[i] < b:
		a[i],a[smaller] = a[smaller] ,a[i]
		smaller += 1
	#print(a)
larger = len(a) -1
for i in reversed(range(len(a))):
	if a[i] < b:
		break
	elif a[i] > b:
		a[larger],a[i] = a[i],a[larger]
		larger -=1
	print(a)
