class Solution:
    def countBits(self, n: int) -> List[int]:

        # let dp[i] = number of 1's in binary of i

        # base cases:
        # dp[0] = 0, dp[1] = 1

        # optimality relation:
        # if i is odd, dp[i] = dp[i-1] + 1
        # else, dp[i] = dp[i>>1]

        dp = list(range(n + 1))

        for i in range(2, n + 1):
            if i & 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]

        return dp
