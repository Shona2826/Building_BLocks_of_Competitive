class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        
        target_len = len(s1)
        
        i = 0
        
        for j, c in enumerate(s2):
            
            if counter[c] > 0:
                target_len -= 1
                
            counter[c] -= 1
        
            
            while target_len==0:
                
                if len(s1) == (j-i+1):
                    return True
                
                counter[s2[i]] += 1
                if counter[s2[i]] > 0:
                    target_len += 1
            
                
                i+=1
                
        return False