class Solution(object):
    def minPartitions(self, n):
        return int(max(n))


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.minPartitions(n)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {n}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # Max digit in "32" is 3.
    run_test(1, "32", 3)

    # Example 2
    # Max digit in "82734" is 8.
    run_test(2, "82734", 8)

    # Example 3
    # Max digit is 9.
    run_test(3, "27346209830709182346", 9)

    # Custom Case: All same digits
    run_test(4, "55555", 5)

    # Custom Case: Single digit
    run_test(5, "1", 1)
