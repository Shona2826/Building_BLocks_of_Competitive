class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        count = count.most_common(k)
        return [i[0] for i in count]