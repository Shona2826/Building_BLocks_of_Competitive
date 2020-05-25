def max_product(arr):
	count = 0
	prod = 1
	for i in range(len(arr)):
		if arr[i] < 0:
			count += 1
	if count% 2 == 0:
		for i in range(len(arr)):
			if arr[i] == 0:
				continue
			prod *= arr[i]
		return prod
	elif count == 1:
		for i in range(len(arr)):
			if arr[i] <= 0:
				continue
			else:
				prod *= arr[i]
		return prod
	else:
		for i in range(len(arr)):
			if arr[i] == 0:
				continue
			prod *= arr[i]
		k = max([n for n in arr if n<0])
		prod = prod // k
		return prod

print(max_product([-5,-2,-3,0,0,5]))

