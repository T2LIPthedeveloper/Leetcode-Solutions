class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #all triplets such that i != j != k and i + j + k = 0
        #sort the list
        #iterate through the list
        #for each element, find the other two elements that sum to 0
        #if the other two elements are not the same as the current element, add them to the list
        #if the other two elements are the same as the current element, add them to the list if they are not already in the list
        #return the list
        res = set()

        neg, pos, zer = [], [], []
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zer.append(i)
        N, P = set(neg), set(pos)

        if zer:
            for n in P:
                if -1*n in N:
                    res.add((-1*n, 0, n))
        
        if len(zer) >= 3:
            res.add((0,0,0))
        
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                if -1*(neg[i]+neg[j]) in P:
                    res.add(tuple(sorted([neg[i], neg[j], -1*(neg[i]+neg[j])])))
        
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if -1*(pos[i]+pos[j]) in N:
                    res.add(tuple(sorted([pos[i], pos[j], -1*(pos[i]+pos[j])])))

        return res
