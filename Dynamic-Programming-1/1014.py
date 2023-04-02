class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #spot i and j have distance j - i between them
        #score of pair i < j = values[i] + values[j] + i - j
        #return max score of pair
        dp = [0] * len(values)
        dp[0] = values[0]
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], values[i] + i) #max score of pair with i as the right spot
        ans = -float('inf')
        for i in range(len(values)-1, 0, -1):
            ans = max(ans, dp[i-1] + values[i] - i) #max score of pair with i as the left spot
        return ans