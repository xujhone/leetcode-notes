class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        # sort nums so nums is increasing

        # let dp[i] be number of elements in a max subset
        # that contains nums[i] in nums[0:i+1]
        # base case:
        # dp[0] = 1
        # optimality relation:
        # for 0 <= j < i, if nums[i] % nums[j] == 0, dp[i] = dp[j] + 1
        # dp[i] = 1 + max_{0<=j<i: nums[i]%nums[j]==0} dp[j]

        n = len(nums)

        nums.sort()

        dp, prev = [1] * n, list(range(n))

        maxdp, idx = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > maxdp:
                maxdp = dp[i]
                idx = i

        res = [nums[idx]]

        while idx != prev[idx]:
            idx = prev[idx]
            res.append(nums[idx])

        return res
