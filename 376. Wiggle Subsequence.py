class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # at any day, there are 3 states:
        # nums[i] == nums[i-1], nums[i] > nums[i-1], nums[i] < nums[i-1]

        # let dp[i][0] be len of longest wiggle subsequence ending with increasing at nums[i]
        # let dp[i][1] be len of longest wiggle subsequence ending with decreasing at nums[i]

        # base case:
        # dp[0][0] = dp[0][1] = 1

        # optimality relation:
        # if nums[i] >= nums[i-1], replacing nums[i-1] by nums[i] so dp[i][0] = dp[i-1][0]
        # else, extending dp[i][1] = dp[i-1][0] + 1
        # if nums[i] <= nums[i-1], replacing nums[i-1] by nums[i] so dp[i][1] = dp[i-1][0]
        # else, extending dp[i][0] = dp[i-1][1] + 1

        dp = [1, 1]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[0] = dp[1] + 1
            # else nums[i] <= nums[i-1]
            # we replace nums[i-1] by nums[i] in subsequence ending with decreasing
            # so not updates to dp[1]
            elif nums[i] < nums[i - 1]:
                dp[1] = dp[0] + 1
            # else nums[i] >= nums[i-1]
            # no updates to dp[0]

        # only need to compare dp[n-1][0] and dp[n-1][1]
        # longest wiggle subsequence can be extended to the end
        return max(dp)
