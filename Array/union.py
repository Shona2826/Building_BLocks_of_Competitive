def union(a,b):
	final = list(set(a) | set(b))
	return final

a = [85,25,1,1,32,54,6]
b = [85,2]
print(union(a,b))

