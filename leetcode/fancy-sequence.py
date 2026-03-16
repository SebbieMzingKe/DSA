class Fancy(object):
    def __init__(self):
        self.seq = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def append(self, val):
        x = ((val - self.add) * pow(self.mult, self.MOD - 2, self.MOD)) % self.MOD
        self.seq.append(x)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD


if __name__ == "__main__":

    def run_test(case_num, actions, params, expected):
        print(f"--- Test Case {case_num} ---")
        obj = None
        results = []

        for i, action in enumerate(actions):
            if action == "Fancy":
                obj = Fancy()
                results.append(None)
            elif action == "append":
                obj.append(params[i][0])
                results.append(None)
            elif action == "addAll":
                obj.addAll(params[i][0])
                results.append(None)
            elif action == "multAll":
                obj.multAll(params[i][0])
                results.append(None)
            elif action == "getIndex":
                res = obj.getIndex(params[i][0])
                results.append(res)

        status = "PASS" if results == expected else "FAIL"
        print(f"Output:   {results}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    actions1 = [
        "Fancy",
        "append",
        "addAll",
        "append",
        "multAll",
        "getIndex",
        "addAll",
        "append",
        "multAll",
        "getIndex",
        "getIndex",
        "getIndex",
    ]
    params1 = [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
    expected1 = [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
    run_test(1, actions1, params1, expected1)

    # Custom Case: Out of bounds index
    actions2 = ["Fancy", "append", "getIndex"]
    params2 = [[], [5], [1]]
    expected2 = [None, None, -1]
    run_test(2, actions2, params2, expected2)
