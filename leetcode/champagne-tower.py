class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        tower = [[0.0] * 102 for _ in range(102)]
        tower[0][0] = float(poured)
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                overflow = (tower[r][c] - 1.0) / 2.0
                if overflow > 0:
                    tower[r+1][c] += overflow
                    tower[r+1][c+1] += overflow
                    
        return min(1.0, tower[query_row][query_glass])


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, poured, r, c, expected):
        result = solver.champagneTower(poured, r, c)

        status = "PASS" if abs(result - expected) < 1e-5 else "FAIL"
        print(f"Test Case {case_num}: Poured={poured} -> Glass({r},{c}) = {result:.5f} (Expected: {expected:.5f}) -> {status}")

    # Example 1
    # Poured 1. Top glass takes 1. 0 overflow. Row 1 glasses get 0.
    run_test(1, 1, 1, 1, 0.0)

    # Example 2
    # Poured 2. Top takes 1. Overflow 1. Splits 0.5 to (1,0) and 0.5 to (1,1).
    run_test(2, 2, 1, 1, 0.5)

    # Example 3
    # Massive pour. Everything should be full.
    run_test(3, 100000009, 33, 17, 1.0)
    
    # Custom Case: Center flow
    # Poured 4. 
    # Row 0: 4 -> Holds 1, Overflows 3.
    # Row 1: (1.5, 1.5).
    # Row 1 (0): 1.5 -> Holds 1, Overflows 0.5 -> sends 0.25 to (2,0) and (2,1).
    # Row 1 (1): 1.5 -> Holds 1, Overflows 0.5 -> sends 0.25 to (2,1) and (2,2).
    # Row 2 (1) receives 0.25 + 0.25 = 0.5.
    run_test(4, 4, 2, 1, 0.5)