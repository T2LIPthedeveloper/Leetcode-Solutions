class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #circular means start and end are consecutive
        #return max sum of subarray
        dp, dp1 = [0] * len(nums), [0] * len(nums)
        dp[0], dp1[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            dp1[i] = min(nums[i], dp1[i-1]+nums[i])
        return max(max(dp), sum(nums)-min(dp1)) if max(dp) > 0 or min(dp1) != sum(nums) else max(dp)
    
        