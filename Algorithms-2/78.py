class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # find all subsets of nums
        result = []
        if nums == []:
            return [[]]
        else:
            result = self.subsets(nums[1:])
            for i in range(len(result)):
                result.append([nums[0]] + result[i])
        return sorted(result)
