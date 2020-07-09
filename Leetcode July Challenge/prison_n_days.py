class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = []
        while True:
            cells = [0] + [1 if cells[i-1] == cells[i+1] else 0 for i in range(1,len(cells)-1)] + [0]
            #print(cells)
            if cells in seen:
                break
            seen.append(cells)
        
        return seen[(N-1) % (len(seen))]
                
        