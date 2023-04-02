class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        pos, neg = [0]*n, [0]*n #storing arrays containing subarray lengths, not products

        pos[0] = 1 if nums[0] > 0 else 0 
        neg[0] = 1 if nums[0] < 0 else 0

        for i in range(1,n):
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1 #if previous subarray is positive, add 1 to length
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0 #if previous subarray is negative, add 1 to length
            elif nums[i] < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0 #if previous subarray is negative, add 1 to length
                neg[i] = pos[i-1] + 1 #if previous subarray is positive, add 1 to length

        return max(pos)