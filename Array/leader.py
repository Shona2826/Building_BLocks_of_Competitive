a = [16,17,4,3,5,2]
count = 0
for i in range (len(a)):
	for j in range(i+1,len(a)):
		if a[i] < a[j]:
			count = 1
			break
	if count == 1:
		count = 0
		continue
	else:
		print(a[i])