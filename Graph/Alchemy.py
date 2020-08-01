def solve(val):
	
	if len(val) == 1:
		return 1
	if len(val) == 2:
		return 0
	
	if len(val)%2 == 0:
		return 0
	while len(val) > 1:
		a = val[:3]
		res1 = a.count(0)
		res2 = a.count(1)
		if res1 == 0 or res2 == 0:
			return 0
		val = val[3:]
		if res1>res2:
			val.insert(0,0)
		else:
			val.insert(0,1)
		if len(val) == 1:
			return 1

t = int(input())
while t:
	n = int(input())
	val = input()[:n]
	val2  = list(val)
	val3= []
	for c in val2:
		num = ord(c)-65
		val3.append(num)
	a = solve(val3)
	if a == 0:
		print("Case #N")
	else:
		print("case Y")
	t -= 1

	

