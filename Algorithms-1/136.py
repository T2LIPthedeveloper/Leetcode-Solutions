class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #every appears twice except one, find that one
        numbers = {}
        for i in nums:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 1
        return [i for i in numbers if numbers[i] == 1][0]
    