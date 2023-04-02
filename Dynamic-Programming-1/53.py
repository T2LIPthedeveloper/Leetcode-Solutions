class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #subarray must be contiguous
        #return max sum of subarray
        #use dp

        dp = [0] * len(nums)
        dp[0] = nums[0]
        begin, end = 0, 0
        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] > nums[i]:
                dp[i] = dp[i-1] + nums[i]
                end = i
            else:
                begin = i
                dp[i] = nums[i]
        return max(dp)
    
