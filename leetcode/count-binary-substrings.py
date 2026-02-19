class Solution(object):
    def countBinarySubstrings(self, s):
        ans = 0
        prev_run = 0
        curr_run = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run += 1
            
            else:
                ans += min(prev_run, curr_run)
                prev_run = curr_run
                curr_run = 1
        ans += min(prev_run, curr_run)
        return ans

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.countBinarySubstrings(s)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Input '{s}' -> Output {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Blocks: 2, 2, 2, 2 -> min(2,2) + min(2,2) + min(2,2) = 2 + 2 + 2 = 6
    run_test(1, "00110011", 6)

    # Example 2
    # Blocks: 1, 1, 1, 1, 1 -> min(1,1)*4 = 4
    run_test(2, "10101", 4)

    # Custom Case: Single block
    # Blocks: 3 -> loop logic applies min(0, 3) = 0
    run_test(3, "000", 0)

    # Custom Case: Uneven blocks
    # Blocks: 3, 1 -> min(3, 1) = 1 ("01")
    run_test(4, "0001", 1)
