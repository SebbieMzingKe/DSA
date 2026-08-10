class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed and suf[i + 1] >= m - 1 - j:
                ans.append(i)
                j += 1
                changed = True

        if len(ans) == m:
            return ans

        return []


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, word1, word2, expected):
        result = solver.validSequence(word1, word2)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    word1 = '{word1}', word2 = '{word2}'")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, "vbcca", "abc", [0, 1, 2])

    # Example 2
    run_test(2, "bacdc", "abc", [1, 2, 4])

    # Example 3
    run_test(3, "aaaaaa", "aaabc", [])

    # Example 4
    run_test(4, "abc", "ab", [0, 1])

    # Custom Case 5: Mismatch used on the very last character
    run_test(5, "abcdex", "abcdey", [0, 1, 2, 3, 4, 5])
