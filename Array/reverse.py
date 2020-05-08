x = -123
num = 0
while x> 0:
	r = x % 10
	num = num* 10 + r
	x = x//10
if x < 0:
	x = -x
	while x> 0:
		r = x % 10
		num = num* 10 + r
		x = x//10
	num = -num
print(num)
