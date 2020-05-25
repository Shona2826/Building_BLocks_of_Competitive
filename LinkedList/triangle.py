def coordinates(x,y):
	res = (x*(x+1))//2
	if y == 1:
		return res
	else:
		res = res + ((x+y-1)*(x+y-2))//2 - (x*(x-1))//2
		return res
print(coordinates(100000,100000))