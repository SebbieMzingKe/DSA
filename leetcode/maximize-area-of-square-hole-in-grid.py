class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def get_max_gap(bars):
            if not bars:
                return 1
            bars.sort()
            max_len = 1
            current_len = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_len += 1
                else:
                    current_len = 1
                max_len = max(max_len, current_len)
            return max_len + 1

        h_gap = get_max_gap(hBars)
        v_gap = get_max_gap(vBars)
        side = min(h_gap, v_gap)
        return side * side


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, m, hBars, vBars, expected):
        result = solver.maximizeSquareHoleArea(n, m, hBars, vBars)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # hBars=[2,3] (consecutive 2 -> gap 3)
    # vBars=[2]   (consecutive 1 -> gap 2)
    # min(3, 2) = 2. Area = 4.
    run_test(1, 2, 1, [2, 3], [2], 4)

    # Example 2
    # hBars=[2] -> gap 2
    # vBars=[2] -> gap 2
    # Area = 4
    run_test(2, 1, 1, [2], [2], 4)

    # Example 3
    # hBars=[2,3] -> gap 3
    # vBars=[2,4] -> gap 2 (2 and 4 are not consecutive)
    # min(3, 2) = 2. Area = 4.
    run_test(3, 2, 3, [2, 3], [2, 4], 4)

    # Custom Case: Large consecutive block
    # hBars=[2,3,4,5] -> gap 5
    # vBars=[2,3,4]   -> gap 4
    # min(5, 4) = 4. Area = 16.
    run_test(4, 10, 10, [2, 3, 4, 5], [2, 3, 4], 16)
