class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        lsum = 0
        for i in nums:
            total += i
        for i in range(len(nums)):
            if lsum == total - lsum - nums[i]:
                return i
            lsum += nums[i]
        return -1
