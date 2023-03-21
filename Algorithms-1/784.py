class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #list of all possible strings with permutations of letter cases
        #return list of strings

        #base case
        if len(s) == 1:
            if s.isalpha():
                return [s.lower(), s.upper()]
            else:
                return [s]
        #recursive case
        if s[0].isalpha():
            return [s[0].lower() + i for i in self.letterCasePermutation(s[1:])] + [s[0].upper() + i for i in self.letterCasePermutation(s[1:])]
        else:
            return [s[0] + i for i in self.letterCasePermutation(s[1:])]