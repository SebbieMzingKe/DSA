class Solution(object):
    def findDifferentBinaryString(self, nums):
        return "".join(["1" if nums[i][i] == "0" else "0" for i in range(len(nums))])


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums):
        result = solver.findDifferentBinaryString(nums)
        n = len(nums)

        is_correct_length = len(result) == n
        is_binary = all(char in "01" for char in result)
        is_unique = result not in nums

        status = "PASS" if (is_correct_length and is_binary and is_unique) else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:  {nums}")
        print(f"  Output: '{result}'")
        print(f"  Status: {status}\n")

    # Example 1
    run_test(1, ["01", "10"])

    # Example 2
    run_test(2, ["00", "01"])

    # Example 3
    run_test(3, ["111", "011", "001"])

    # Custom Case: n=4
    run_test(4, ["0000", "1111", "1010", "0101"])

    # Custom Case: n=1
    run_test(5, ["0"])
