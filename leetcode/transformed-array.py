class Solution(object):
    def constructTransformedArray(self, nums):

        n = len(nums)
        result= [0] * n

        for i in range(n):
            target_index = (i + nums[i]) % n
            result[i] = nums[target_index]
        
        return result
    
if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, expected):
        result = solver.constructTransformedArray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: Input {nums} -> Output {result} (Expected: {expected}) -> {status}")

    # Example 1
    # i=0: move 3 right -> index 3 (val 1)
    # i=1: move 2 left -> index 3 (val 1)
    # i=2: move 1 right -> index 3 (val 1)
    # i=3: move 1 right -> index 0 (val 3)
    run_test(1, [3,-2,1,1], [1,1,1,3])

    # Example 2
    # i=0: move 1 left -> index 2 (val -1)
    # i=1: move 4 right -> index 2 (val -1)
    # i=2: move 1 left -> index 1 (val 4)
    run_test(2, [-1,4,-1], [-1,-1,4])

    # Custom Case: Zero movement
    # [0, 0, 0] should return [0, 0, 0]
    run_test(3, [0, 0, 0], [0, 0, 0])

    # Custom Case: Full wrap around
    # length 3, move 3 steps right -> lands on same index
    run_test(4, [3, 3, 3], [3, 3, 3])