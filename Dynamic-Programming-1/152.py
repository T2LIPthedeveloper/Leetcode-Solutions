class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp, dp1 = [0] * len(nums), [0] * len(nums)
        dp[0], dp1[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp[i] = max(nums[i], dp1[i-1]*nums[i])
                dp1[i] = min(nums[i], dp[i-1]*nums[i])
            else:
                dp[i] = max(nums[i], dp[i-1]*nums[i])
                dp1[i] = min(nums[i], dp1[i-1]*nums[i])
        return max(max(dp), nums[0])