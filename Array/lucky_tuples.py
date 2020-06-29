def lucky(a):
	if len(a) < 3:
		return 0
	else:
		res = 0
		result = [0 for _ in range(len(a))]
		for i in range(1,len(a)):
			j=0
			for j in range(0,i):
				if a[i] % a[j] == 0:
					result[i] += 1
					res += result[j]
		return res

a = [1,2,3,4,5,6]
b = lucky(a)
print(b)
