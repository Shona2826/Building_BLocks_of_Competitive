nums = [0,1,2,3,4]
index = [0,1,2,2,1]
target =list()
for i, j in zip(nums,index):
	target.insert(j,i)
print(target)