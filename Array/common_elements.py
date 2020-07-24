def common(a,b,c):
	res = []
	for i in list(set(a)):
		if i in b and i in c:
			res.append(i)

	return res
a = [1,5,10,20,40,80,20]
b = [6,7,20,80,100]
c = [3,4,15,20,30,70,80,120]
print(common(a,b,c))
