a = [1,3,5,2,2]
left = 0
right = len(a)-1
sum1 = 0
total_sum = sum(a)

for i,num in enumerate(a):
	total_sum -= num
	if sum1 == total_sum:
		print(i)
	sum1 += num
print("done")