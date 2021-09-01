class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        n = len(nums)
        # since elements in nums are in range [1, n]
        # can use the sign of nums to indicate whether it appears before

        for val in nums:
            if nums[abs(val) - 1] < 0:
                # val appeared once
                res.append(abs(val))
            else:
                nums[abs(val) - 1] *= -1

        return res
    