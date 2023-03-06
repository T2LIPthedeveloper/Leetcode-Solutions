class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # assumption: all rotations are to the right.
        while (k > 0):
            nums.insert(0, nums.pop()) #inserts specified value at start if it's popped from the end.
            k -= 1

