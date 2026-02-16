class Solution:

    def reverseBits(self, n):
        result = 0

        for _ in range(32):
            result = result << 1

            bit = n & 1

            result = result | bit

            n = n >> 1

        return result


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.reverseBits(n)
        status = "PASS" if result == expected else "FAIL"

        # Formatting for binary visualization
        bin_n = format(n, "032b")
        bin_res = format(result, "032b")

        print(f"Test Case {case_num}:")
        print(f"Input:    {n} ({bin_n})")
        print(f"Output:   {result} ({bin_res})")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    # Input: 43261596 (00000010100101000001111010011100)
    # Expected: 964176192 (00111001011110000010100101000000)
    run_test(1, 43261596, 964176192)

    # Example 2
    # Input: -3 
    # 2147483644 -> 1073741822
    run_test(2, 2147483644, 1073741822)

    # Custom Case: 0
    run_test(3, 0, 0)

    # Custom Case: 1 (00...001) -> (10...000) which is 2^31
    # 2147483648
    run_test(4, 1, 2147483648)
