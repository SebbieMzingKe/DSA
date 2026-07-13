class Solution(object):
    def sequentialDigits(self, low, high):
        sample = "123456789"
        ans = []
        
        low_len = len(str(low))
        high_len = len(str(high))
        
        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                
                if low <= num <= high:
                    ans.append(num)
                    
        return ans

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, low, high, expected):
        result = solver.sequentialDigits(low, high)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Range:    [{low}, {high}]")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 100, 300, [123, 234])

    # Example 2
    run_test(2, 1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345])

    # Custom Case 3: Exactly matching bounds
    run_test(3, 12, 89, [12, 23, 34, 45, 56, 67, 78, 89])
    
    # Custom Case 4: No valid sequential digits in range
    run_test(4, 300, 340, [])