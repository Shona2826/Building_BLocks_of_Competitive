class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,0,len(nums)-1
  
        while k >= j:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                
            elif nums[j] == 1:
                j += 1
                
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
          
                
        return nums
 
s = Solution()
l = [2,0,1]                
a = s.sortColors(l)
print(a)