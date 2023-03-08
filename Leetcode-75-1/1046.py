class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # combine two heaviest stones until only one is left.
        # return the weight of the last stone
        stones.sort()
        while len(stones) > 1:
            # combine the two heaviest stones
            # add the new stone to the list
            # sort the list
            stones.append(stones.pop() - stones.pop())
            stones.sort()
        return stones[0]