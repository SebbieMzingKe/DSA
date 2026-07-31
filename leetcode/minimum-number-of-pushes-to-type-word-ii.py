from collections import Counter


class Solution(object):
    def minimmPushes(self, word):
        freq = Counter(word)
        counts = sorted(freq.values(), reverse=True)

        total_pushes = 0

        for i, count in enumerate(counts):
            cost = (i // 8) + 1
            total_pushes += count * cost

        return total_pushes


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, word, expected):
        result = solver.minimmPushes(word)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    word = \"{word}\"")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1: 5 distinct characters (all fit on cost 1)
    run_test(1, "abcde", 5)

    # Example 2: 3 distinct characters repeated (all fit on cost 1)
    run_test(2, "xyzxyzxyzxyz", 12)

    # Example 3: Mix of characters spilling into cost 2
    run_test(3, "aabbccddeeffgghhiiiiii", 24)
    
    # Custom Case 4: All 26 letters of the alphabet exactly once
    # Expected: 8*1 + 8*2 + 8*3 + 2*4 = 8 + 16 + 24 + 8 = 56
    run_test(4, "abcdefghijklmnopqrstuvwxyz", 56)