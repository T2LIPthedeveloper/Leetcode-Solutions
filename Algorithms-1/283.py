class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move all zeros to end if they exist.
        # O(n) time complexity, O(1) space complexity

        nums.sort(key = lambda x: x == 0)

        #thank god for lambda functions