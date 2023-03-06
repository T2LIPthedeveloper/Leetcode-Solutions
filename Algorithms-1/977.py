class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums

#sort the array after squaring everything. O(nlogn) time complexity because of the sorting algorithm used