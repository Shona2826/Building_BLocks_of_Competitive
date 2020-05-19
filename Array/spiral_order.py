a = [[1,2,3,4],
	 [5,6,7,8],
	 [9,10,11,12],
	 [13,14,15,16]]

def matrix_in_spiral_order(a):
	def matrix_layer_in_clockwise(offset):
		if offset == len(a)-offset-1:
			spiral_ordering.append(a[offset][offset])
			return 
		spiral_ordering.extend(a[offset][offset:-1-offset])
		print(spiral_ordering)
		spiral_ordering.extend(list(zip(*a))[-1-offset][offset:-1-offset])
		print(spiral_ordering)
		spiral_ordering.extend(a[-1-offset][-1-offset:offset:-1])
		print(spiral_ordering)
		spiral_ordering.extend(list(zip(*a))[offset][-1-offset:offset:-1])
		print(spiral_ordering)

	spiral_ordering = []
	for offset in range((len(a) + 1)//2):
		matrix_layer_in_clockwise(offset)
		print(spiral_ordering)
	return spiral_ordering

print(matrix_in_spiral_order(a))