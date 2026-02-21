class Solution(object):
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        prime_count = 0

        for i in range(left, right + 1):
            if bin(i).count("1") in primes:
                prime_count += 1
        
        return prime_count


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, left, right, expected):
        result = solver.countPrimeSetBits(left, right)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Range [{left}, {right}] -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # 6(110)->2, 7(111)->3, 8(1000)->1, 9(1001)->2, 10(1010)->2.
    # Primes: 2, 3, 2, 2. Total = 4.
    run_test(1, 6, 10, 4)

    # Example 2
    # 10(2), 11(3), 12(2), 13(3), 14(3), 15(4).
    # Primes: 2, 3, 2, 3, 3. Total = 5.
    run_test(2, 10, 15, 5)

    # Custom Case: Single Number
    # 21 -> 10101 (3 set bits, 3 is prime)
    run_test(3, 21, 21, 1)

    # Custom Case: Zero prime bits
    # 8 -> 1000 (1 set bit, 1 is NOT prime)
    run_test(4, 8, 8, 0)
