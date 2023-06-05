class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #find all subsets of nums
        #no duplicates
        #return sorted list
        ans = []
        nums.sort()

        def helper(curr, prior):
            if len(prior) == 0:
                if curr not in ans:
                    ans.append(curr)
                return
            ch = prior[0]
            helper(curr + [ch], prior[1:])
            helper(curr, prior[1:])
        helper([], nums)
        return ans
    
