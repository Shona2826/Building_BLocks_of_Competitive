a = [1,2,3,4,5,6]
min_index  = 0
max_index = len(a) -1
max_ele = a[max_index] + 1
for i in range(len(a)):
	if i% 2 == 0:
		a[i] = a[i] + (a[max_index]%max_ele) * max_ele
		max_index -= 1
	else:
		a[i] = a[i] + (a[min_index] % max_ele) * max_ele
		min_index += 1
for i in range(len(a)):
	a[i] = a[i] // max_ele
print(a)
