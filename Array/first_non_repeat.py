nums = [1,2,2,3,3,4,4,8,8]
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high)//2
    print(mid)
    if mid == 0 or mid == (len(nums)-1):
        break
    if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
        print(nums[mid])
        break
    elif (nums[mid] == nums[mid-1] and mid%2 != 0) or (nums[mid] == nums[mid+1] and mid%2 == 0):
        low = mid+1    
    elif(nums[mid] == nums[mid-1] and mid%2 == 0) or (nums[mid] == nums[mid+1] and mid %2 != 0):
        hi = mid - 1
print(nums[mid])