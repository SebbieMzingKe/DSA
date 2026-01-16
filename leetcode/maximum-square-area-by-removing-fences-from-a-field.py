class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])

        v_gaps = set()

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_gaps.add(vFences[j] - vFences[i])

        max_side = -1

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                current_gap = hFences[j] - hFences[i]

                if current_gap in v_gaps:
                    max_side = max(max_side, current_gap)

        if max_side == -1:
            return -1

        return (max_side * max_side) % (10**9 + 7)


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, m, n, hFences, vFences, expected):
        result = solver.maximizeSquareArea(m, n, hFences, vFences)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # H-Fences: 1, 2, 3, 4 -> Gaps: {1, 2, 3}
    # V-Fences: 1, 2, 3    -> Gaps: {1, 2}
    # Common max: 2. Area = 4.
    run_test(1, 4, 3, [2, 3], [2], 4)

    # Example 2
    # H-Fences: 1, 2, 6 -> Gaps: {1, 4, 5}
    # V-Fences: 1, 4, 7 -> Gaps: {3, 6}
    # No common gaps.
    run_test(2, 6, 7, [2], [4], -1)

    # Large constraints example (Simulated small for validation)
    # m=5, n=5, H=[3], V=[3]
    # H: 1,3,5 -> Gaps {2, 4}
    # V: 1,3,5 -> Gaps {2, 4}
    # Max gap 4 -> Area 16
    run_test(3, 5, 5, [3], [3], 16)
