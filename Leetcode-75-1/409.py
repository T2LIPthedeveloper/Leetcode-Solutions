class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Longest palindrome (case sensitive) with characters given
        chars = {

        }
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1
        # now we have a dictionary of characters and their frequencies
        # we can use this to find the longest palindrome
        # we can use the fact that a palindrome can have at most one character with an odd frequency
        # if there is an odd frequency character, we can use it as the middle character of the palindrome
        odd_value_counter = 0
        for count in chars.values():
            if count % 2 == 1:
                odd_value_counter += 1
        
        if odd_value_counter <= 1:
            return len(s)
        else:
            return len(s) - odd_value_counter + 1
                
