class Solution(object):
    def smallestNumber(self, num, t):
        def get_factors(val):
            r2 = r3 = r5 = r7 = 0
            while val % 2 == 0: r2 += 1; val //= 2
            while val % 3 == 0: r3 += 1; val //= 3
            while val % 5 == 0: r5 += 1; val //= 5
            while val % 7 == 0: r7 += 1; val //= 7
            if val > 1: return -1
            return (r2, r3, r5, r7)
            
        factors = get_factors(t)
        if factors == -1: return "-1"
        R2, R3, R5, R7 = factors
        
        factors_of = {
            '1':(0,0,0,0), '2':(1,0,0,0), '3':(0,1,0,0), '4':(2,0,0,0), 
            '5':(0,0,1,0), '6':(1,1,0,0), '7':(0,0,0,1), '8':(3,0,0,0), '9':(0,2,0,0)
        }
        
        if '0' not in num:
            c2=c3=c5=c7=0
            for char in num:
                df = factors_of[char]
                c2 += df[0]; c3 += df[1]; c5 += df[2]; c7 += df[3]
            if c2 >= R2 and c3 >= R3 and c5 >= R5 and c7 >= R7:
                return num

        memo = {}
        def get_min_len_23(r2, r3):
            r2, r3 = max(0, r2), max(0, r3)
            if (r2, r3) in memo: return memo[(r2, r3)]
            ans = float('inf')
            for sixes in range(min(r2, r3) + 1):
                rem2, rem3 = max(0, r2 - sixes), max(0, r3 - sixes)
                req = sixes + (rem2 + 2) // 3 + (rem3 + 1) // 2
                if req < ans: ans = req
            memo[(r2, r3)] = ans
            return ans

        def get_min_len(r2, r3, r5, r7):
            return get_min_len_23(r2, r3) + max(0, r5) + max(0, r7)

        n = len(num)
        pref_c2, pref_c3, pref_c5, pref_c7 = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
        
        first_zero = num.find('0')
        if first_zero == -1: first_zero = n
            
        for i in range(first_zero):
            df = factors_of[num[i]]
            pref_c2[i+1] = pref_c2[i] + df[0]
            pref_c3[i+1] = pref_c3[i] + df[1]
            pref_c5[i+1] = pref_c5[i] + df[2]
            pref_c7[i+1] = pref_c7[i] + df[3]

        found = False
        ans_i, ans_d = -1, -1
        
        for i in range(min(n - 1, first_zero), -1, -1):
            curr_c2, curr_c3 = pref_c2[i], pref_c3[i]
            curr_c5, curr_c7 = pref_c5[i], pref_c7[i]
            
            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                df = factors_of[str(d)]
                rem2, rem3 = R2 - (curr_c2 + df[0]), R3 - (curr_c3 + df[1])
                rem5, rem7 = R5 - (curr_c5 + df[2]), R7 - (curr_c7 + df[3])
                
                if get_min_len(rem2, rem3, rem5, rem7) <= n - 1 - i:
                    ans_i, ans_d = i, d
                    found = True
                    break
            if found: break
                
        if found:
            res = list(num[:ans_i])
            res.append(str(ans_d))
            
            curr_c2 = pref_c2[ans_i] + factors_of[str(ans_d)][0]
            curr_c3 = pref_c3[ans_i] + factors_of[str(ans_d)][1]
            curr_c5 = pref_c5[ans_i] + factors_of[str(ans_d)][2]
            curr_c7 = pref_c7[ans_i] + factors_of[str(ans_d)][3]
            
            rem_len = n - 1 - ans_i
            for slot in range(rem_len):
                for d in range(1, 10):
                    df = factors_of[str(d)]
                    rem2, rem3 = R2 - (curr_c2 + df[0]), R3 - (curr_c3 + df[1])
                    rem5, rem7 = R5 - (curr_c5 + df[2]), R7 - (curr_c7 + df[3])
                    
                    if get_min_len(rem2, rem3, rem5, rem7) <= rem_len - 1 - slot:
                        res.append(str(d))
                        curr_c2 += df[0]; curr_c3 += df[1]
                        curr_c5 += df[2]; curr_c7 += df[3]
                        break
            return "".join(res)
        else:
            L = max(n + 1, get_min_len(R2, R3, R5, R7))
            res = []
            curr_c2 = curr_c3 = curr_c5 = curr_c7 = 0
            
            for slot in range(L):
                for d in range(1, 10):
                    df = factors_of[str(d)]
                    rem2, rem3 = R2 - (curr_c2 + df[0]), R3 - (curr_c3 + df[1])
                    rem5, rem7 = R5 - (curr_c5 + df[2]), R7 - (curr_c7 + df[3])
                    
                    if get_min_len(rem2, rem3, rem5, rem7) <= L - 1 - slot:
                        res.append(str(d))
                        curr_c2 += df[0]; curr_c3 += df[1]
                        curr_c5 += df[2]; curr_c7 += df[3]
                        break
            return "".join(res)

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, num, t, expected):
        result = solver.smallestNumber(num, t)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}:")
        print(f"  Input:    num = '{num}', t = {t}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, "1234", 256, "1488")
    # Example 2
    run_test(2, "12355", 50, "12355")
    # Example 3
    run_test(3, "11111", 26, "-1")
    # Custom Case 4 (Needs string len incremented)
    run_test(4, "99", 2, "112")
