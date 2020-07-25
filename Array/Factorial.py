def factorial(a):
	f = [0 for i in range(a+1)]
	f[0] = 1
	f[1] = 1
	for i in range(2,a+1):
		f[i] = f[i-1] * i
	return f[-1]

a = 10
print(factorial(a))