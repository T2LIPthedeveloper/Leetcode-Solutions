class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #use BFS to find max island area
        #use a queue to store the coordinates of the island
        #use a set to store the coordinates of the island

        len_x = len(grid)
        len_y = len(grid[0])
        max_area = 0
        for i in range(len_x):
            for j in range(len_y):
                if grid[i][j] == 1:
                    area = 0
                    q = [(i,j)]
                    while q:
                        x,y = q.pop(0)
                        if grid[x][y] == 1:
                            area += 1
                            grid[x][y] = 0
                            if x > 0:
                                q.append((x-1,y))
                            if x < len_x-1:
                                q.append((x+1,y))
                            if y > 0:
                                q.append((x,y-1))
                            if y < len_y-1:
                                q.append((x,y+1))
                    max_area = max(max_area, area)
        return max_area
        