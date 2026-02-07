class Solution(object):
    def minimumDeletions(self, s):
        b_count = 0
        min_deletions = 0

        for char in s:
            if char == 'b':
                b_count += 1

            else:
                min_deletions = min(min_deletions + 1, b_count)
        
        return min_deletions

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, s, expected):
        result = solver.minimumDeletions(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: '{s}' -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # We can delete 'b' at index 2 and 'b' at index 6 -> "aaabbb" (2 deletions)
    # OR delete 'a' at index 3 and 'a' at index 6 -> "aabbbb" (2 deletions)
    run_test(1, "aababbab", 2)

    # Example 2
    # Delete the two leading 'b's -> "aaaaabb"
    run_test(2, "bbaaaaabb", 2)
    
    # Custom Case: Already balanced
    run_test(3, "aaabbb", 0)

    # Custom Case: All 'b's then 'a's (Worst case)
    # "bbbaaa" -> delete 3 'b's OR 3 'a's -> cost 3
    run_test(4, "bbbaaa", 3)