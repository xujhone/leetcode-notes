class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        # let dp[i][j] be minimized largest sum among j subarrays
        # from nums[0:i]

        # base cases:
        # if i < j or (i > 0 and j = 0), dp[i][j] = inf
        # dp[i][1] = sum(nums[0:i])

        # optimality relation:
        # let j-1 <= k < i and nums[k:i] be last subarray
        # then the largest sum is max(dp[k][j-1], sum(nums[k:i]))
        # dp[i][j] = min_{j-1<=k<i} max(dp[k][j-1], sum(nums[k:i]))

        # note dp[k][j-1] is increasing as k increases
        # while sum(nums[k:i]) is decreasing as k increases
        # the min is when two arrays are closest to each other

        n = len(nums)

        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        # base cases: j = 1
        dp[0][0] = 0
        dp[0][1] = 0
        for i in range(1, n + 1):
            dp[i][1] = dp[i - 1][1] + nums[i - 1]

        # note sum(nums[k:i]) = dp[i][1] - dp[k][1]

        for j in range(2, m + 1):
            tmp = list(dp[k][j - 1] + dp[k][1] for k in range(j - 1, n))
            for i in range(j, n + 1):
                # dp[i][j] = min(max(dp[k][j-1], dp[i][1]-dp[k][1]) for k in range(j-1, i))
                # note dp[k][j-1] is increasing and dp[i][1]-dp[k][1] is decreasing
                # the min of max is when dist(dp[k][j-1], dp[i][1]-dp[k][1]) is minimized
                # consider dp[k][j-1]+dp[k][1] for k in range(j-1, i)
                # find k such that dp[k][j-1]+dp[k][1] is closest to dp[i][1]

                # tmp[0:idx] < dp[i][1] and tmp[idx:] >= dp[i][1]
                idx = bisect.bisect_left(tmp, dp[i][1], 0, i - j + 1)
                # update idx from tmp
                idx += j - 1

                c1 = c2 = float('inf')

                if idx >= j:
                    c1 = max(dp[idx - 1][j - 1], dp[i][1] - dp[idx - 1][1])
                if idx < i:
                    c2 = max(dp[idx][j - 1], dp[i][1] - dp[idx][1])

                dp[i][j] = min(c1, c2)

        return dp[n][m]

