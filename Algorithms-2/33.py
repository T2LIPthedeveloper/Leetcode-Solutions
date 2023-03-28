class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #search through rotated sorted array at random pivot index
        # return index of target in O log n time
        # use a binary search algorithm to find pivot index first
        # then use binary search to find target index

        #find pivot index
        def findPivot(nums):
            lo, hi = 0, len(nums)-1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > nums[hi]:
                    lo = mid+1 #pivot is in the right half
                else:
                    hi = mid #pivot is not in the right half
            return lo
        
        piv = findPivot(nums)

        #search for target
        def search(nums, target):
            lo, hi = 0, len(nums)-1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid
            return lo
        
        lo = search(nums[:piv], target)
        hi = search(nums[piv:], target)
        return lo if nums[lo] == target else hi+piv if nums[hi+piv] == target else -1
        