class Solution(object):
    def numSteps(self, s):
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry

            if digit == 1:
                steps += 2
                carry = 1
            
            else:
                steps += 1
        
        return steps + carry

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.numSteps(s)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    '{s}'")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # 13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1 (6 steps)
    run_test(1, "1101", 6)

    # Example 2
    # 2 -> 1 (1 step)
    run_test(2, "10", 1)

    # Example 3
    # 1 is already 1 (0 steps)
    run_test(3, "1", 0)

    # Custom Case: Long string of 1s
    # "111" (7) -> 8 -> 4 -> 2 -> 1 (4 steps)
    run_test(4, "111", 4)

    # Custom Case: Single carry propagation
    # "1011" (11) -> 12 -> 6 -> 3 -> 4 -> 2 -> 1 (6 steps)
    run_test(5, "1011", 6)
