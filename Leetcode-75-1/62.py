class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid is a 2d array
        # move to bottom right corner
        # only move right or down
        # RETURN NUMBER OF WAYS TO REACH BOTTOM RIGHT CORNER
        # m = number of rows
        # n = number of columns
        m_fact = self.fact(m-1) #subtract 1 because we don't need to move down
        n_fact = self.fact(n-1) #subtract 1 because we don't need to move right
        m_n_fact = self.fact(m+n-2) #subtract 2 because we don't need to move down or right
        return m_n_fact // (m_fact * n_fact)
    

    
    def fact(self, n):
        if n == 0:
            return 1
        return n * self.fact(n-1)
    