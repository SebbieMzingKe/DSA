class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        max_len = 0

        current_run = 0
        for i in range(n):
            if i > 0 and s[i] == s[i - 1]:
                current_run += 1
            else:
                current_run = 1
            max_len = max(max_len, current_run)

        pairs = [("a", "b", "c"), ("a", "c", "b"), ("b", "c", "a")]
        for c1, c2, forbidden in pairs:
            diff_map = {0: -1}
            balance = 0
            for i, char in enumerate(s):
                if char == forbidden:
                    balance = 0
                    diff_map = {0: i}
                else:
                    if char == c1:
                        balance += 1
                    elif char == c2:
                        balance -= 1

                    if balance in diff_map:
                        max_len = max(max_len, i - diff_map[balance])
                    else:
                        diff_map[balance] = i

        state_map = {(0, 0): -1}
        ca, cb, cc = 0, 0, 0
        for i, char in enumerate(s):
            if char == "a":
                ca += 1
            elif char == "b":
                cb += 1
            elif char == "c":
                cc += 1

            state = (ca - cb, ca - cc)
            if state in state_map:
                max_len = max(max_len, i - state_map[state])
            else:
                state_map[state] = i

        return max_len


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.longestBalanced(s)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: '{s}' -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # "abba" -> 'a':2, 'b':2 (Case 2). Len 4.
    run_test(1, "abbac", 4)

    # Example 2
    # "abc" -> 'a':1, 'b':1, 'c':1 (Case 3). Len 3.
    run_test(2, "aabcc", 3)

    # Example 3
    # "ab" -> 'a':1, 'b':1 (Case 2). Len 2.
    run_test(3, "aba", 2)

    # Custom Case: Single char run
    # "aaaaa" -> Len 5.
    run_test(4, "aaaaa", 5)

    # Custom Case: Complex Interleaved
    # "aabbc" -> "aabb" (Case 2) Len 4. "aabbc" (Case 3) unbalanced.
    run_test(5, "aabbc", 4)

    # Custom Case: Case 2 Reset
    # Index 2 - (-1) = 3.
    # "acb" has a:1, b:1, c:1. It IS balanced Output should be 3.
    run_test(6, "acb", 3)
