class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # let nums[idx] be the single element
        # note idx is even

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # if mid is even (idx < n-1)
            # if nums[mid] == nums[mid+1], idx > mid
            # else, idx <= mid

            # if mid is odd
            # if nums[mid] == nums[mid-1], idx > mid
            # else, idx < mid

            if nums[mid] == nums[mid ^ 1]:
                # note odd ^ 1 = odd - 1 and even ^ 1 = even + 1
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
