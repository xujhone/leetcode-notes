from collections import deque
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

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for j in range(2, n + 1):
            # let k0 be the largest k such that dp[i][k-1] <= dp[k+1][j]
            # when i = j - 1, dp[j-1][k-1] <= dp[k+1][j], take k0 = j - 1
            k = j - 1
            # deque of (dec, inc) pairs (k, k + dp[k+1][j]) for i <= k <= k0
            dq = deque()
            for i in range(j - 1, 0, -1):
                # note as i decreases k0 decreases
                while dp[i][k - 1] > dp[k + 1][j]:
                    k -= 1
                    if dq and dq[0][0] > k:
                        dq.popleft()
                # add (i, i + dp[i+1][j]) to deque
                val = i + dp[i + 1][j]
                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((i, val))

                dp[i][j] = min(dq[0][1], dp[i][k] + k + 1)

        return dp[1][n]
