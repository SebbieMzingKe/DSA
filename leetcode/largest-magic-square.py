class Solution(object):
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * (n) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = row_prefix[r][c + k] - row_prefix[r][c]

                    match = True
                    for i in range(1, k):
                        if (row_prefix[r + i][c + k] - row_prefix[r + i][c]) != target:
                            match = False
                            break
                    if not match:
                        continue

                    for j in range(k):
                        if (col_prefix[r + k][c + j] - col_prefix[r][c + j]) != target:
                            match = False
                            break
                    if not match:
                        continue

                    d1, d2 = 0, 0
                    for i in range(k):
                        d1 += grid[r + i][c + i]
                        d2 += grid[r + i][c + k - 1 - i]

                    if d1 == target and d2 == target:
                        return k
        return 1


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, expected):
        result = solver.largestMagicSquare(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    grid1 = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    # The 3x3 square at top-middle (indices [0][1] to [2][3]) is magic.
    run_test(1, grid1, 3)

    # Example 2
    grid2 = [[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]
    # 2x2 square [3,3],[3,3] matches
    run_test(2, grid2, 2)

    # Edge Case: Smallest 1x1
    grid3 = [[5]]
    run_test(3, grid3, 1)
