class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 4 directional connection to each pixel
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # get the original color
        original_color = image[sr][sc]
        # if the original color is the same as the new color, return the image
        if original_color == color:
            return image
        # get the size of the image
        m, n = len(image), len(image[0])
        # create a queue
        queue = []
        queue.append((sr, sc))
        while queue:
            x, y = queue.pop(0)
            image[x][y] = color
            for dir_x, dir_y in directions:
                new_x, new_y = x + dir_x, y + dir_y
                if 0 <= new_x < m and 0 <= new_y < n and image[new_x][new_y] == original_color:
                    queue.append((new_x, new_y)) #using BFS to find all points that have the same color and change them
        return image
    