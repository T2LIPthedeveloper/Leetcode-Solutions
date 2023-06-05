class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #find all permutations of numbers in nums
        #no duplicates
        #return sorted list
        ans = []
        nums.sort()
        
        def helper(a, b):
            if len(b) == 0:
                if a not in ans:
                    ans.append(a)
                return
            for i in range(len(b)):
                c = a[i]
                helper(a + [c], b[:i] + b[i+1:])
                helper(a, b[:i] + b[i+1:])
        helper([], nums)
        
        