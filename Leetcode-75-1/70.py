class Solution:
    def climbStairs(self, n: int) -> int:
        # each step is either 1 or 2
        # faster algorithm than usual recursion
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return third
    #
    
    
    
        