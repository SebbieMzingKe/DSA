class Solution(object):
    def totalWaviness(self, num1, num2):
        total_sum = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            if n < 3:
                continue
            for i in range(1, n - 1):
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    total_sum += 1
                elif s[i] < s[i-1] and s[i] < s[i+1]:
                    total_sum += 1
        return total_sum

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, num1, num2, expected):
        result = solver.totalWaviness(num1, num2)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Range:    [{num1}, {num2}]")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 120, 130, 3)

    # Example 2
    run_test(2, 198, 202, 3)

    # Example 3
    run_test(3, 4848, 4848, 2)
    
    # Custom Case 4: Numbers less than 3 digits
    run_test(4, 1, 99, 0)