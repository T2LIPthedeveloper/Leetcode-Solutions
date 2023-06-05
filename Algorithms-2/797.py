from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #find all paths in DAG from node 0 to node N-1
        n = len(graph)
        #use DFS
        #keep track of path
        queue = deque()
        queue.append((0, [0]))
        paths = []
        while queue:
            node, path = queue.popleft()
            if node == n-1:
                paths.append(path)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
        return paths