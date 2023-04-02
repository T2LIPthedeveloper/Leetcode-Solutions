class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        #use dfs to find all connected
        #if a node is connected to another node, then it is connected to all the nodes that the other node is connected to
        def dfs(isConnected, i, visited):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(isConnected, j, visited)



        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(isConnected, i, visited)
                count += 1
        return count
    