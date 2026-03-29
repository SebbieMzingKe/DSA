class Solution(object):
    def canBeEqual(self, s1, s2):
        even_match = sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]])
        odd_match = sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        return even_match and odd_match


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s1, s2, expected):
        result = solver.canBeEqual(s1, s2)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}: s1='{s1}', s2='{s2}'")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # s1 even: a, c -> sorted: a, c. s2 even: c, a -> sorted: a, c (Match)
    # s1 odd:  b, d -> sorted: b, d. s2 odd:  d, b -> sorted: b, d (Match)
    run_test(1, "abcd", "cdab", True)

    # Example 2
    # s1 even: a, c -> sorted: a, c. s2 even: d, c -> sorted: c, d (Fail)
    run_test(2, "abcd", "dacb", False)

    # Custom Case: Strings are already equal
    run_test(3, "leet", "leet", True)

    # Custom Case: Only odd indices swapped
    run_test(4, "xxyz", "xzyx", True)
