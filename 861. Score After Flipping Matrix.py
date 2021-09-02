class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # toggle i-th row, grid[i] -> 2^n - 1 - grid[i]
        # if grid[i] < 2^{n-1} (grid[i][0] == 0), toggle i-th row

        # 0-th col
        res = m * (1 << n - 1)

        # if j-th col has more 0's than 1's, toggle j-th col
        for j in range(1, n):
            # count number of 1's

            # if grid[i][0] == 1 and grid[i][j] == 1,
            # no need to toggle i-th row
            # if grid[i][0] == 0 and grid[i][j] == 0,
            # need to toggle i-th row
            ones = sum(grid[i][0] == grid[i][j] for i in range(m))

            # if ones <= m // 2, toggle j-th col
            res += max(ones, m - ones) * (1 << n - 1 - j)

        return res
    