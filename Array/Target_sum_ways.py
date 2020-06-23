class Solution:
    def findTargetSumWays(self, nums,s):
    	result = 0
    	for i in range(len(nums)):
    		result += nums[i]

    	result -= s
    	
        