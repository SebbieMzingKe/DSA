class MinStack(object):
    
    def __init__(self):
        self.stack = []
        self.min_stack =[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        # elif self.min_stack[-1] < val:
        #     self.min_stack.append(self.min_stack[-1])
        # else:
        #     self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]