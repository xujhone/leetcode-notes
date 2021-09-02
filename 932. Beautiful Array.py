class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # note nums[k] * 2 is even, so is nums[i] + nums[j]
        # consider put all even numbers in the first half
        # and all odd numbers in second half
        # then (i, j) have to be in the same half
        # otherwise nums[i] + nums[j] is odd

        # now consider [2, 4, 6, 8, 10, ...]
        # divided all by 2
        # then [1, 2, 3, 4, 5, ...]

        # for [1, 3, 5, 7, 9, ...]
        # add all by 1, then divide by 2
        # then [1, 2, 3, 4, 5, ...]

        v2bin = {i: bin(i)[:1:-1] for i in range(1, n + 1)}

        return sorted(range(1, n + 1), key=lambda x: v2bin[x])
    