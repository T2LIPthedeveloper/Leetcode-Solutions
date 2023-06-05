from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #8-directional connection meaning corners included
        #return shortest path from top left to bottom right
        #if no path, return -1
        #if top left or bottom right is 1, return -1
        #if grid is empty, return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if not grid:
            return -1
        #use BFS
        directions = {
            (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)
        }
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        while queue:
            row, col = queue.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return grid[row][col]
            for d in directions:
                r, c = row + d[0], col + d[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                    queue.append((r,c))
                    grid[r][c] = grid[row][col] + 1
        return -1