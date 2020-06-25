class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        sol = []
        while a < len(A) and b < len(B):
            if(B[b][0] <= A[a][1] and A[a][0] <= B[b][1]):
                low_val = max(A[a][0],B[b][0])
                high_val = min(A[a][1],B[b][1])
                sol.append((low_val,high_val))
                
            if A[a][1] > B[b][1]:
                b+=1
            else:
                a+=1
                
        return sol