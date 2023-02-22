# The isBadVersion API is already defined for you.


class Solution:
    def isBadVersion(version: int) -> bool:
        pass
    def firstBadVersion(self, n: int) -> int:
        #implement binary search algorithm for this question
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left