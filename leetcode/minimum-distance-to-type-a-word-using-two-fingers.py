class Solution(object):
    def minimumDistance(self, word):
        def get_dist(p1, p2):
            if p1 == 26: return 0
            x1, y1 = p1 // 6, p1 % 6
            x2, y2 = p2 // 6, p2 % 6
            return abs(x1 - x2) + abs(y1 - y2)

        memo = {}
        def dp(i, other):
            if i == len(word): return 0
            if (i, other) in memo: return memo[(i, other)]
            
            curr = ord(word[i]) - 65
            prev = ord(word[i-1]) - 65
            
            cost1 = get_dist(prev, curr) + dp(i + 1, other)
            cost2 = get_dist(other, curr) + dp(i + 1, prev)
            
            memo[(i, other)] = min(cost1, cost2)
            return memo[(i, other)]
            
        return dp(1, 26)

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, word, expected):
        result = solver.minimumDistance(word)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input word: '{word}'")
        print(f"  Output:     {result}")
        print(f"  Expected:   {expected}")
        print(f"  Status:     {status}\n")

    # Example 1
    run_test(1, "CAKE", 3)

    # Example 2
    run_test(2, "HAPPY", 6)
    
    # Custom Case 3: Same letter repeated (fingers shouldn't move)
    run_test(3, "AAAAA", 0)
    
    # Custom Case 4: Long alternating word
    run_test(4, "QWERTYUIOP", 14)
