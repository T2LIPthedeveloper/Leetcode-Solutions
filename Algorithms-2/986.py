class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #return the intersection of the two lists
        #if there is no intersection, return an empty list
        m, n = len(firstList), len(secondList)
        i = j = 0
        res = []
        while i < m and j < n:
            if firstList[i][-1] >= secondList[j][0] and firstList[i][0] <= secondList[j][-1]:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][-1], secondList[j][-1])])
            if firstList[i][-1] < secondList[j][-1]:
                i += 1
            else:
                j += 1
        return res 
            
            
    