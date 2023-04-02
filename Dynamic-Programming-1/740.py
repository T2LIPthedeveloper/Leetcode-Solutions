class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)

        for val in nums:
            dp[val] += val
        #list of value sums
        #dp[i] = sum of all values in nums that are equal to i
        #dp[i] = 0 if i not in nums
        #house robber technique

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+dp[i])
        #dp[i] = max value that can be earned by deleting all values equal to i
        #dp[i] = max(dp[i-1], dp[i-2]+dp[i])
        return dp[-1]


