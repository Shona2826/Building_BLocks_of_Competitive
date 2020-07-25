def rightrotate(arr,n,out,cur):
	temp = arr[cur]
	for i in range(cur,out,-1):
		arr[i] = arr[i-1]
	arr[out] = temp
	return arr

def rearrange(arr,n):
	out = -1
	for i in range(n):
		if out >= 0:
			if ((arr[i] >= 0  and arr[out] < 0) or (arr[i] < 0 and arr[out] >= 0)):
				arr = rightrotate(arr,n,out,i)
				if i-out > 2:
					out += 2
				else:
					out = -1


		if out == -1:
			if ((arr[i] >= 0 and i%2 == 0) or (arr[i] < 0 and i %2 == 1)):
				print(out)
				out = i   
				print(out)     
	return arr

a = [-5,-2,5,2,4,7,1,8,0,-8]

print(rearrange(a,len(a)))