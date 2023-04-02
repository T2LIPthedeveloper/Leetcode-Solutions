class Solution:
    def maxArea(self, height: List[int]) -> int:
        #endpoints in format (i, 0) and (i, height[i])
        #find the max area of the container
        #area = dist(endpoints) * min(height)
        #find smaller side first
        #move the larger side inwards
        #return the max area

        max_area, min_h, area, i, j = 0, 0, 0, 0, len(height)-1
        while i < j:
            min_h = min(height[i], height[j])
            area = min_h * (j-i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
    



