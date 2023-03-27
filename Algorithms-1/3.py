class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find length of longest substring without repeating letters
        # sliding window
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 0
        j = 1
        max_len = 1
        while j < n:
            if s[j] not in s[i:j]:
                j += 1
                max_len = max(max_len, j-i)
            else:
                i += 1
        return max_len
        