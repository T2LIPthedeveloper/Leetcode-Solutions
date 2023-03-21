class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #given two numbers n and k, return all possible combinations of k numbers out of 1 ... n.

        while (n < k):
            return []
        if (k == 1):
            return [[i] for i in range(1,n+1)]
        if (k == n):
            return [[i for i in range(1,n+1)]]
        return self.combine(n-1,k) + [[n] + i for i in self.combine(n-1,k-1)]
    