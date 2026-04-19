class Solution(object):
    def mirrorDistance(self, n):
        reversed_n = int(str(n)[::-1])
        return abs(n - reversed_n)

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, n, expected):
        result = solver.mirrorDistance(n)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input n:  {n}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 25, 27)

    # Example 2 (Testing trailing zeros)
    run_test(2, 10, 9)

    # Example 3 (Single digit)
    run_test(3, 7, 0)
    
    # Custom Case 4 (Palindrome)
    run_test(4, 121, 0)
