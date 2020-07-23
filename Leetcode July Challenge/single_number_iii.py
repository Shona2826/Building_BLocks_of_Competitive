class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            if d[nums[i]]==1:
                del d[nums[i]]
                
            else:
                d[nums[i]] += 1
                
        print(d)
        return d.keys()