class Solution(object):
    def leftRightDifference(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for num in nums:
            right_sum = total_sum - left_sum- num
            ans.append(abs(left_sum - right_sum))
            left_sum += num

        return ans


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, expected):
        result = solver.leftRightDifference(nums)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input nums: {nums}")
        print(f"  Output:     {result}")
        print(f"  Expected:   {expected}")
        print(f"  Status:     {status}\n")

    # Example 1
    run_test(1, [10, 4, 8, 3], [15, 1, 11, 22])

    # Example 2
    run_test(2, [1], [0])

    # Custom Case 3: All zeros
    run_test(3, [0, 0, 0, 0], [0, 0, 0, 0])
    
    # Custom Case 4: Increasing sequence
    run_test(4, [1, 2, 3, 4, 5], [14, 11, 6, 1, 10])