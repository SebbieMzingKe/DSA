class Solution(object):
    def getMinDistance(self, nums, target, start):
        n = len(nums)

        for dist in range(n):
            if start + dist < n and nums[start + dist] == target:
                return dist
            if start - dist >= 0 and nums[start - dist] == target:
                return dist

        return -1

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, target, start, expected):
        result = solver.getMinDistance(nums, target, start)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    nums = {nums}, target = {target}, start = {start}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 2, 3, 4, 5], 5, 3, 1)

    # Example 2
    run_test(2, [1], 1, 0, 0)

    # Example 3
    run_test(3, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 0)
    
    # Custom Case 4: Target is far to the left
    run_test(4, [5, 2, 3, 4, 1], 5, 4, 4)
    
    # Custom Case 5: Target appears on both sides, left is closer
    run_test(5, [1, 5, 3, 4, 5, 6, 7], 5, 2, 1)