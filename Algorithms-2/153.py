class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find minimum in rotated sorted array
        #array rotation is done by moving elements to the right
        #return min element of array
        #binary search, O(log n)
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]: #this works even when array is rotated by 1 element
                lo = mid + 1 #instead of mid because mid could be the minimum so we need to check it
            else:
                hi = mid #instead of mid - 1 because mid could be the minimum
        return nums[lo] #and not hi because we are returning the value not the index
    