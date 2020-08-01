def max_sum(a):
	inc = a[0]
	exc = 0
	for i in range(1,len(a)):
		temp = inc
		inc = max(inc,exc+a[i])
		exc = temp
		print(inc)

	return inc

a = [75,105,120,75,90,135]
print(max_sum(a))