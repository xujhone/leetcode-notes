class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        # let dp[i][j] be length of longest Fib subsequence
        # ending with arr[i] and arr[j]

        # base cases:
        # dp[0][j] = 2

        # optimality relation:
        # if k > j such that arr[k] = arr[i] + arr[j], dp[j][k] = dp[i][j] + 1
        # given arr[j] and arr[k], if arr[k] - arr[j] in arr and let i be index
        # if i < j
        # if arr[k]-arr[j] in arr with index i and i < j, dp[j][k] = dp[i][j] + 1
        # else, dp[j][k] = 2

        n = len(arr)

        val2idx = {v: i for i, v in enumerate(arr)}

        dp = [[2] * n for _ in range(n)]

        res = 2

        for j in range(1, n - 1):
            for k in range(j + 1, n):
                arri = arr[k] - arr[j]
                if arri >= arr[j]:
                    break
                # arri < arr[j] < arr[k]
                if arri in val2idx:
                    dp[j][k] = dp[val2idx[arri]][j] + 1

                    res = max(res, dp[j][k])

        if res >= 3:
            return res
        else:
            return 0
