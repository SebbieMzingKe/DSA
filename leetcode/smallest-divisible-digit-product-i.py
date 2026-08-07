class Solution(object):
    def smallestNumber(self, n, t):
        def digit_product(num):
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            return prod
            
        current = n
        while True:
            if digit_product(current) % t == 0:
                return current
            current += 1

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, n, t, expected):
        result = solver.smallestNumber(n, t)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    n = {n}, t = {t}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 10, 2, 10)

    # Example 2
    run_test(2, 15, 3, 16)

    # Custom Case 3: Need to jump several numbers
    run_test(3, 11, 4, 14)
    
    # Custom Case 4: A number where t is larger than n
    run_test(4, 3, 7, 7)

