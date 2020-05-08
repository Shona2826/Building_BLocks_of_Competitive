a = 'LOVELEETCODE'
count = [0] * 256
for i in a:
	count[ord(i)] += 1
k =0
for i in a:
	if count[ord(i)] == 1:
		index = k
		break
	k+=1

print(index)