
a = [1,3,4,2,4,4]
flag = True
for i in range(1,len(a)):
	if a[i] >= a[i-1]:
		continue
	if flag:

		if i >= 2 and a[i-2] > a[i]:
			a[i] = a[i-1]
			flag = False

		else:
			a[i-1] = a[i]
			flag = False
print(a)