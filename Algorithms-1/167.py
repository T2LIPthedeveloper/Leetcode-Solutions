class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two numbers such that they add up to target, index1 < index2.
        #return the indices of the two numbers
        #O(n) time complexity, O(1) space complexity
        #numbers is sorted in ascending order (non-decreasing)
        i1, i2 = 0, len(numbers)-1
        while i1 < i2:
            if numbers[i1] + numbers[i2] == target:
                return [i1+1, i2+1]
            elif numbers[i1] + numbers[i2] > target:
                i2 -= 1 #decrease the sum
            else:
                i1 += 1 #increase the sum
        return [-1, -1] #supposedly a non-existent case
