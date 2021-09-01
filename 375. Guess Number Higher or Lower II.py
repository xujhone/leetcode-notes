class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # let dp[i][j] be min money needed to win for number from i to j
        # base cases:
        # dp[i][i] = 0, dp[i][j] = TBD if i > j
        # optimality relation:
        # for i <= k <= j, if guess k and it was wrong,
        # dp[i][j] = k + max(dp[i][k-1], dp[k+1][j])
        # thus, dp[i][j] = 0 if i > j
        # thus, dp[i][j] = min_{i<=k<=j} k + max(dp[i][k-1], dp[k+1][j])

        # dp[i][j+1] = min_{i<=k<=j+1} k + max(dp[i][k-1], dp[k+1][j+1])
        #            = min(min_{i<=k<=j} k + max(dp[i][k-1], dp[k+1][j+1]), j+1 + max(dp[i][j], dp[j+2][j+1]))
        #            = min(min_{i<=k<=j} k + max(dp[i][k-1], dp[k+1][j+1]), j+1 + dp[i][j])
        # inductively, suppose dp[k+1][j+1] >= dp[k+1][j], then dp[i][j+1] >= dp[i][j]
        # Thus, dp[i][j] increases as j increases
        # similarly, dp[i][j] decreases as i increases

        #

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(2, n + 1):
            # l = j - i + 1
            for i in range(1, n - l + 2):
                j = l + i - 1
                dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j + 1))

        return dp[1][n]
