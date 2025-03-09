from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_dict = { }
        for num in nums:
            n_dict[num] = n_dict.get(num, 0) + 1

        i = 0
        for num in sorted(n_dict.keys()):
            for j in range(min(n_dict[num], 2)):
                nums[i] = num
                i+=1
        return i