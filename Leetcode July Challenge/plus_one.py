class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=int("".join(map(str, digits)))
        s=s+1
        res = list(map(int, str(s)))
        return res