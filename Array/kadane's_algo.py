def kadane(a):
	max_ending_here = 0
	max_so_far = 0
	for i in range(len(a)):
		max_ending_here += a[i]
		if max_ending_here < 0:
			max_ending_here = 0
		if max_ending_here > max_so_far:
			max_so_far = max_ending_here

	return max_so_far
a = [1,2,3,-2,5]
print(kadane(a))

