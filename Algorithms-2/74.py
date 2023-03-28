class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search through 2d matrix
        #m = rows, n = columns
        #return True if target is found, False otherwise
        #non-decreasing order sorted rows
        #first int of each row > last int of prev row
        #use binary search to find target

        #find row
        # use mid/n, mid%n to find row and column
        
        start, end = 0, len(matrix)*len(matrix[0])-1
        while start <= end:
            mid = (start + end) // 2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid+1
            else:
                end = mid-1
        return False
    
    
    

