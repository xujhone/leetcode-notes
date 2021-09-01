class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor of all nums
        xor = 0

        for v in nums:
            xor ^= v

        # since two elements (a, b) appear only once
        # xor = a ^ b != 0

        # find the rightmost set bit where a and b differ
        # note -xor = ~xor + 1
        xor &= -xor

        res = [0, 0]

        for v in nums:
            # divide nums into two groups
            if v & xor:
                res[0] ^= v
            else:
                res[1] ^= v

        return res
