a = [-1,-2,3,4,5,-1,7]
max_ending_here, max_so_far = 0,0
for i in range(len(a)):
	max_ending_here += a[i]
	if max_ending_here < 0:
		max_ending_here = 0
	if max_so_far < max_ending_here:
		max_so_far = max_ending_here
print(max_so_far)