class Solution:
    def hammingWeight(self, n: int) -> int:
        #binary representation of unsigned int, return 1 bits
        return bin(n).count('1')
    