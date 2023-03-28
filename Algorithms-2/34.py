class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #use binary search to find the target
        #if target is not found, return [-1,-1]
        
        #store target indices
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]
        
        

