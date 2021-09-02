class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        # precompute prime numbers up to 32
        # to quickly check if a number is prime

        #  665772: 0b10100010100010101100
        # to check if i is a prime, (665772 >> i) & 1

        res = 0

        for i in range(left, right + 1):
            if (665772 >> bin(i).count('1')) & 1:
                res += 1

        return res
    