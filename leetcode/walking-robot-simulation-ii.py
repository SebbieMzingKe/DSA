class Robot(object):
    def __init__(self, width, height):
        self.w = width - 1
        self.h = height - 1
        self.perimeter = 2 * self.w + 2 * self.h
        self.pos = 0
        self.has_moved = False

    def step(self, num):
        self.has_moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self):
        if self.pos <= self.w:
            return [self.pos, 0]
        elif self.pos <= self.w + self.h:
            return [self.w, self.pos - self.w]
        elif self.pos <= 2 * self.w + self.h:
            return [self.w - (self.pos - self.w - self.h), self.h]
        else:
            return [0, self.h - (self.pos - 2 * self.w - self.h)]

    def getDir(self):
        if self.pos == 0:
            return "South" if self.has_moved else "East"
        elif self.pos <= self.w:
            return "East"
        elif self.pos <= self.w + self.h:
            return "North"
        elif self.pos <= 2 * self.w + self.h:
            return "West"
        else:
            return "South"


if __name__ == "__main__":

    def run_test(actions, params, expected):
        print(f"Executing sequence...")
        robot = None
        results = []

        for i, action in enumerate(actions):
            if action == "Robot":
                robot = Robot(params[i][0], params[i][1])
                results.append(None)
            elif action == "step":
                robot.step(params[i][0])
                results.append(None)
            elif action == "getPos":
                results.append(robot.getPos())
            elif action == "getDir":
                results.append(robot.getDir())

        status = "PASS" if results == expected else "FAIL"

        print(f"Output:   {results}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    actions1 = [
        "Robot",
        "step",
        "step",
        "getPos",
        "getDir",
        "step",
        "step",
        "step",
        "getPos",
        "getDir",
    ]
    params1 = [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
    expected1 = [None, None, None, [4, 0], "East", None, None, None, [1, 2], "West"]
    run_test(actions1, params1, expected1)

    # Custom Case: Full lap check (Testing the origin edge case)
    # 2x2 grid has perimeter of 4
    actions2 = ["Robot", "getDir", "step", "getDir", "getPos"]
    params2 = [[2, 2], [], [4], [], []]
    expected2 = [None, "East", None, "South", [0, 0]]
    run_test(actions2, params2, expected2)
