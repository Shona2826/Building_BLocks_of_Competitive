class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        t1,t2,t3 = 0,0,0
        ugly = [0] * n
        ugly[0] = 1
        for i in range(1,n):
            ugly[i] = min(ugly[t1]*2, ugly[t2]*3, ugly[t3]*5)
            if ugly[i] == ugly[t1]*2: t1 += 1
            if ugly[i] == ugly[t2]*3: t2 += 1
            if ugly[i] == ugly[t3]*5: t3 += 1
        
        return ugly[n-1]