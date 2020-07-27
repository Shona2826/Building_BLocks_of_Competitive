
def find_min(a,low,high):
	
	if high<low:
		return a[0]
	if high == low:
		return a[low]
	mid = (high+low)//2
	if mid < high and a[mid+1] < a[mid]:
		return a[mid+1]

	if mid > low and a[mid] < a[mid-1]:
		return a[mid]

	if a[high]>a[mid]:
		return find_min(a,low,mid-1)
	return find_min(a,mid+1,high)

a = [10,20,30,40,5,7]
low = 0
high = len(a)-1
print(find_min(a,low,high))