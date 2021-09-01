class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # let P (N) be set of elements in nums that are assigned '+' ('-')
        # note if nums[i] = nums[j] and i !=j, we consider them as different elements in the set
        # then need to count number of P's such that sum(P) - sum(N) = target
        # sum(P) - sum(N) + sum(P) + sum(N) = target + sum(P) + sum(N)
        # 2 * sum(P) = target + sum(nums)
        # sum(P) = (target + sum(nums)) / 2

        # need to find number P's such that sum(P) = (target + sum(nums)) / 2
        # note it implies (target + sum(nums)) has to be even

        total = sum(nums)

        if target < - total or target > total or (target + total) & 1:
            return 0

        # let dp[i][t] be number of subsets P in nums[0:i] such that sum(P) = j
        # base case:
        # dp[0][0] = 0 ? 1

        # optimality relation:
        # if the subset does not contain nums[i-1], dp[i][j] += dp[i-1][j]
        # else, dp[i][j] += dp[i-1][j-nums[i-1]]
        # thus, dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

        # dp[1][nums[0]] = dp[0][nums[0]] + dp[0][0] = 0 + 1 = 1
        # thus, dp[0][0] = 1 and dp[i][j] = 0 for impossible j

        n = len(nums)
        # reset new target for subset problem
        target = (target + total) // 2

        dp = [1] + [0] * target

        for val in nums:
            for j in range(target, val - 1, -1):
                dp[j] += dp[j - val]

        return dp[target]
