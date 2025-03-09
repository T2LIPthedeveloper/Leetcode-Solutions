from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n1 = nums[-k:]
        n2 = nums[:-k]
        for i, v in enumerate(n1):
            nums[i] = v
        for i, v in enumerate(n2):
            nums[i+k] = v
        


        