class Solution(object):
    def minMirrorPairDistance(self, nums):
        seen = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            if num in seen:
                dist = j - seen[num]
                if dist < min_dist:
                    min_dist = dist
                    
            rev_num = int(str(num)[::-1])
            seen[rev_num] = j
            
        return -1 if min_dist == float('inf') else min_dist

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, expected):
        result = solver.minMirrorPairDistance(nums)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [12, 21, 45, 33, 54], 1)

    # Example 2 (Trailing zero test)
    run_test(2, [120, 21], 1)

    # Example 3 (Asymmetry failure)
    run_test(3, [21, 120], -1)
    
    # Custom Case 4: Multiple matches, ensuring we keep the closest one
    run_test(4, [10, 5, 5, 1], 3) # reverse(10) is 1. (0, 3) -> distance 3