class Solution(object):
    def minOperations(self, s):
        diff0 = 0
        n = len(s)

        for i in range(n):
            if s[i] != str(i % 2):
                diff0 += 1
        
        return min(diff0, n -diff0)


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, s, expected):
        result = solver.minOperations(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: '{s}' -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # s = "0100". 
    # Target 0: "0101" -> 1 diff
    # Target 1: "1010" -> 3 diffs
    # Min is 1
    run_test(1, "0100", 1)

    # Example 2
    # s = "10". Already alternating. 0 diffs from Target 1.
    run_test(2, "10", 0)

    # Example 3
    # s = "1111". 
    # Target 0: "0101" -> 2 diffs
    # Target 1: "1010" -> 2 diffs
    # Min is 2
    run_test(3, "1111", 2)
    
    # Custom Case: All zeros
    # "00000" -> Target 0 ("01010") is 2 diffs. Target 1 ("10101") is 3 diffs.
    run_test(4, "00000", 2)