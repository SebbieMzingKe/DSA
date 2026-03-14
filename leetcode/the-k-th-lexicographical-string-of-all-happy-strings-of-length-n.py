class Solution(object):
    def getHappyString(self, n, k):
        max_strings = 3 * (2 ** (n - 1))
        if k > max_strings:
            return ""
            
        happy_strings = []
        
        def backtrack(current_string):
            if len(happy_strings) == k:
                return
            if len(current_string) == n:
                happy_strings.append(current_string)
                return
                
            for char in ['a', 'b', 'c']:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
                    
        backtrack("")
        return happy_strings[k - 1]

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, n, k, expected):
        result = solver.getHappyString(n, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: n={n}, k={k}")
        print(f"  Output:   '{result}'")
        print(f"  Expected: '{expected}'")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 1, 3, "c")

    # Example 2 (k is too large)
    run_test(2, 1, 4, "")

    # Example 3
    run_test(3, 3, 9, "cab")
    
    # Custom Case: The very first string
    run_test(4, 3, 1, "aba")
    
    # Custom Case: Max constraints (n=10, k=100)
    run_test(5, 10, 100, "abacbabacb")