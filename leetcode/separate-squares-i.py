class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')

        for _, y, l in squares:
            total_area += float(l) * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        target = total_area / 2.0

        low = float(min_y)
        high = float(max_y)

        for _ in range(100):
            mid = (low + high) / 2.0
            current_area = 0.0

            for _, y, l in squares:
                if mid > y:

                    h = min(float(l), mid - y)
                    current_area += h * l

            if current_area >= target:
                high = mid
            else:
                low = mid

        return high


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, squares, expected):
        result = solver.separateSquares(squares)
        # Check if result is within 10^-5
        diff = abs(result - expected)
        status = "PASS" if diff < 1e-5 else "FAIL"
        print(
            f"Test Case {case_num}: Result {result:.5f} (Expected: {expected:.5f}) -> {status}"
        )

    # Example 1
    # Total area = 1*1 + 1*1 = 2. Target = 1.
    # At y=1, area below is 1 (sq1 full). y=2, area below is 2.
    # Range [1, 2] has area 1. Minimum is 1.0.
    squares1 = [[0, 0, 1], [2, 2, 1]]
    run_test(1, squares1, 1.00000)

    # Example 2
    # Sq1: [0,0,2] -> Area 4. Sq2: [1,1,1] -> Area 1. Total = 5. Target = 2.5.
    # Cut at 1.16667...
    squares2 = [[0, 0, 2], [1, 1, 1]]
    run_test(2, squares2, 1.16667)

    # Custom Case: Overlapping squares
    # Sq1: [0,0,2] (Area 4), Sq2: [0,0,2] (Area 4). Total 8. Target 4.
    # Cut should be exactly halfway up the squares, at y=1.
    squares3 = [[0, 0, 2], [0, 0, 2]]
    run_test(3, squares3, 1.00000)
