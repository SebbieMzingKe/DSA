class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = {}
            max_freq = 0
            
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                max_freq = max(max_freq, freq[char])
                
                current_len = j - i + 1
                distinct_count = len(freq)
                
                if max_freq * distinct_count == current_len:
                    if current_len > max_len:
                        max_len = current_len
        return max_len


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.longestBalanced(s)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: '{s}' -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # "abba" -> 'a':2, 'b':2. Balanced. Length 4.
    run_test(1, "abbac", 4)

    # Example 2
    # "zabc" -> 'z':1, 'a':1, 'b':1, 'c':1. Balanced. Length 4.
    run_test(2, "zzabccy", 4)

    # Example 3
    # "aba" -> 'a':2, 'b':1. Not balanced.
    # Substring "ab" or "ba" is balanced. Length 2.
    run_test(3, "aba", 2)

    # Custom Case: Single character
    run_test(4, "a", 1)

    # Custom Case: All same
    # "aaaa" -> 4 * 1 = 4. Balanced.
    run_test(5, "aaaa", 4)

    # Custom Case: Full mix
    # "aabbccc" -> Not balanced. "aabb" is 4.
    run_test(6, "aabbccc", 4)
