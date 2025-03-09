from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))
        for i, v in enumerate(sorted(set(nums))):
            nums[i] = v
        return k