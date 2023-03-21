class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #given list of numbers return all possible permutations
        if len(nums) == 1:
            return [nums]
        return [[nums[i]] + j for i in range(len(nums)) for j in self.permute(nums[:i] + nums[i+1:])]