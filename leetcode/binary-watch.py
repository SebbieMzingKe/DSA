class Solution(object):
    def readBinaryWatch(self, turnedOn):
        times =  []

        for h in range(12):
            for m in range(60):

                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:

                    times.append("%d:%02d" % (h, m))
        
        return times


if __name__ == "__main__":
    solver = Solution()
    def run_test(case_num, turnedOn, expected):

        result = sorted(solver.readBinaryWatch(turnedOn))
        expected = sorted(expected)
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: turnedOn={turnedOn}")
        print(f"   Result:   {result}")
        print(f"   Expected: {expected}")
        print(f"   Status:   {status}\n")

    # Example 1
    # 1 LED on: Could be hour 1, 2, 4, 8 OR minute 1, 2, 4, 8, 16, 32
    expected_1 = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    run_test(1, 1, expected_1)

    # Example 2
    # 9 LEDs on: Impossible. 
    # Max hour bits (11 -> 1011) is 3. Max minute bits (59 -> 111011) is 5.
    # Total max bits is 3 + 5 = 8. So 9 is impossible.
    run_test(2, 9, [])
    
    # Custom Case: 0 LEDs
    # Only midnight 0:00 has 0 bits set.
    run_test(3, 0, ["0:00"])