def count_bits(x):
	no_of_bits = 0
	while x:
		no_of_bits += x & 1
		x = x>>1

	print(no_of_bits)
	return 0

count_bits(5)