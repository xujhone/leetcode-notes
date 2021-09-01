class Solution:
    def addDigits(self, num: int) -> int:
        # if num = 0, return 0
        # else, it is one of {1,2,3,4,5,6,7,8,9}

        # num = d0 + d1 * 10 + d2 * 100 + ... + d_k * 10^k
        #     = d0 + d1 * (1 + 9) + d2 * (1 + 99) + ... + d_k * (1 + 9...9)
        #     = d0 + d1 + d2 + ... d_k + 9 * (d1 + d2*11 + ... + d_k * 1...1)
        # num mod 9 = (d0 + d1 + ... d_k) mod 9

        if num == 0:
            return 0

        return 1 + (num - 1) % 9
    