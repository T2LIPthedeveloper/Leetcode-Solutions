class Solution:
    def reverseBits(self, n: int) -> int:
        #rverse bits of 32 bit unsigned
        return int(bin(n)[2:].zfill(32)[::-1],2)