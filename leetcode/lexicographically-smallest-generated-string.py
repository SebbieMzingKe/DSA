class Solution(object):
    def generateString(self, str1, str2):
        n = len(str1)
        m = len(str2)
        L = n + m - 1

        fixed = ['?'] * L

        for i in range(n):
            if str1[i] == 'T':
                for k in range(m):
                    if fixed[i + k] != '?' and fixed[i + k] != str2:
                        return ""
                    fixed[i+ k] = str2[k]

        
        pi = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and str2[i] != str2[j]:
                j = pi[j - 1]
            
            if str2[i] == str2[j]:
                j += 1
            pi[i] = j

        aut = [[0] * 26 for _ in range(m)]

        for j in range(m):
            for c in range(26):
                char_c = chr(c + 97)
                k = j

                while k > 0 and str2[k] != char_c:
                    k = pi[k - 1]
                
                if str2[k] == char_c:
                    k += 1
                
                aut[j][c] = k

        dp = bytearray((L + 1) * m)
        for j in range(m):
            dp[L * m + j] = 1
        
        fixed_ords = [ord(c) - 97 if c != '?' else -1 for c in fixed]

        for i in range(L -1, -1, -1):
            f_c = fixed_ords[i]

            is_F = (i - m + 1 >= 0 and str1[i - m + 1] == 'F')

            row_offset = i * m
            next_row_offset = (i + 1) * m

            if f_c != -1:
                for j in range(m):
                    nj = aut[j][f_c]

                    if nj == m:
                        if is_F:
                            dp[row_offset + j] = 0
                        
                        else:
                            dp[row_offset + j] = dp[next_row_offset + pi[m - 1]]
                    else:
                        dp[row_offset + j] = dp[next_row_offset + nj]
            else:
                for j in range(m):
                    valid = 0
                    for c in range(26):
                        nj = aut[j][c]

                        if nj == m:
                            if is_F:
                                continue
                            
                            nj_next = pi[m - 1]
                        
                        else:
                            nj_next = nj

                        if dp[next_row_offset + nj_next]:
                            valid = 1
                            break
                    dp[row_offset + j] = valid

        if not dp[0]:
            return ""

        
        ans = []
        j = 0
        for i in range(L):
            f_c = fixed_ords[i]
            is_F = (i - m + 1 >= 0 and str1[i- m + 1] == 'F')
            next_row_offset = (i + 1) * m

            if f_c != -1:
                c = f_c
                ans.append(chr(c + 97))
                nj = aut[j][c]
                j = pi[m- 1] if nj == m else nj
            
            else:
                for c in range(26):
                    nj = aut[j][c]
                    if nj == m:
                        if is_F:
                            continue
                        nj_next = pi[m - 1]
                    else:
                        nj_next = nj
                    
                    if dp[next_row_offset + nj_next]:
                        ans.append(chr(c + 97))
                        j = nj_next
                        break
        return "".join(ans)


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, str1, str2, expected):
        result = solver.generateString(str1, str2)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    str1 = '{str1}', str2 = '{str2}'")
        print(f"  Output:   '{result}'")
        print(f"  Expected: '{expected}'")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, "TFTF", "ab", "ababa")

    # Example 2
    run_test(2, "TFTF", "abc", "")

    # Example 3
    run_test(3, "F", "d", "a")
    
    # Custom 1 (No conflict 'T' and 'F')
    run_test(4, "TF", "a", "ab")