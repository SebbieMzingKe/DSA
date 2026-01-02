class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
    
if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.repeatedNTimes(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"test case {case_num}: {result} (expected: {expected}) -> {status}")

        # Example 1
    # n=2, len=4. Target is 3.
    nums1 = [1, 2, 3, 3]
    run_test(1, nums1, 3)
    
    # Example 2
    # n=3, len=6. Target is 2.
    nums2 = [2, 1, 2, 5, 3, 2]
    run_test(2, nums2, 2)
    
    # Example 3
    # n=4, len=8. Target is 5.
    nums3 = [5, 1, 5, 2, 5, 3, 5, 4]
    run_test(3, nums3, 5)