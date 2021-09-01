class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # let dp[i] be len of LIS ending with nums[i] in nums[0:i+1]

        # base case:
        # dp[0] = 1

        # optimality relation:
        # for 0 <= j < i, if nums[j] < nums[i], dp[i] = dp[j] + 1
        # thus, dp[i] = 1 + max_{0<=j<i: nums[j] < nums[i]} dp[j]
        # O(n^2)

        # binary search: O(n log n)

        n = len(nums)

        # stack of top of piles of cards
        top = [nums[0]]

        for i in range(1, n):
            # binary search for the left most pile whose top is larger than nums[i]
            # if not exists, add a new pile
            if top[-1] < nums[i]:
                top.append(nums[i])
            else:
                # top[0:idx] < nums[i]
                idx = bisect_left(top, nums[i])
                # put nums[i] on top the pile
                top[idx] = nums[i]

        return len(top)
