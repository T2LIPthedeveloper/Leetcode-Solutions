class Solution:
    def rob(self, nums: List[int]) -> int:
        #houses arranged in circle so first and last cannot be consecutively robbed
        if len(nums) <= 3:
            return max(nums)
        #rob first house
        dp1 = [0] * len(nums)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i]) #generate maximum when robbing first house
        #rob last house
        dp2 = [0] * len(nums)
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i]) #generate maximum when robbing last house
        return max(dp1[-2], dp2[-1]) #choose between their relative maximums
    