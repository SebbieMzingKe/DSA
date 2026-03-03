class Solution(object):
    def findKthBit(self, n, k):
        if n == 1:
            return "0"

        length = (1 << n) - 1
        mid = (length // 2) + 1

        if k == mid:
            return "1"

        elif k < mid:
            return self.findKthBit(n - 1, k)
        
        else:
            mirrored_k = length - k + 1
            bit = self.findKthBit(n - 1, mirrored_k)

            return "0" if bit == "1" else "1"
            


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, n, k, expected):
        result = solver.findKthBit(n, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: n={n}, k={k} -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # S3 = "0111001", k=1 -> "0"
    run_test(1, 3, 1, "0")

    # Example 2
    # S4 = "011100110110001", k=11 -> "1"
    run_test(2, 4, 11, "1")

    # Custom Case: Middle of S3
    # S3 = "0111001", k=4 -> "1"
    run_test(3, 3, 4, "1")

    # Custom Case: Deep right side
    # n=2 is "011". n=1 is "0". 
    run_test(4, 2, 3, "1")