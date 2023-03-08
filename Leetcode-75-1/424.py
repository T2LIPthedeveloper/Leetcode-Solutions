class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # choose any char of string and change it to any other uppercase char
        # at most k times
        # return the length of the longest substring that contains the same
        # letter after the changes

        hashmap, result, start, end, maxCount = {}, 0, 0, 0, 0
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
            # update the maxCount
            maxCount = max(maxCount, hashmap[char])
            # if the number of characters that are not the most frequent
            while end - start + 1 - maxCount > k:
                # remove the first character from the hashmap
                hashmap[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
            # move the end pointer
            end += 1
        return result
    