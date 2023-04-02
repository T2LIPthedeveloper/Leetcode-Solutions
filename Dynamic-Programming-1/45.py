class Solution:
    def jump(self, nums: List[int]) -> int:
        #initial position is nums[0]
        #return minimum number of jumps to reach nums[-1]
        #jump to any nums[i+j] where j <= nums[i] and i+j < len(nums)
        #can jump less than what's given on each index
        #jump from 0 is 0
        farthest, steps = 0, 0
        # window to define level - which elements are reachable from current index
        l, r = 0, 0
        while r<len(nums)-1: # check till second last index
            # check for that window
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            steps+=1
        return steps

    
