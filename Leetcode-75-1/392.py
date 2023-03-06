class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            curr = t.find(ch)
            if curr == -1: #means character couldn't be found
                return False
            t = t[curr+1:] #ensures order is maintained
        return True

#Main issue is maintaining order, which is solved by reducing the length of the target string.