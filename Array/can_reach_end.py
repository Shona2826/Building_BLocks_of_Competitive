def can_reach_end(a):
	furthest_reach_so_far,last_index = 0,len(a) -1
	i =0 
	while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
		furthest_reach_so_far = max(furthest_reach_so_far, a[i] + i)
		i += 1
		print(furthest_reach_so_far)
	return furthest_reach_so_far >= last_index

a = [3,3,1,0,2,0,1]
print(can_reach_end(a))