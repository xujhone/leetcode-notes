class Solution:
    def trap(self, height: List[int]) -> int:

        # consider bar at index i with height[i]
        # how much water can it hold?
        # let le = max(height[0:i]) and ri = max(height[i+1:])
        # then it can trap max(min(le, ri) - height[i], 0) water

        n = len(height)

        l, r = 1, n - 2
        # maxl = max(height[0:l])
        # maxr = max(height[r+1:])
        maxl, maxr = height[0], height[n - 1]

        res = 0

        while l <= r:
            # consider bar at l and r
            if maxl <= maxr:
                # since max(height[l+1:]) >= maxr >= maxl
                # min(le, ri) = maxl
                res += max(maxl - height[l], 0)
                maxl = max(maxl, height[l])
                l += 1
            else:
                res += max(maxr - height[r], 0)
                maxr = max(maxr, height[r])
                r -= 1

        return res
