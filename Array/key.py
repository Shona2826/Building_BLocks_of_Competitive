a =[1,2,3,3,1,5,6,7,7]
key = 1
if not a:
	print(0)
write_index = 1
for i in range(1,len(a)):
	if a[write_index-1] != key:
		a[write_index] = a[i]
		write_index += 1

print(a)
