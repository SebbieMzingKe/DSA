class Solution(object):
    def minimumCost(self, nums):
        head_cost = nums[0]
        
        # Find two smallest in nums[1:]
        min1 = float('inf')
        min2 = float('inf')
        
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
                
        return head_cost + min1 + min2

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, expected):
        result = solver.minimumCost(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {nums} -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # First part [1]. Rest is [2, 3, 12]. Smallest are 2 and 3.
    # Total = 1 + 2 + 3 = 6.
    run_test(1, [1, 2, 3, 12], 6)

    # Example 2
    # First part [5]. Rest is [4, 3]. Smallest are 3 and 4.
    # Total = 5 + 3 + 4 = 12.
    run_test(2, [5, 4, 3], 12)
    
    # Example 3
    # First part [10]. Rest is [3, 1, 1]. Smallest are 1 and 1.
    # Total = 10 + 1 + 1 = 12.
    run_test(3, [10, 3, 1, 1], 12)