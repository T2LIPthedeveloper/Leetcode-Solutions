class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split(" ")
        # split individual words
        for i in range(len(str_arr)):
            str_arr[i] = str_arr[i][::-1]
            # each word becomes its reverse
        return " ".join(str_arr)
