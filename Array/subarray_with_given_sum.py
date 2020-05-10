a = [1,2,3,6,5,6,7,8]
value = 17
sum_value = 0
count = 0
for i in range(len(a)):
	for j in range(i,len(a)):
		sum_value += a[j]
		if sum_value < value:
			continue
		if sum_value >= value:
			b = j
			break
	if sum_value == value:
		count = 1
		print(i,b)
		break
	sum_value = 0
if count == 1:
	print("yes")
else:
	print("no")
