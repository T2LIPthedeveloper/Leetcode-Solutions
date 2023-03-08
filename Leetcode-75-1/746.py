class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of the ith step on a staircase
        # start either on 0 or 1
        # find the minimum cost to reach the top of the staircase
        # the top of the staircase is the last index of the cost array
        
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        # create a dp array
        # a dp array is an array that stores the minimum cost to reach the ith step
        # it works because the minimum cost to reach the ith step is the minimum of the minimum cost to reach the (i-1)th step and the (i-2)th step
        dp = [0] * len(cost)
        # initialize the dp array
        dp[0] = cost[0]
        dp[1] = cost[1]
        # fill the dp array
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # return the minimum of the last two elements of the dp array
        return min(dp[-1], dp[-2])
    