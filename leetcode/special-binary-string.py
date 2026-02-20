class Solution(object):
    def makeLargestSpecial(self, s):
        count = 0
        start = 0
        blocks = []

        for i, char in enumerate(s):
            count += 1 if char == "1" else -1

            if count == 0:
                inner_string = s[start + 1 : i]
                processed_inner = self.makeLargestSpecial(inner_string)

                blocks.append("1" + processed_inner + "0")

                start = i + 1
            
        blocks.sort(reverse = True)

        return "".join(blocks)

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.makeLargestSpecial(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}:")
        print(f"  Input:    {s}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # Decomposes into "10" and "1100" (which has inner "10").
    # Swap "10" and "1100" -> "110010" Wait, inner decomposition:
    # 11011000 -> blocks: "1 10 1100 0"? No, outer blocks are 1(10)(1100)0 -> 11100100
    run_test(1, "11011000", "11100100")

    # Example 2
    # Already sorted and primitive
    run_test(2, "10", "10")

    # Custom Case
    # Two independent blocks: "10" and "10" -> "1010"
    run_test(3, "1010", "1010")

    # Custom Case: Unsorted outer blocks
    # "10" followed by "1100" -> "101100"
    # Should sort to "1100" followed by "10" -> "110010"
    run_test(4, "101100", "110010")
