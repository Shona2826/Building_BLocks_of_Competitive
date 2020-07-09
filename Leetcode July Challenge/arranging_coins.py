class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((sqrt(8*n + 1)/2) - 0.5)
        
        