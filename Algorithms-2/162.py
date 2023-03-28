class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #peak is strictly higher than any neighbours
        #return any peak
        #binary search, O(log n)
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid+1]:
                hi = mid #instead of mid - 1 because mid could be the peak
            else:
                lo = mid + 1 #instead of mid because mid could be the peak so we need to check it
        return lo
    