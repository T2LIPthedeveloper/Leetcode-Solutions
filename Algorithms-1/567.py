class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check if s2 contains permutation of s1
        # sliding window
        if len(s2) < len(s1): return False
        if len(s1) == 0: return True
        if len(s2) == 0: return False
        i = 0
        j = len(s1)
        while j <= len(s2):
            if sorted(s2[i:j]) == sorted(s1):
                return True
            i += 1
            j += 1
        return False
        
        

