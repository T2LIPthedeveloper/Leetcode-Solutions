class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #count number of subarrays with product less than k
        prod = 1
        count = 0
        i = 0
        for j in range(len(nums)):
            prod *= nums[j]
            while prod >= k and i <= j:
                prod /= nums[i] #divide by the first element in the subarray
                i += 1 #bring the start of the subarray forward
            count += j-i+1 #number of subarrays ending at j
        return count
    
    #sliding window, O(n)