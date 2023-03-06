class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i] #adding char to dictionary if it's not there
            if t[i] not in dict2:
                dict2[t[i]] = s[i] #corresponding char
            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]: #both chars should map to each other if it is isomorphic
                return False
        return True