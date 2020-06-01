def NGE(arr):
	for i in range(0,len(arr)):
		next = -1
		for j in range(i+1,len(arr)):
			if arr[i] < arr[j]:
				next = arr[j]
				break
		print(str(arr[i]) + " -- " + str(next))

arr =[1,2,3,1,4]
NGE(arr)