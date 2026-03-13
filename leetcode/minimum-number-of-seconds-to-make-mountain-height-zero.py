import math


class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        fastest_worker = min(workerTimes)
        low = 1
        high = fastest_worker * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            total_reduced = 0
            for t in workerTimes:
                val = (mid * 2) // t
                x = (math.isqrt(1 + 4 * val) - 1) // 2
                total_reduced += x
                if total_reduced >= mountainHeight:
                    break
                    
            if total_reduced >= mountainHeight:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
    

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, mountainHeight, workerTimes, expected):
        import time

        start = time.time()
        result = solver.minNumberOfSeconds(mountainHeight, workerTimes)
        end = time.time()

        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: Height={mountainHeight}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status} ({end - start:.4f}s)\n")

    # Example 1
    run_test(1, 4, [2, 1, 1], 3)

    # Example 2
    run_test(2, 10, [3, 2, 2, 4], 12)

    # Example 3
    run_test(3, 5, [1], 15)

    # Custom Case: Large inputs (Performance Check)
    run_test(4, 100000, [1, 2, 3, 4, 5], 1183269229)
