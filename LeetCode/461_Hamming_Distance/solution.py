class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dif = 0
        mask = 1
        while mask <= x or mask <= y:
            if x & mask != y & mask:
                dif += 1
            mask <<= 1
        return dif