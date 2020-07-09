class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = format(x,'032b')
        b = format(y,'032b')
        count = 0
        for i in range(32):
            if a[i] != b[i]:
                count += 1
        return count
        