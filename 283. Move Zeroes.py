class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # index of nonzero element
        # nums[0:i] are nonzeros
        i = 0

        for j in range(len(nums)):
            # nums[i:j] are all zeros
            if nums[j]:
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                