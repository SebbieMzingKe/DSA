    package main

import (
	"fmt"
)

type Solution struct{}

func getFactors(val int) (r2, r3, r5, r7 int, ok bool) {
	for val%2 == 0 {
		r2++
		val /= 2
	}
	for val%3 == 0 {
		r3++
		val /= 3
	}
	for val%5 == 0 {
		r5++
		val /= 5
	}
	for val%7 == 0 {
		r7++
		val /= 7
	}
	if val > 1 {
		return 0, 0, 0, 0, false
	}
	return r2, r3, r5, r7, true
}

var factorsOf = map[byte][4]int{
	'1': {0, 0, 0, 0},
	'2': {1, 0, 0, 0},
	'3': {0, 1, 0, 0},
	'4': {2, 0, 0, 0},
	'5': {0, 0, 1, 0},
	'6': {1, 1, 0, 0},
	'7': {0, 0, 0, 1},
	'8': {3, 0, 0, 0},
	'9': {0, 2, 0, 0},
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type pair struct{ a, b int }

// smallestNumber mirrors Solution.smallestNumber from the Python version.
func (s *Solution) smallestNumber(num string, t int) string {
	R2, R3, R5, R7, ok := getFactors(t)
	if !ok {
		return "-1"
	}

	// --- fast path: num itself (with no zero digits) already satisfies t ---
	if !containsZero(num) {
		c2, c3, c5, c7 := 0, 0, 0, 0
		for i := 0; i < len(num); i++ {
			df := factorsOf[num[i]]
			c2 += df[0]
			c3 += df[1]
			c5 += df[2]
			c7 += df[3]
		}
		if c2 >= R2 && c3 >= R3 && c5 >= R5 && c7 >= R7 {
			return num
		}
	}

	memo := make(map[pair]int)

	var getMinLen23 func(r2, r3 int) int
	getMinLen23 = func(r2, r3 int) int {
		r2 = maxInt(0, r2)
		r3 = maxInt(0, r3)
		key := pair{r2, r3}
		if v, found := memo[key]; found {
			return v
		}
		ans := int(^uint(0) >> 1) // max int
		for sixes := 0; sixes <= minInt(r2, r3); sixes++ {
			rem2 := maxInt(0, r2-sixes)
			rem3 := maxInt(0, r3-sixes)
			req := sixes + (rem2+2)/3 + (rem3+1)/2
			if req < ans {
				ans = req
			}
		}
		memo[key] = ans
		return ans
	}

	getMinLen := func(r2, r3, r5, r7 int) int {
		return getMinLen23(r2, r3) + maxInt(0, r5) + maxInt(0, r7)
	}

	n := len(num)
	prefC2 := make([]int, n+1)
	prefC3 := make([]int, n+1)
	prefC5 := make([]int, n+1)
	prefC7 := make([]int, n+1)

	firstZero := indexOfZero(num)
	if firstZero == -1 {
		firstZero = n
	}

	for i := 0; i < firstZero; i++ {
		df := factorsOf[num[i]]
		prefC2[i+1] = prefC2[i] + df[0]
		prefC3[i+1] = prefC3[i] + df[1]
		prefC5[i+1] = prefC5[i] + df[2]
		prefC7[i+1] = prefC7[i] + df[3]
	}

	found := false
	ansI, ansD := -1, -1

	startI := minInt(n-1, firstZero)
	for i := startI; i >= 0; i-- {
		currC2, currC3 := prefC2[i], prefC3[i]
		currC5, currC7 := prefC5[i], prefC7[i]

		startD := int(num[i]-'0') + 1
		for d := startD; d < 10; d++ {
			df := factorsOf[byte('0' + d)]
			rem2 := R2 - (currC2 + df[0])
			rem3 := R3 - (currC3 + df[1])
			rem5 := R5 - (currC5 + df[2])
			rem7 := R7 - (currC7 + df[3])

			if getMinLen(rem2, rem3, rem5, rem7) <= n-1-i {
				ansI, ansD = i, d
				found = true
				break
			}
		}
		if found {
			break
		}
	}

	if found {
		res := []byte(num[:ansI])
		res = append(res, byte('0'+ansD))

		df0 := factorsOf[byte('0'+ansD)]
		currC2 := prefC2[ansI] + df0[0]
		currC3 := prefC3[ansI] + df0[1]
		currC5 := prefC5[ansI] + df0[2]
		currC7 := prefC7[ansI] + df0[3]

		remLen := n - 1 - ansI
		for slot := 0; slot < remLen; slot++ {
			for d := 1; d < 10; d++ {
				df := factorsOf[byte('0' + d)]
				rem2 := R2 - (currC2 + df[0])
				rem3 := R3 - (currC3 + df[1])
				rem5 := R5 - (currC5 + df[2])
				rem7 := R7 - (currC7 + df[3])

				if getMinLen(rem2, rem3, rem5, rem7) <= remLen-1-slot {
					res = append(res, byte('0'+d))
					currC2 += df[0]
					currC3 += df[1]
					currC5 += df[2]
					currC7 += df[3]
					break
				}
			}
		}
		return string(res)
	}

	L := maxInt(n+1, getMinLen(R2, R3, R5, R7))
	res := make([]byte, 0, L)
	currC2, currC3, currC5, currC7 := 0, 0, 0, 0

	for slot := 0; slot < L; slot++ {
		for d := 1; d < 10; d++ {
			df := factorsOf[byte('0' + d)]
			rem2 := R2 - (currC2 + df[0])
			rem3 := R3 - (currC3 + df[1])
			rem5 := R5 - (currC5 + df[2])
			rem7 := R7 - (currC7 + df[3])

			if getMinLen(rem2, rem3, rem5, rem7) <= L-1-slot {
				res = append(res, byte('0'+d))
				currC2 += df[0]
				currC3 += df[1]
				currC5 += df[2]
				currC7 += df[3]
				break
			}
		}
	}
	return string(res)
}

func containsZero(num string) bool {
	for i := 0; i < len(num); i++ {
		if num[i] == '0' {
			return true
		}
	}
	return false
}

func indexOfZero(num string) int {
	for i := 0; i < len(num); i++ {
		if num[i] == '0' {
			return i
		}
	}
	return -1
}

func runTest(caseNum int, num string, t int, expected string) {
	solver := &Solution{}
	result := solver.smallestNumber(num, t)
	status := "FAIL"
	if result == expected {
		status = "PASS"
	}
	fmt.Printf("Test Case %d:\n", caseNum)
	fmt.Printf("  Input:    num = '%s', t = %d\n", num, t)
	fmt.Printf("  Output:   %s\n", result)
	fmt.Printf("  Expected: %s\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(1, "1234", 256, "1488")
	// Example 2
	runTest(2, "12355", 50, "12355")
	// Example 3
	runTest(3, "11111", 26, "-1")
	// Custom Case 4 (Needs string len incremented)
	runTest(4, "99", 2, "112")
}
