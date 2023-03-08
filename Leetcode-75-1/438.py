class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #result is a list of integers with start indices that are anagrams of p
        hashmap, result, pLen, sLen = {}, [], len(p), len(s)
        #create a hashmap of the characters in p
        if len(p) > len(s):
            return result
        for char in p:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        #create a hashmap of the characters in the first pLen characters of s
        for i in range(pLen):
            if s[i] in hashmap:
                hashmap[s[i]] -= 1
            else:
                hashmap[s[i]] = -1
        #check if the first pLen characters of s are an anagram of p
        if all(value == 0 for value in hashmap.values()):
            result.append(0)
        #iterate through the rest of the characters in s
        for i in range(pLen, sLen):
            #remove the first character from the hashmap
            if s[i-pLen] in hashmap:
                hashmap[s[i-pLen]] += 1
            else:
                hashmap[s[i-pLen]] = 1
            #add the new character to the hashmap
            if s[i] in hashmap:
                hashmap[s[i]] -= 1
            else:
                hashmap[s[i]] = -1
            #check if the new characters are an anagram of p
            if all(value == 0 for value in hashmap.values()):
                result.append(i-pLen+1)
        return result
    

    