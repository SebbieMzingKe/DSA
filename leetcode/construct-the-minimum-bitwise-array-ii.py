class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:

                temp = n
                idx = 0
                while (temp & 1):
                    temp >>= 1
                    idx += 1
                

                ans.append(n - (1 << (idx - 1)))
        return ans

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, expected):
        result = solver.minBitwiseArray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # 2 -> -1
    # 3 (11) -> Trailing ones len 2. Flip bit 1 (val 2). 3-2=1.
    # 5 (101) -> Trailing ones len 1. Flip bit 0 (val 1). 5-1=4.
    # 7 (111) -> Trailing ones len 3. Flip bit 2 (val 4). 7-4=3.
    run_test(1, [2, 3, 5, 7], [-1, 1, 4, 3])

    # Example 2
    # 11 (1011) -> 1s len 2. Flip bit 1 (val 2). 11-2=9.
    # 13 (1101) -> 1s len 1. Flip bit 0 (val 1). 13-1=12.
    # 31 (11111)-> 1s len 5. Flip bit 4 (val 16). 31-16=15.
    run_test(2, [11, 13, 31], [9, 12, 15])
    
    # Large Number Test (Logic Check)
    # 10^9 + 7 is 1000000007 (Binary ends in ...0111)
    # Trailing ones len 3. Flip bit 2 (val 4). Result 1000000003.
    # Check: 1000000003 | 1000000004 = 1000000007. Correct.
    run_test(3, [1000000007], [1000000003])