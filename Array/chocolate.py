a = [7,3,2,4,9,12,56]
m = 3
a.sort()
min_diff = a[-1]
i =0
while i+m-1 < len(a):
	diff = a[i+m-1] - a[i]
	if diff < min_diff:
		min_diff = diff
	i+=1
print(min_diff)