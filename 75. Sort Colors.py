class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # if the current element is 0, put it in the first third
        # and if it is 2, put it in the last third

        n = len(nums)

        # i: nums[0:i] are all 0's
        i = 0
        # j: nums[j+1:] are all 2's
        j = n - 1
        # index of current element
        # perform swaps such that nums[0:k] do not have 2
        k = 0

        # k < j does not work b/c it may accur that nums[k] = 2, nums[j] = 0 and k = j - 1
        # so after swap, nums[k] = 0 and j = k, still need one more swap
        while k <= j:
            if nums[k] == 0:
                # note i <= k so nums[i] cannot be 2
                # so after swap, nums[k] can be 0 or 1 so increment k
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                # nums[0:i] are all 0's
                k += 1
                # nums[i:k] do not have 2
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
                # nums[j+1:] are all 2's
                # after swap, nums[k] can be 0, 1 or 2 so do not increment k
            else:
                # nums[k] = 1, nums[0:k+1] do not have 2, so increment k
                k += 1
