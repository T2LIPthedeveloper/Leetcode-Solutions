class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #return true if max index in nums can be reached else false
        #can jump less than what's given on each index

        #use dp
        #must reset if index is 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] == 0:
                return False
            dp[i] = max(dp[i-1]-1, nums[i])
            #dp[i] = max steps that can be taken from index i
            #has to be max of previous index's max steps - 1 and current index's value
            #because we can jump less than what's given on each index
        return True
            
