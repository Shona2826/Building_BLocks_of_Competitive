num = "1432219"
k = 3
def removeKDigits(num,k):
	if k == len(num):
		return "0"
	if k > len(num):
		return "-1"
	for j in range(k):
		i =0
		while i < len(num) - 1 and num[i] <= num[i+1]:
			i += 1
		print(i)
		num = num.replace(num[i],'')
		print(num)
	while len(num) > 0 and num[0] == '0':
		num.replace(num[0],'')
	if len(num) == 0:
		return "0"
	return num

print(removeKDigits(num,k))