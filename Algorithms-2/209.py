class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j] #iterates until sum is greater, then inner loop
            while sum >= target:
                min_len = min(min_len, j-i+1)
                sum -= nums[i]
                i += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len
    
    
