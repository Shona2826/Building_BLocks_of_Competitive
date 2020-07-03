s = "2344f4"
res = 0
for i in range(len(s)):
	res = res*10 + (ord(s[i]) - ord('0'))
print(res)
