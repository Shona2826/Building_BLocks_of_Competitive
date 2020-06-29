s = list(input())
l = []
for i in s:
	p = (ord(i)-96)+ord(i)
	g = p%26
	k = chr(96+g)
	l.append(k)
print("".join(l))