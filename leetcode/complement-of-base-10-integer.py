class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        
        mask = (1 << n.bit_length()) - 1

        return n ^ mask


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, n, expected):
        result = solver.bitwiseComplement(n)
        status = "PASS" if result == expected else "FAIL"
        
        # Binary representations for clearer debugging output
        bin_n = bin(n)[2:]
        bin_res = bin(result)[2:]
        
        print(f"Test Case {case_num}: n={n} ({bin_n})")
        print(f"  Output:   {result} ({bin_res})")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # 5 -> "101". Complement is "010" -> 2
    run_test(1, 5, 2)

    # Example 2
    # 7 -> "111". Complement is "000" -> 0
    run_test(2, 7, 0)

    # Example 3
    # 10 -> "1010". Complement is "0101" -> 5
    run_test(3, 10, 5)
    
    # Custom Case: The edge case
    run_test(4, 0, 1)