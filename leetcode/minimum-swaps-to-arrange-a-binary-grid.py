class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)

        trailing_zeros = []

        for row in grid:
            count = 0
            
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        for i in range(n):
            target_zeros = n - 1 - i
            found_valid_row = False

            for j in range(i, n):
                if trailing_zeros[j] >= target_zeros:
                    found_valid_row = True

                    swaps += (j - i)

                    valid_row_zeros = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, valid_row_zeros)
                    break
            
            if not found_valid_row:
                return -1
        return swaps


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, expected):
        result = solver.minSwaps(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Zeros needed: [2, 1, 0]. Grid zeros: [0, 1, 2].
    # Swap row 2 to 0 (2 swaps). Zeros become [2, 0, 1].
    # Swap row 2 to 1 (1 swap). Zeros become [2, 1, 0].
    # Total swaps = 3
    run_test(1, [[0,0,1],[1,1,0],[1,0,0]], 3)

    # Example 2
    # All rows have 1 trailing zero. Row 0 needs 3. Impossible.
    run_test(2, [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]], -1)

    # Example 3
    # Zeros: [2, 1, 0]. Already valid. 0 swaps.
    run_test(3, [[1,0,0],[1,1,0],[1,1,1]], 0)
    
    # Custom Case: Large jump
    # [[0,0,0],[1,1,1],[1,1,0]]
    # Zeros: [3, 0, 1]. Needed: [2, 1, 0]
    # index 0: needs 2. Row 0 has 3. Good. (0 swaps)
    # index 1: needs 1. Row 1 has 0. Look at Row 2 (has 1).
    # Swap row 2 up. (1 swap). Zeros: [3, 1, 0]. Good.
    run_test(4, [[0,0,0],[1,1,1],[1,1,0]], 1)