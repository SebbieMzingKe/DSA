class Solution(object):
    def uniformArray(self, nums1):
        return True

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums1, expected):
        result = solver.uniformArray(nums1)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    nums1 = {nums1}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1: Mix of even and odd
    run_test(1, [2, 3], True)

    # Example 2: All even
    run_test(2, [4, 6], True)

    # Custom Case 3: All odd
    run_test(3, [1, 3, 5, 7], True)
    
    # Custom Case 4: Single element
    run_test(4, [10], True)