class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        largest_sum = 0
        sum_total = 0
        l ={}
        for i in range(len(nums)):
            if nums[i] == 1:
                sum_total += 1
            else:
                sum_total -= 1
            if sum_total == 0:
                largest_sum = max(largest_sum,i+1)
            else:
                if sum_total in l:
                    j = l[sum_total]
                    largest_sum = max(i-j,largest_sum)
                else:
                    l[sum_total] = i
                
        return largest_sum
        
        