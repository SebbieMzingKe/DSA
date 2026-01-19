class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    mat[i - 1][j - 1] + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]
                )

        max_len = 0
        for i in range(m + 1):
            for j in range(n + 1):
                length = max_len + 1
                if i >= length and j >= length:
                    # Sum of square ending at i,j with size 'length'
                    total = (
                        P[i][j]
                        - P[i - length][j]
                        - P[i][j - length]
                        + P[i - length][j - length]
                    )
                    if total <= threshold:
                        max_len += 1

        return max_len


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, mat, threshold, expected):
        result = solver.maxSideLength(mat, threshold)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Square size 2: [[1,1], [1,1]] -> sum 4 <= 4
    # Square size 3: sum > 4
    mat1 = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    run_test(1, mat1, 4, 2)

    # Example 2
    # Smallest element is 2, which is > 1. Return 0.
    mat2 = [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
    ]
    run_test(2, mat2, 1, 0)

    # Example 3: Single element valid
    mat3 = [[1, 2], [3, 4]]
    run_test(3, mat3, 1, 1)  # [1] is valid
