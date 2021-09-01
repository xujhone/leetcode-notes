class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        # let dp[i] be number of arithmetic slices ending at nums[i]

        # base case:
        # dp[2] = nums[2] - nums[1] == nums[1] - nums[0]

        # optimality relation:
        # if nums[i+1] - nums[i] != nums[i] - nums[i-1], dp[i+1] = 0
        # else, dp[i+1] = dp[i] + 1
        # all previous arithmetic slice can be extended to nums[i+1]: dp[i]
        # another slice: nums[i-1: i+2]

        n = len(nums)

        if n < 3:
            return 0

        # total number of arithmetic slices
        res = 0

        prev = nums[2] - nums[1] == nums[1] - nums[0]

        res += prev

        for i in range(2, n - 1):
            # dp[i] = prev
            if nums[i + 1] - nums[i] == nums[i] - nums[i - 1]:
                prev += 1
                res += prev
            else:
                prev = 0

        return res
