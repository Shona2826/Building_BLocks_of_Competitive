class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        points.sort(key=lambda nums: math.sqrt(nums[0]**2 + nums[1]**2 ))
        return points[:K]
        