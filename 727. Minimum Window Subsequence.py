class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        # if s2[0:j] is a subsequence of s1[0:i], dp[i][j] = len of min substring of s1[0:i] that contains s2[0:j] as
        # subsequence and ends at s1[i-1] else, dp[i][j] = inf

        # base cases:
        # if j > 0, dp[0][j] = inf, dp[i][0] = 0

        # optimality relation:
        # if s1[i-1] == s2[j-1] and dp[i-1][j-1] != inf, dp[i][j] = dp[i-1][j-1] + 1
        # else, if dp[i-1][j] != inf, dp[i][j] = dp[i-1][j] + 1

        m, n = len(s1), len(s2)

        if m < n:
            return ''

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # base cases:
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j] + 1

        idx, minLen = -1, float('inf')
        for i in range(n, m + 1):
            if minLen > dp[i][n]:
                idx = i
                minLen = dp[i][n]

        return '' if minLen == float('inf') else s1[idx - dp[idx][n]:idx]
