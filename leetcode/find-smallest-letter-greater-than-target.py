import bisect


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect_right(letters, target)

        return letters[index % len(letters)]

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, letters, target, expected):
        # You can swap this to solver.nextGreatestLetterBinary to test the optimization
        result = solver.nextGreatestLetter(letters, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: letters={letters}, target='{target}' -> Output='{result}' (Expected='{expected}') -> {status}")

    # Example 1
    # 'c' is the first letter greater than 'a'
    run_test(1, ["c", "f", "j"], "a", "c")

    # Example 2
    # 'f' is the first letter greater than 'c'
    run_test(2, ["c", "f", "j"], "c", "f")

    # Example 3 (Wrap Around)
    # Target 'z' is larger than everything. Return letters[0] -> 'x'
    run_test(3, ["x", "x", "y", "y"], "z", "x")
    
    # Edge Case: Target is smaller than everything
    run_test(4, ["a", "b", "c"], "@", "a") # '@' is ASCII smaller than 'a'