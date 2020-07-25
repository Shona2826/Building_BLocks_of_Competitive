def max_product(a):
	max_so_far = 1
	max_ending_here = 1
	min_ending_here = 1
	flag = 0
	for i in range(len(a)):
		if a[i] > 0:
			max_ending_here *= a[i]
			min_ending_here = min(min_ending_here*a[i],1)
			flag = 1
		elif a[i] == 0:
			max_ending_here= 1
			min_ending_here = 1
		else:
			temp = max_ending_here
			max_ending_here = max(min_ending_here*a[i],1)
			min_ending_here = temp*a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
	if flag == 0 and max_so_far == 1:
		return 0
	return max_so_far


a = [6,-3,-10,0,2]
print(max_product(a))
