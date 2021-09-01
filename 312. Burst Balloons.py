class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # let numsNew = [1] + nums + [1]
        # let n = len(numsNew) and nums = numsNew[1:n-1]

        # for 1 <= i <= j <= n-2
        # let dp[i][j] = max coins for bursting balloons in numsNew[i:j+1]

        # base cases:
        # dp[i][i] = numsNew[i-1] * numsNew[i] * numsNew[i+1] for 1 <= i <= n-2

        # optimality relation:
        # for i <= k <= j, suppose numsNew[k] is the LAST to burst
        # dp[i][j] = max_{i<=k<=j} dp[i][k-1] + numsNew[i-1] * numsNew[k] * numsNew[j+1] + dp[k+1][j]

        # let dp[i][j] = 0 for i > j

        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # base cases:
        for i in range(1, n - 1):
            dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]

        for l in range(2, n - 1):
            for i in range(1, n - l):
                j = i + l - 1
                dp[i][j] = max(
                    dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j] for k in range(i, j + 1))

        return dp[1][n - 2]
