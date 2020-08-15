# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# 	push(x) -- Push element x onto stack.
# 	pop() -- Removes the element on top of the stack.
# 	top() -- Get the top element.
# 	getMin() -- Retrieve the minimum element in the stack.
#
#
#  
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#  
# Constraints:
#
#
# 	Methods pop, top and getMin operations will always be called on non-empty stacks.
#
#


class MinStack:
    # 使用辅助栈 同增同减
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min_stack = [float('inf')]
    #
    # def push(self, x: int) -> None:
    #     self.stack.append(x)
    #     self.min_stack.append(min(x, self.min_stack[-1]))
    #
    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.min_stack.pop()
    #
    # def top(self) -> int:
    #     return self.stack[-1]
    #
    # def getMin(self) -> int:
    #     return self.min_stack[-1]

    # 差值法 栈中保存的是元素与当时最小值的差值
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min = float('inf')
    #
    # def push(self, x: int) -> None:
    #     self.stack.append(x-self.min)
    #     if x < self.min:
    #         self.min = x
    #
    # def pop(self) -> None:
    #     x = self.stack.pop()
    #     if x < 0:
    #         self.min -= x
    #
    # def top(self) -> int:
    #     x = self.stack[-1]
    #     if x > 0:
    #         return self.min + x
    #     return self.min
    #
    # def getMin(self) -> int:
    #     return self.min

    # 使用一个栈
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.stack[-1][1] if self.stack else float('inf'))))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

