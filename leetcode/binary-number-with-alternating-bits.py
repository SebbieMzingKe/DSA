class Solution(object):
    def hasAlternatingBits(self, n):

        last_bit = n & 1
        n = n >> 1

        while n > 0:
            current_bit = n & 1
            if current_bit == last_bit:
                return False

            last_bit = current_bit
            n = n >> 1

        return True

    # xor trick.
    # def hasAlternatingBitsXOR(self, n):
    #     temp = n ^ (n >> 1)
    #     return (temp & (temp + 1)) == 0


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.hasAlternatingBits(n)
        status = "PASS" if result == expected else "FAIL"

        # Visualize the binary
        binary_rep = bin(n)[2:]
        print(
            f"Test Case {case_num}: Input {n} ({binary_rep}) -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1: 5 is 101 (Alternating)
    run_test(1, 5, True)

    # Example 2: 7 is 111 (Not alternating)
    run_test(2, 7, False)

    # Example 3: 11 is 1011 (Adjacent 1s at the end broken)
    run_test(3, 11, False)

    # Custom Case: 10 is 1010 (Alternating)
    run_test(4, 10, True)

    # Custom Case: 4 is 100 (Adjacent 0s broken)
    run_test(5, 4, False)
