class Solution(object):
    def totalWaviness(self, num1, num2):
        def count_waviness(limit_str):
            if limit_str == "0":
                return 0
            
            memo = {}

            def dp(pos, is_tight, is_started, prev1, prev2):
                if pos == len(limit_str):
                    return (1, 0)
                
                state = (pos, is_tight, is_started, prev1, prev2)
                if state in memo:
                    return memo[state]


                limit_digit = int(limit_str[pos]) if is_tight else 9
                total_count = 0
                total_wav = 0

                for d in range(limit_digit + 1):
                    new_tight = is_tight and (d == limit_digit)
                    new_started = is_started or (d > 0)
                    if not new_started:
                        c, w = dp(pos + 1, new_tight, False, -1, -1)
                        total_count += c
                        total_wav += w

                    else:
                        new_prev1 = d
                        new_prev2 = prev1 if  is_started else -1
                        is_peak = (prev2 != -1 and prev1 > prev2 and prev1 > d)
                        is_valley = (prev2 != -1 and prev1 < prev2 and prev1 < d)
                        current_waviness = 1 if (is_peak or is_valley) else 0
                        c, w = dp(pos + 1, new_tight, True, new_prev1, new_prev2)
                        total_count += c
                        total_wav +=w + (c * current_waviness)
                
                memo[state] = (total_count, total_wav)
                return memo[state]
            return dp(0, True, False,-1, -1)[1]
        return count_waviness(str(num2)) - count_waviness(str(num1 - 1))


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, num1, num2, expected):
        import time
        start_time = time.time()
        result = solver.totalWaviness(num1, num2)
        end_time = time.time()
        
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Range:    [{num1}, {num2}]")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status} ({end_time - start_time:.5f}s)\n")

    # Example 1
    run_test(1, 120, 130, 3)

    # Example 2
    run_test(2, 198, 202, 3)

    # Example 3
    run_test(3, 4848, 4848, 2)
    
    # Custom Case 4: Max Constraints Performance Check
    run_test(4, 1, 10**15, 1066666666666665)    